#!/usr/bin/env python3
"""Zoha — 27.8s landscape motion explainer (stylized UI mockup animation).

Usage:
    python3 zoha_explainer.py                 # light version
    python3 zoha_explainer.py --dark          # black-background version
    python3 zoha_explainer.py --preview [t…]  # still frames (add --dark for dark)
"""

import math
import os
import sys

sys.path.insert(0, "/Users/v.zahid/Downloads/video-editing-tools/motion-skills")

import numpy as np
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

from motion_engine.color import parse_color
from motion_engine.easing import get_easing
from motion_engine.elements import Circle, Element, ImageElement, Rect, Text
from motion_engine.renderer import VideoWriter
from motion_engine.scene import Scene

# ---------------------------------------------------------------- constants

DARK = "--dark" in sys.argv

W, H, FPS = 1920, 1080, 30
ROOT = "/Users/v.zahid/startups/zoha/openmuse"
MASCOT = os.path.join(ROOT, "apps/mobile/assets/capybara.png")
OUT = os.path.join(
    ROOT,
    "assets/demos/2026-10-11/"
    + ("zoha-explainer-dark.mp4" if DARK else "zoha-explainer.mp4"),
)

C = {
    "canvas": "#FCFCFC",
    "card": "#FFFFFF",
    "text": "#11191C",
    "muted": "#697176",
    "line": "#EEEEF0",
    "blue": "#C8E7FF",
    "blueDark": "#1473C8",
    "sky": "#EDF7FD",
    "green": "#E3F3E8",
    "lavender": "#F0EEFA",
    "orange": "#FDF0DF",
    "bubble": "#F1F3F4",
    "track": "#E7E9EB",
    "live": "#2F9E68",
    "attach": "#E8963E",
    # page-level ink (left column, intro, outro) — adapts to the theme
    "ink": "#11191C",
    "inkMuted": "#697176",
    "inkAccent": "#1473C8",
    "railOff": "#E7E9EB",
}

if DARK:
    C.update({
        "canvas": "#0A0B10",
        "ink": "#F4F6F8",
        "inkMuted": "#A9B2B9",
        "inkAccent": "#7FB8EC",
        "railOff": "#262B31",
    })

RGB = {k: parse_color(v) for k, v in C.items()}
RGBA = {k: parse_color(v).rgba for k, v in C.items()}

FONT_PATH = "/System/Library/Fonts/HelveticaNeue.ttc"
WEIGHTS = {"r": 0, "b": 1, "m": 10, "l": 7}
_font_cache = {}

# phone mockup geometry
CARD_W, CARD_H = 560, 820
CARD_CX, CARD_CY = 1330, 540
IX0, IX1 = 1086, 1574
IW = IX1 - IX0

# timeline
T_INTRO_OUT = 3.9
S1_IN, S1_OUT = 4.3, 11.15
S2_IN, S2_OUT = 11.6, 18.05
S3_IN, S3_OUT = 18.5, 24.2
S4_IN = 24.6
TOTAL = 27.8

EASE_IN_CUBIC = get_easing("ease_in_cubic")
EASE_OUT_QUINT = get_easing("ease_out_quint")
EASE_INOUT_CUBIC = get_easing("ease_in_out_cubic")
EASE_OUT_EXPO = get_easing("ease_out_expo")
EASE_OUT_BACK = get_easing("ease_out_back")


def clamp01(v):
    return 0.0 if v < 0 else (1.0 if v > 1 else v)


def lerp(a, b, t):
    return a + (b - a) * t


def smoothstep(t):
    t = clamp01(t)
    return t * t * (3 - 2 * t)


def track(s):
    return " ".join(s.upper())


def get_font(size, weight="r"):
    key = (int(size), weight)
    if key not in _font_cache:
        _font_cache[key] = ImageFont.truetype(FONT_PATH, int(size), index=WEIGHTS[weight])
    return _font_cache[key]


# ---------------------------------------------------------------- elements


class T(Text):
    """Text element with Helvetica Neue weight selection.

    Renders with baseline anchors and full ascender/descender line boxes,
    so descender-free lines are never clipped (the engine's tight-bbox
    math cuts them off).
    """

    def __init__(self, text, size, color, weight="r", **kw):
        kw.setdefault("align", "left")
        super().__init__(text, font_size=size, color=color, font=FONT_PATH, **kw)
        self.weight = weight
        self._font_obj = None

    def _get_font(self):
        if self._font_obj is None:
            self._font_obj = get_font(self.font_size, self.weight)
        return self._font_obj

    def _metrics(self):
        f = self._get_font()
        asc, desc = f.getmetrics()
        lh = max(int(self.font_size * self.line_height), asc + desc)
        return f, asc, desc, lh

    def get_bounds(self):
        f, asc, desc, lh = self._metrics()
        lines = self._wrap_text(f)
        w = max([f.getlength(l) for l in lines] + [0])
        h = 4 + asc + lh * (len(lines) - 1) + desc + 4
        return (w + 8, h)

    def draw_content(self, img):
        d = ImageDraw.Draw(img)
        f, asc, desc, lh = self._metrics()
        lines = self._wrap_text(f)
        img_w = img.width
        if self.align == "center":
            anchor, x = "ms", img_w / 2
        elif self.align == "right":
            anchor, x = "rs", img_w - 4
        else:
            anchor, x = "ls", 4
        for i, line in enumerate(lines):
            if not line.strip():
                continue
            d.text((x, 4 + asc + i * lh), line, font=f,
                   fill=self.color.rgba, anchor=anchor)
        return img


class Card(Element):
    """Rounded card with a soft drop shadow (content is cached)."""

    PAD = 46

    def __init__(self, width, height, color=None, radius=40, shadow=True,
                 border_color=None, border_width=0, **kw):
        super().__init__(**kw)
        self.width = width
        self.height = height
        self.color = parse_color(color or C["card"])
        self.radius = radius
        self.shadow = shadow
        self.border_color = parse_color(border_color) if border_color else None
        self.border_width = border_width
        self._cache = None

    def get_bounds(self):
        return (self.width + 2 * self.PAD, self.height + 2 * self.PAD)

    def _build(self):
        p = self.PAD
        w, h = int(self.width), int(self.height)
        canvas = Image.new("RGBA", (w + 2 * p, h + 2 * p), (0, 0, 0, 0))
        if self.shadow:
            sh = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
            d = ImageDraw.Draw(sh)
            d.rounded_rectangle([p, p + 16, p + w - 1, p + h + 16],
                                radius=self.radius, fill=(17, 25, 28, 70))
            sh = sh.filter(ImageFilter.GaussianBlur(30))
            canvas.alpha_composite(sh)
        d = ImageDraw.Draw(canvas)
        d.rounded_rectangle([p, p, p + w - 1, p + h - 1],
                            radius=self.radius, fill=self.color.rgba)
        if self.border_color and self.border_width:
            d.rounded_rectangle([p, p, p + w - 1, p + h - 1], radius=self.radius,
                                outline=self.border_color.rgba,
                                width=self.border_width)
        self._cache = canvas

    def draw_content(self, img):
        if self._cache is None:
            self._build()
        img.paste(self._cache, (0, 0), self._cache)
        return img


class R(Rect):
    """Rect with a friendlier `radius` kwarg."""

    def __init__(self, width, height, color=None, radius=0, **kw):
        super().__init__(width, height, color=color, border_radius=radius, **kw)


def put(scene, el, t_in, t_out, anim="fade_in", eanim="fade_out",
        edur=0.45, xdur=0.4, ease="ease_out_quint", xease="ease_in_cubic", z=5):
    scene.add(el, enter=t_in, dur=max(0.05, t_out - t_in), exit=t_out,
              enter_anim=anim, exit_anim=eanim, enter_dur=edur, exit_dur=xdur,
              enter_easing=ease, exit_easing=xease, z_index=z)


# ---------------------------------------------------------------- background


class BackdropScene(Scene):
    """Scene whose canvas starts with drifting, colour-keyframed soft blobs."""

    KEYS_LIGHT = [
        (0.0, "#C8E7FF", "#F0EEFA"),
        (5.2, "#C8E7FF", "#EDF7FD"),
        (13.2, "#F0EEFA", "#EDF7FD"),
        (20.6, "#E3F3E8", "#F0EEFA"),
        (26.2, "#C8E7FF", "#F0EEFA"),
    ]
    KEYS_DARK = [
        (0.0, "#1B5FAA", "#5650A0"),
        (5.2, "#1B5FAA", "#2E6E8E"),
        (13.2, "#5650A0", "#2E6E8E"),
        (20.6, "#2E7D4F", "#5650A0"),
        (26.2, "#1B5FAA", "#5650A0"),
    ]
    STRENGTH_LIGHT = (0.85, 0.75)
    STRENGTH_DARK = (0.62, 0.55)

    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self.KEYS = self.KEYS_DARK if DARK else self.KEYS_LIGHT
        self.STRENGTH = self.STRENGTH_DARK if DARK else self.STRENGTH_LIGHT
        self._masks = (
            self._radial(1650, 120, 620),
            self._radial(150, 1010, 660),
        )
        self._blob_a = np.zeros((H, W), np.float32)
        self._blob_b = np.zeros((H, W), np.float32)

    @staticmethod
    def _radial(cx, cy, r):
        ys, xs = np.mgrid[0:H, 0:W].astype(np.float32)
        d2 = ((xs - cx) ** 2 + (ys - cy) ** 2) / (r * r)
        return np.exp(-d2 * 1.45).astype(np.float32)

    def _colors_at(self, t):
        keys = self.KEYS
        if t <= keys[0][0]:
            a, b = keys[0][1], keys[0][2]
        elif t >= keys[-1][0]:
            a, b = keys[-1][1], keys[-1][2]
        else:
            for i in range(len(keys) - 1):
                t0, a0, b0 = keys[i]
                t1, a1, b1 = keys[i + 1]
                if t0 <= t <= t1:
                    k = smoothstep((t - t0) / (t1 - t0))
                    a = tuple(lerp(x, y, k) for x, y in zip(parse_color(a0).rgb, parse_color(a1).rgb))
                    b = tuple(lerp(x, y, k) for x, y in zip(parse_color(b0).rgb, parse_color(b1).rgb))
                    return np.array(a, np.float32), np.array(b, np.float32)
        return np.array(parse_color(a).rgb, np.float32), np.array(parse_color(b).rgb, np.float32)

    def render_frame(self, t):
        canvas = super().render_frame(t)
        arr = np.asarray(canvas).astype(np.float32)

        ax = int(round(46 * math.sin(t * 0.33)))
        ay = int(round(34 * math.cos(t * 0.26)))
        bx = int(round(-52 * math.sin(t * 0.24)))
        by = int(round(40 * math.cos(t * 0.31)))
        ma = np.roll(np.roll(self._masks[0], ay, axis=0), ax, axis=1)
        mb = np.roll(np.roll(self._masks[1], by, axis=0), bx, axis=1)

        ca, cb = self._colors_at(t)
        sa, sb = self.STRENGTH
        for mask, col, strength in ((ma, ca, sa), (mb, cb, sb)):
            a = (mask * strength)[..., None]
            arr[..., :3] = arr[..., :3] * (1 - a) + col * a

        return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))


# ---------------------------------------------------------------- scene 1


def build_intro(scene):
    t0, t1 = 0.0, T_INTRO_OUT

    put(scene, ImageElement(MASCOT, width=350, pos=(520, 330), anchor=(0, 0)),
        0.15, t1, anim="bounce_in", ease="ease_out_back", eanim="scale_out",
        xease="ease_in_cubic", edur=0.7, xdur=0.45, z=3)

    blocks = [
        (T(track("personal agent"), 24, C["inkAccent"], "b", anchor=(0, 0.5)),
         930, 318, 0.30),
        (T("Zoha", 150, C["ink"], "b", anchor=(0, 0)), 930, 346, 0.45),
        (T("A personal agent with a browser, terminal, files, and work that keeps going.",
           36, C["inkMuted"], max_width=700, line_height=1.35, anchor=(0, 0)),
         930, 580, 0.80),
    ]
    for el, x, y, tin in blocks:
        el.x, el.y = x, y
        put(scene, el, tin, t1, anim="fade_right", edur=0.55)

    chips = [
        ("Browse", 146, "blue", "blueDark"),
        ("Documents", 190, "lavender", "text"),
        ("Money", 140, "green", "text"),
    ]
    x = 930
    for i, (label, cw, bg, fg) in enumerate(chips):
        pill = R(cw, 58, C[bg], radius=29)
        pill.x, pill.y = x, 772
        put(scene, pill, 1.15 + i * 0.14, t1, anim="fade_up", edur=0.5)
        txt = T(label, 24, C[fg], "b", align="center", anchor=(0.5, 0.5))
        txt.x, txt.y = x + cw / 2, 801
        put(scene, txt, 1.2 + i * 0.14, t1, anim="fade_up", edur=0.5)
        x += cw + 16


def build_browse(scene):
    t0, t1 = S1_IN, S1_OUT

    left_column(scene, "01 / browse", "Ask once.\nIt browses live.",
                "Follow the agent's browser right in the chat — then take the wheel.",
                t0, t1)

    card = Card(CARD_W, CARD_H, radius=42)
    card.x, card.y = CARD_CX, CARD_CY
    put(scene, card, t0 + 0.05, t1, anim="slide_left", ease="ease_out_quint",
        edur=0.6, eanim="scale_out", xease="ease_in_cubic", z=1)

    # header
    put(scene, ImageElement(MASCOT, width=48, pos=(IX0, 172), anchor=(0, 0)),
        t0 + 0.4, t1, z=6)
    put(scene, T("Zoha", 26, C["text"], "b", pos=(1146, 196), anchor=(0, 0.5)),
        t0 + 0.4, t1, z=6)
    put(scene, Circle(6, C["live"], pos=(1524, 196)), t0 + 0.45, t1, z=6)
    put(scene, T("live", 18, C["muted"], anchor=(1, 0.5), pos=(1574, 196)),
        t0 + 0.45, t1, z=6)
    put(scene, R(IW, 2, C["line"], pos=(IX0, 246), anchor=(0, 0)),
        t0 + 0.4, t1, z=6)

    # user bubble
    put(scene, R(430, 120, C["sky"], radius=24, pos=(1144, 288), anchor=(0, 0)),
        t0 + 0.7, t1, anim="fade_up", z=6)
    put(scene, T("Find today's top stories on Hacker News", 26, C["text"],
                 max_width=370, pos=(1174, 348), anchor=(0, 0.5)),
        t0 + 0.85, t1, z=7)

    # agent bubble + inline browser card
    put(scene, R(440, 240, C["bubble"], radius=24, pos=(IX0, 438), anchor=(0, 0)),
        t0 + 1.3, t1, anim="fade_up", z=6)
    put(scene, R(392, 46, C["card"], radius=23, border_color=C["line"],
                    border_width=1, pos=(1110, 462), anchor=(0, 0)),
        t0 + 1.5, t1, z=7)
    put(scene, Circle(6, C["live"], pos=(1132, 485)), t0 + 1.55, t1, z=7)
    put(scene, T("news.ycombinator.com", 20, C["muted"], pos=(1148, 485),
                 anchor=(0, 0.5)), t0 + 1.55, t1, z=7)

    rows = [
        (C["blueDark"], "Show HN: Local models on a laptop"),
        ("#5FA3E0", "Ask HN: What are you building?"),
        (C["blue"], "Zoha is now open source"),
    ]
    for i, (col, headline) in enumerate(rows):
        y = 542 + 44 * i
        put(scene, R(14, 14, col, radius=4, pos=(1110, y - 7), anchor=(0, 0)),
            t0 + 1.75 + i * 0.12, t1, z=7)
        put(scene, T(headline, 20, C["text"], pos=(1134, y), anchor=(0, 0.5)),
            t0 + 1.75 + i * 0.12, t1, z=7)

    # take control
    put(scene, T("Hands you the same live session.", 20, C["muted"],
                 pos=(IX0, 826), anchor=(0, 0.5)), t0 + 3.0, t1, z=7)
    btn = R(246, 58, C["blue"], radius=29, pos=(IX0, 745), anchor=(0, 0))
    put(scene, btn, t0 + 3.1, t1, anim="bounce_in", ease="ease_out_back",
        edur=0.5, z=7)
    put(scene, T("Take control", 24, C["blueDark"], "b", align="center",
                 anchor=(0.5, 0.5), pos=(1209, 774)), t0 + 3.2, t1, z=8)


# ---------------------------------------------------------------- scene 2


def build_docs(scene):
    t0, t1 = S2_IN, S2_OUT

    left_column(scene, "02 / documents", "It finishes\nthe paperwork.",
                "Mail search, a filled PDF, and a reply you approve.",
                t0, t1)

    card = Card(CARD_W, CARD_H, radius=42)
    card.x, card.y = CARD_CX, CARD_CY
    put(scene, card, t0 + 0.05, t1, anim="slide_left", ease="ease_out_quint",
        edur=0.6, eanim="scale_out", xease="ease_in_cubic", z=1)

    put(scene, ImageElement(MASCOT, width=48, pos=(IX0, 172), anchor=(0, 0)),
        t0 + 0.4, t1, z=6)
    put(scene, T("Zoha", 26, C["text"], "b", pos=(1146, 196), anchor=(0, 0.5)),
        t0 + 0.4, t1, z=6)
    put(scene, Circle(6, C["live"], pos=(1524, 196)), t0 + 0.45, t1, z=6)
    put(scene, T("live", 18, C["muted"], anchor=(1, 0.5), pos=(1574, 196)),
        t0 + 0.45, t1, z=6)
    put(scene, R(IW, 2, C["line"], pos=(IX0, 246), anchor=(0, 0)),
        t0 + 0.4, t1, z=6)

    # mail thread
    put(scene, R(IW, 172, C["sky"], radius=22, pos=(IX0, 276), anchor=(0, 0)),
        t0 + 0.7, t1, anim="fade_up", z=6)
    put(scene, T("School trip — permission slip", 24, C["text"], "b",
                 pos=(1110, 316), anchor=(0, 0.5)), t0 + 0.85, t1, z=7)
    put(scene, T("Ms. Rivera · 9:14 AM", 19, C["muted"], pos=(1110, 354),
                 anchor=(0, 0.5)), t0 + 0.9, t1, z=7)
    put(scene, R(340, 50, C["card"], radius=25, pos=(1110, 380), anchor=(0, 0)),
        t0 + 1.0, t1, z=7)
    put(scene, Circle(8, C["attach"], pos=(1132, 405)), t0 + 1.1, t1, z=8)
    put(scene, T("permission-slip.pdf", 20, C["text"], pos=(1150, 405),
                 anchor=(0, 0.5)), t0 + 1.1, t1, z=8)
    put(scene, T("128 KB", 18, C["muted"], anchor=(1, 0.5), pos=(1430, 405)),
        t0 + 1.1, t1, z=8)

    # pdf form
    put(scene, R(IW, 296, C["card"], radius=22, border_color=C["line"],
                    border_width=2, pos=(IX0, 468), anchor=(0, 0)),
        t0 + 1.35, t1, anim="fade_up", z=6)
    put(scene, T(track("permission slip"), 16, C["muted"], "b", pos=(1110, 502),
                 anchor=(0, 0.5)), t0 + 1.5, t1, z=7)
    put(scene, T("Filled from the email", 18, C["muted"], anchor=(1, 0.5),
                 pos=(1548, 502)), t0 + 1.5, t1, z=7)
    put(scene, R(440, 1, C["line"], pos=(1110, 528), anchor=(0, 0)),
        t0 + 1.5, t1, z=7)

    labels = [track("student"), track("grade"), track("date")]
    for i, lab in enumerate(labels):
        y = 568 + i * 72
        put(scene, T(lab, 16, C["muted"], "b", pos=(1110, y), anchor=(0, 0.5)),
            t0 + 1.55 + i * 0.05, t1, z=7)
        if i < 2:
            put(scene, R(440, 1, C["line"], pos=(1110, y + 36), anchor=(0, 0)),
                t0 + 1.55, t1, z=7)

    # send + receipt
    put(scene, R(IW, 62, C["blue"], radius=31, pos=(IX0, 778), anchor=(0, 0)),
        t0 + 4.0, t1, anim="bounce_in", ease="ease_out_back", edur=0.5, z=7)
    put(scene, T("Review & send", 24, C["blueDark"], "b", align="center",
                 anchor=(0.5, 0.5), pos=(1330, 809)), t0 + 4.1, t1, z=8)
    put(scene, R(IW, 54, C["green"], radius=27, pos=(IX0, 854), anchor=(0, 0)),
        t0 + 5.0, t1, anim="fade_up", z=7)
    put(scene, Circle(9, C["live"], pos=(1116, 881)), t0 + 5.1, t1, z=8)
    put(scene, T("Reply sent · receipt saved", 21, C["text"], pos=(1138, 881),
                 anchor=(0, 0.5)), t0 + 5.1, t1, z=8)


# ---------------------------------------------------------------- scene 3

BARS = [
    ("Rent", "$1,450", 1450, "#1473C8"),
    ("Groceries", "$620", 620, "#4E9BDD"),
    ("Transport", "$310", 310, "#8FC4EF"),
    ("Fun", "$440", 440, "#C8E7FF"),
]


def build_money(scene):
    t0, t1 = S3_IN, S3_OUT

    left_column(scene, "03 / money", "Your spending,\nsorted.",
                "Drop a CSV. Get a plan, categories, and totals.", t0, t1)

    card = Card(CARD_W, CARD_H, radius=42)
    card.x, card.y = CARD_CX, CARD_CY
    put(scene, card, t0 + 0.05, t1, anim="slide_left", ease="ease_out_quint",
        edur=0.6, eanim="scale_out", xease="ease_in_cubic", z=1)

    put(scene, ImageElement(MASCOT, width=48, pos=(IX0, 172), anchor=(0, 0)),
        t0 + 0.4, t1, z=6)
    put(scene, T("Zoha", 26, C["text"], "b", pos=(1146, 196), anchor=(0, 0.5)),
        t0 + 0.4, t1, z=6)
    put(scene, Circle(6, C["live"], pos=(1524, 196)), t0 + 0.45, t1, z=6)
    put(scene, T("live", 18, C["muted"], anchor=(1, 0.5), pos=(1574, 196)),
        t0 + 0.45, t1, z=6)
    put(scene, R(IW, 2, C["line"], pos=(IX0, 246), anchor=(0, 0)),
        t0 + 0.4, t1, z=6)

    # import row
    put(scene, R(IW, 56, C["green"], radius=18, pos=(IX0, 276), anchor=(0, 0)),
        t0 + 0.6, t1, anim="fade_up", z=6)
    put(scene, Circle(11, C["blueDark"], pos=(1116, 304)), t0 + 0.7, t1, z=7)
    put(scene, T("transactions.csv", 22, C["text"], "b", pos=(1138, 304),
                 anchor=(0, 0.5)), t0 + 0.7, t1, z=7)
    put(scene, T("412 rows", 19, C["muted"], anchor=(1, 0.5), pos=(1556, 304)),
        t0 + 0.7, t1, z=7)

    # stat tiles
    put(scene, R(236, 120, C["green"], radius=20, pos=(IX0, 352), anchor=(0, 0)),
        t0 + 0.85, t1, anim="fade_up", z=6)
    put(scene, T(track("income"), 16, C["muted"], "b", pos=(1110, 382),
                 anchor=(0, 0.5)), t0 + 0.95, t1, z=7)
    put(scene, R(236, 120, C["orange"], radius=20, pos=(1338, 352), anchor=(0, 0)),
        t0 + 0.95, t1, anim="fade_up", z=6)
    put(scene, T(track("spent"), 16, C["muted"], "b", pos=(1362, 382),
                 anchor=(0, 0.5)), t0 + 1.05, t1, z=7)

    put(scene, T(track("remaining"), 16, C["muted"], "b", pos=(IX0, 506),
                 anchor=(0, 0.5)), t0 + 2.0, t1, z=7)
    put(scene, T("$1,680", 26, C["text"], "b", anchor=(1, 0.5), pos=(IX1, 506)),
        t0 + 2.0, t1, z=7)

    for i, (name, val, _, _) in enumerate(BARS):
        y = 560 + i * 60
        put(scene, T(name, 22, C["text"], pos=(IX0, y), anchor=(0, 0.5)),
            t0 + 2.1 + i * 0.1, t1, z=7)
        put(scene, T(val, 20, C["muted"], anchor=(1, 0.5), pos=(IX1, y)),
            t0 + 2.1 + i * 0.1, t1, z=7)
        put(scene, R(IW, 14, C["track"], radius=7, pos=(IX0, y + 14),
                        anchor=(0, 0)), t0 + 2.1 + i * 0.1, t1, z=7)

    # savings chip
    put(scene, R(IW, 56, C["blue"], radius=28, pos=(IX0, 786), anchor=(0, 0)),
        t0 + 4.1, t1, anim="fade_up", z=7)
    put(scene, T("Move $300 to savings", 23, C["blueDark"], "b", align="center",
                 anchor=(0.5, 0.5), pos=(1330, 814)), t0 + 4.2, t0 + 4.8, z=8,
        eanim="fade_out", xdur=0.2)
    put(scene, T("Scheduled for Nov 1", 23, C["blueDark"], "b", align="center",
                 anchor=(0.5, 0.5), pos=(1330, 814)), t0 + 5.05, t1, z=8,
        anim="fade_up", edur=0.35)
    put(scene, T("finance-summary.md saved to workspace", 19, C["muted"],
                 align="center", anchor=(0.5, 0.5), pos=(1330, 886)),
        t0 + 4.5, t1, z=7)


# ---------------------------------------------------------------- shared bits


def left_column(scene, label, headline, sub, t0, t1):
    put(scene, T(track(label), 24, C["inkAccent"], "b", pos=(120, 396),
                 anchor=(0, 0.5)), t0 + 0.1, t1, anim="fade_right", edur=0.5)
    put(scene, T(headline, 78, C["ink"], "b", max_width=760, line_height=1.12,
                 pos=(120, 440), anchor=(0, 0)), t0 + 0.25, t1,
        anim="fade_right", edur=0.65)
    put(scene, T(sub, 30, C["inkMuted"], max_width=620, line_height=1.4,
                 pos=(120, 662), anchor=(0, 0)), t0 + 0.5, t1,
        anim="fade_right", edur=0.55)


def build_outro(scene):
    t1 = TOTAL

    mascot = ImageElement(MASCOT, width=260, pos=(830, 250), anchor=(0, 0))
    put(scene, mascot, S4_IN + 0.05, t1, anim="bounce_in", ease="ease_out_back",
        edur=0.7, z=3)

    put(scene, T("Zoha", 110, C["ink"], "b", align="center", anchor=(0.5, 0.5),
                 pos=(960, 600)), S4_IN + 0.25, t1, anim="fade_up", edur=0.6)
    put(scene, T("A personal agent that keeps going.", 32, C["inkMuted"],
                 align="center", anchor=(0.5, 0.5), pos=(960, 692)),
        S4_IN + 0.45, t1, anim="fade_up", edur=0.55)

    pill = R(560, 68, C["card"], radius=34, border_color=C["line"],
                border_width=2, pos=(680, 736), anchor=(0, 0))
    put(scene, pill, S4_IN + 0.7, t1, anim="fade_up", edur=0.55, z=4)
    put(scene, T("github.com/CopilotKit/Zoha", 26, C["text"], align="center",
                 anchor=(0.5, 0.5), pos=(960, 770)), S4_IN + 0.8, t1,
        anim="fade_up", edur=0.55, z=5)
    put(scene, T("Open source · MIT · Built with CopilotKit", 22, C["inkMuted"],
                 align="center", anchor=(0.5, 0.5), pos=(960, 864)),
        S4_IN + 1.0, t1, anim="fade_up", edur=0.55, z=5)


# ---------------------------------------------------------------- dynamics


def draw_cursor(d, x, y, alpha=1.0, scale=1.0):
    pts = [(0, 0), (0, 32), (8, 25), (13, 36), (19, 34), (13, 23), (23, 23)]
    a = int(255 * clamp01(alpha))
    if a <= 0:
        return
    poly = [(x + px * scale, y + py * scale) for px, py in pts]
    d.line(poly + [poly[0]], fill=(17, 25, 28, a), width=3, joint="curve")
    d.polygon(poly, fill=(255, 255, 255, a))


def draw_click(d, cx, cy, t_click, t, color=(20, 115, 200)):
    if not (t_click <= t < t_click + 0.45):
        return
    p = (t - t_click) / 0.45
    r = 8 + 62 * EASE_OUT_QUINT(p)
    a = int(210 * (1 - p))
    if a <= 0:
        return
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color + (a,), width=4)


def scene1_dynamic(layer, t):
    d = ImageDraw.Draw(layer)

    # attention pulse on the button before the click
    if 7.9 <= t < 9.55:
        for i in range(2):
            ph = ((t - 7.9) * 0.85 + i * 0.5) % 1.0
            r = 44 + 76 * ph
            a = int(130 * (1 - ph))
            if a <= 0:
                continue
            d.ellipse([1209 - r, 774 - r * 0.75, 1209 + r, 774 + r * 0.75],
                      outline=(20, 115, 200, a), width=3)

    # cursor + click wash/ripple are drawn first (under the takeover),
    # then the live-session takeover, then the cursor on top.
    if 9.0 <= t < 11.6:
        if 9.55 <= t < 9.8:
            a = int(200 * (1 - (t - 9.55) / 0.25))
            d.rounded_rectangle([IX0, 745, IX0 + 246, 803], radius=29,
                                fill=(255, 255, 255, max(a, 0)))
        draw_click(d, 1209, 774, 9.55, t)

    # live-session takeover
    if 9.7 <= t < 11.6:
        p = EASE_OUT_QUINT(clamp01((t - 9.7) / 0.55))
        x = lerp(IX0, IX0, p)
        y = lerp(745, 264, p)
        w = lerp(246, IW, p)
        h = lerp(58, 650, p)
        r = lerp(29, 24, p)
        fade = clamp01((11.55 - t) / 0.35)

        win = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        wd = ImageDraw.Draw(win)
        wd.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=(255, 255, 255, 255))

        body = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        bd = ImageDraw.Draw(body)
        for i, cx in enumerate((1112, 1136, 1160)):
            bd.ellipse([cx - 8, 292, cx + 8, 308], fill=(226, 229, 231, 255))
        bd.rounded_rectangle([1194, 278, 1490, 322], radius=22,
                             fill=(243, 245, 246, 255))
        bd.text((1216, 300), "news.ycombinator.com", font=get_font(18),
                fill=RGBA["muted"], anchor="lm")
        bd.rounded_rectangle([1506, 282, 1574, 318], radius=18, fill=RGBA["blue"])
        bd.text((1540, 300), "LIVE", font=get_font(16, "b"), fill=RGBA["blueDark"],
                anchor="mm")
        bd.rectangle([IX0, 344, IX1, 346], fill=RGBA["line"])
        bd.rounded_rectangle([1086, 378, 1104, 396], radius=5, fill=(245, 166, 35, 255))
        bd.text((1116, 388), "Hacker News", font=get_font(26, "b"),
                fill=RGBA["text"], anchor="lm")
        stories = [
            ("Show HN: Local models on a laptop", "412 pts", C["blueDark"]),
            ("Ask HN: What are you building?", "268 pts", "#5FA3E0"),
            ("Zoha is now open source", "519 pts", C["blue"]),
            ("The browser is the new shell", "133 pts", "#B9D9F4"),
        ]
        for i, (title, score, col) in enumerate(stories):
            yy = 452 + i * 60
            bd.rounded_rectangle([1086, yy - 8, 1102, yy + 8], radius=4,
                                 fill=parse_color(col).rgba)
            bd.text((1116, yy), title, font=get_font(22), fill=RGBA["text"],
                    anchor="lm")
            bd.text((IX1, yy), score, font=get_font(18), fill=RGBA["muted"],
                    anchor="rm")
        bd.rounded_rectangle([1086, 830, 1302, 882], radius=26, fill=(255, 255, 255, 255),
                             outline=RGBA["line"], width=2)
        bd.text((1194, 856), "Back to chat", font=get_font(20), fill=RGBA["muted"],
                anchor="mm")
        bd.rounded_rectangle([1338, 830, 1574, 882], radius=26, fill=RGBA["blue"])
        bd.text((1456, 856), "You're driving", font=get_font(20, "b"),
                fill=RGBA["blueDark"], anchor="mm")

        mask = Image.new("L", (W, H), 0)
        ImageDraw.Draw(mask).rounded_rectangle([x, y, x + w, y + h], radius=r, fill=255)
        win.alpha_composite(body)
        alpha = ImageChops.multiply(win.getchannel("A"), mask)
        win.putalpha(alpha.point(lambda v: int(v * fade)))

        layer.alpha_composite(win)

    # cursor on top of everything
    if 9.0 <= t < 11.6:
        fade = clamp01((11.55 - t) / 0.25)
        if t < 9.5:
            p = EASE_INOUT_CUBIC(clamp01((t - 9.0) / 0.5))
            x = lerp(1790, 1209, p)
            y = lerp(1010, 774, p)
        elif t < 10.0:
            x, y = 1209, 774
        else:
            p = EASE_INOUT_CUBIC(clamp01((t - 10.0) / 0.6))
            x = lerp(1209, 1305, p)
            y = lerp(774, 690, p)
        draw_cursor(d, x, y, alpha=fade)


def scene2_dynamic(layer, t):
    d = ImageDraw.Draw(layer)

    fields = [
        ("Maya Alvarez", 13.3, 13.8),
        ("4B", 14.0, 14.2),
        ("Fri, Oct 24", 14.35, 14.75),
    ]
    for i, (value, a, b) in enumerate(fields):
        y = 568 + i * 72
        if t < a:
            continue
        p = clamp01((t - a) / (b - a))
        n = int(math.ceil(len(value) * p)) if p < 1 else len(value)
        shown = value[:n]
        d.text((1260, y), shown, font=get_font(24), fill=RGBA["text"], anchor="lm")
        if p < 1:
            tw = get_font(24).getlength(shown)
            blink = 1.0 if int(t * 6) % 2 == 0 else 0.25
            d.rectangle([1266 + tw, y - 15, 1270 + tw, y + 15],
                        fill=RGBA["blueDark"][:3] + (int(235 * blink),))

        check_at = b + 0.14
        if t >= check_at:
            s = EASE_OUT_BACK(clamp01((t - check_at) / 0.35))
            r = 15 * max(s, 0.01)
            d.ellipse([1530 - r, y - r, 1530 + r, y + r], fill=RGBA["live"])
            if s > 0.55:
                d.line([(1530 - 7, y), (1530 - 2, y + 5), (1530 + 7, y - 6)],
                       fill=(255, 255, 255, 255), width=3, joint="curve")

    # cursor (wash + ripple first so the opaque cursor stays on top)
    if 15.75 <= t < 18.2:
        if 16.28 <= t < 16.53:
            a = int(200 * (1 - (t - 16.28) / 0.25))
            d.rounded_rectangle([IX0, 778, IX1, 840], radius=31,
                                fill=(255, 255, 255, max(a, 0)))
        draw_click(d, 1330, 809, 16.28, t)
        fade = clamp01((18.15 - t) / 0.25)
        if t < 16.25:
            p = EASE_INOUT_CUBIC(clamp01((t - 15.75) / 0.5))
            x = lerp(1790, 1330, p)
            y = lerp(1010, 809, p)
        elif t < 16.9:
            x, y = 1330, 809
        else:
            p = EASE_INOUT_CUBIC(clamp01((t - 16.9) / 0.7))
            x = lerp(1330, 1440, p)
            y = lerp(809, 906, p)
        draw_cursor(d, x, y, alpha=fade)


def scene3_dynamic(layer, t):
    d = ImageDraw.Draw(layer)

    # counters
    if t >= 19.6:
        p = EASE_OUT_EXPO(clamp01((t - 19.6) / 0.9))
        d.text((1110, 432), f"${4820 * p:,.0f}", font=get_font(42, "b"),
               fill=RGBA["text"], anchor="lm")
        d.text((1362, 432), f"${3140 * p:,.0f}", font=get_font(42, "b"),
               fill=RGBA["text"], anchor="lm")

    # category bars
    for i, (_, _, val, col) in enumerate(BARS):
        start = 20.9 + i * 0.15
        if t < start:
            continue
        p = EASE_OUT_QUINT(clamp01((t - start) / 0.75))
        w = IW * (val / 1450.0) * p
        if w < 2:
            continue
        y = 560 + i * 60 + 14
        d.rounded_rectangle([IX0, y, IX0 + w, y + 14], radius=7,
                            fill=parse_color(col).rgba)

    # savings chip confirmation
    if t >= 23.5:
        s = EASE_OUT_BACK(clamp01((t - 23.5) / 0.35))
        r = 15 * max(s, 0.01)
        d.ellipse([1122 - r, 814 - r, 1122 + r, 814 + r], fill=(255, 255, 255, 255))
        if s > 0.55:
            d.line([(1115, 814), (1120, 819), (1129, 808)],
                   fill=RGBA["blueDark"], width=3, joint="curve")

    # cursor (wash + ripple first so the opaque cursor stays on top)
    if 22.8 <= t < 24.4:
        if 23.3 <= t < 23.55:
            a = int(200 * (1 - (t - 23.3) / 0.25))
            d.rounded_rectangle([IX0, 786, IX1, 842], radius=28,
                                fill=(255, 255, 255, max(a, 0)))
        draw_click(d, 1330, 814, 23.3, t)
        fade = clamp01((24.35 - t) / 0.3)
        if t < 23.25:
            p = EASE_INOUT_CUBIC(clamp01((t - 22.8) / 0.45))
            x = lerp(1790, 1330, p)
            y = lerp(1010, 814, p)
        elif t < 23.9:
            x, y = 1330, 814
        else:
            p = EASE_INOUT_CUBIC(clamp01((t - 23.9) / 0.5))
            x = lerp(1330, 1470, p)
            y = lerp(814, 906, p)
        draw_cursor(d, x, y, alpha=fade)


def draw_rail(d, t):
    if not (S1_IN <= t < S3_OUT):
        return
    active = 0 if t < S2_IN else (1 if t < S3_IN else 2)
    cols = []
    for i in range(3):
        if i < active:
            cols.append("#8FC4EF")
        elif i == active:
            cols.append(C["inkAccent"])
        else:
            cols.append(C["railOff"])
    for i, col in enumerate(cols):
        x = 120 + i * 108
        d.rounded_rectangle([x, 1004, x + 96, 1011], radius=3,
                            fill=parse_color(col).rgba)


def dynamic(canvas, t, frame_num):
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    draw_rail(d, t)
    del d

    if t < S2_IN:
        scene1_dynamic(layer, t)
    elif t < 18.25:
        scene2_dynamic(layer, t)
    elif t < 24.6:
        scene3_dynamic(layer, t)

    canvas.alpha_composite(layer)
    return canvas


# ---------------------------------------------------------------- render


def render(path=OUT, preview_times=None, preview_dir=None):
    scene = BackdropScene(W, H, fps=FPS, duration=TOTAL, bg=C["canvas"])
    build_intro(scene)
    build_browse(scene)
    build_docs(scene)
    build_money(scene)
    build_outro(scene)
    scene.on_frame(dynamic)

    if preview_times is not None:
        os.makedirs(preview_dir, exist_ok=True)
        for t in preview_times:
            img = scene.render_frame(t)
            for cb in scene._frame_callbacks:
                img = cb(img, t, int(t * FPS))
            name = os.path.join(preview_dir, f"frame_{t:05.2f}.png")
            img.convert("RGB").save(name)
            print("wrote", name)
        return

    writer = VideoWriter(path, W, H, FPS, codec="avc1")
    total = int(TOTAL * FPS)
    try:
        for f in range(total):
            t = f / FPS
            canvas = scene.render_frame(t)
            for cb in scene._frame_callbacks:
                canvas = cb(canvas, t, f)
            writer.write_frame(canvas)
            if f % FPS == 0:
                sys.stdout.write(f"\r{int(100 * f / total)}% ({f}/{total})")
                sys.stdout.flush()
        sys.stdout.write(f"\r100% ({total}/{total})\n")
    finally:
        writer.close()
    print("wrote", path)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--dark"]
    if args and args[0] == "--preview":
        times = ([float(x) for x in args[1:]]
                 or [1.4, 5.6, 7.6, 9.9, 10.6, 13.9, 16.4, 20.6, 23.5, 26.2])
        render(preview_times=times,
               preview_dir=os.path.join(
                   ROOT, "assets/motion/" + ("preview-dark" if DARK else "preview")))
    else:
        render()
