export default {
  nav: {
    work: "Product",
    services: "Capabilities",
    agency: "About",
    demo: "Live Demo",
    lets_talk: "GitHub",
    lets_talk_mobile: "View on GitHub →",
  },
  social: {
    github: "GitHub",
    copilotkit: "CopilotKit",
  },
  hero: {
    title: "zoha",
    digital: "personal",
    experiences: "agent.",
    description:
      "A personal agent that does the work — and shows you how. Self-hosted, built on CopilotKit.",
    view_work: "See what it does",
    our_services: "How it works",
  },
  manifesto: {
    label: "Manifesto",
    text: "Zoha is a personal agent you run yourself. It works transparently — every action visible, every send gated by your approval. Your machine, your accounts, your rules. Built on CopilotKit.",
  },
  brands: {
    subtitle: "Plugs into the tools you already use",
  },
  showcase: {
    label: "What Zoha does",
    services: [
      {
        title: "Say it like a person",
        desc: "Ask in plain language. Zoha plans the steps, checks in when it is unsure, and keeps every thread in one place.",
        icon: "M8 10h.01M12 10h.01M16 10h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z",
      },
      {
        title: "Take control",
        desc: "Hand it a browser and it works for you — you watch every step on screen and can take over at any moment.",
        icon: "M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z",
      },
      {
        title: "Nothing leaves without your yes",
        desc: "Emails, messages, anything outbound — every action waits for your approve, edit, or deny. With receipts.",
        icon: "M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z",
      },
    ],
  },
  works: {
    title: "Built-in",
    title_italic: "surfaces.",
    description:
      "What Zoha plugs into out of the box. Everything runs where you run it.",
    col_id: "ID",
    col_project: "App",
    col_category: "Surface",
    col_year: "Status",
    cta: "Get started",
  },
  gallery: {
    label: "In the product",
    title: "See Zoha",
    title_italic: "in action.",
    description:
      "Real screens from the agent — browser, documents and finance, all gated by your approval.",
    items: [
      {
        src: "/screenshots/computer.png",
        alt: "Zoha agent computer screen with browser session",
        title: "Agent computer",
        desc: "A browser and files that stay with your agent.",
      },
      {
        src: "/screenshots/document.png",
        alt: "Zoha document screen filling a community visit form",
        title: "Documents",
        desc: "Review, fill and send forms — nothing leaves without your yes.",
      },
      {
        src: "/screenshots/finance.png",
        alt: "Zoha finance tracker screen organizing spending",
        title: "Finance tracker",
        desc: "Spending, savings, and a plan for what's next.",
      },
    ],
  },
  problem: {
    label: "Problem → Solution",
    title: "Tab-hopping is",
    title_italic: "the work.",
    description:
      "Work lives in five apps at once. Chatbots answer, but they don't act — and acting agents ask for blind trust.",
    problems: [
      {
        title: "Scattered tools",
        desc: "Email, calendar, docs, finance and browser tabs — every task means copy-paste between apps.",
      },
      {
        title: "Chatbots stop at words",
        desc: "They draft replies but can't operate the computer, fill the form, or track the spending.",
      },
      {
        title: "Agents demand blind trust",
        desc: "Black-box automation sends emails and moves data without showing its steps or asking first.",
      },
    ],
    solution_title: "Zoha acts — and shows how",
    solution_desc:
      "A personal agent you run yourself. It plans the steps, works visibly on screen, and waits for your yes before anything leaves.",
    solution_points: [
      "Plans multi-step tasks across Gmail, Calendar, Docs, Finance and Browser",
      "Every action visible — watch and take over at any moment",
      "Approvals gate every send, with receipts for review",
      "Self-hosted: your machine, your accounts, your rules",
    ],
  },
  team: {
    label: "Team",
    title: "Small team,",
    title_italic: "full stack.",
    description:
      "Two co-founders — engineering and strategy. Full-stack build plus accelerator and fundraising experience.",
    members: [
      {
        name: "Mamurov Xasan",
        initials: "MX",
        role: "Co-founder & CTO · ex Exadel",
        skills: ["React & full project stack", "AI agent builder @ GK", "SvelteKit", "APIs & integrations"],
        stack: ["React", "SvelteKit", "CopilotKit", "Hono", "Tailwind"],
      },
      {
        name: "Zohid Vohijonov",
        initials: "ZV",
        role: "Co-founder & CEO · Strategy",
        skills: ["Plug and Play accelerator", "Pre-seed soft commits", "E-com strategy @ Uzum"],
        stack: ["Strategy", "Uzum e-com", "Go-to-market"],
      },
    ],
  },
  why: {
    label: "Why us",
    title: "Why we can",
    title_italic: "ship this.",
    description:
      "We don't pitch slides — we ship a running prototype, real screens and a demo video.",
    points: [
      {
        title: "Working prototype, not mockups",
        desc: "Agent computer, documents and finance flows run today — see /demo and the screenshots.",
      },
      {
        title: "Deep in the stack",
        desc: "SvelteKit + CopilotKit + approvals architecture. We own the full loop from chat to side-effect.",
      },
      {
        title: "Design and motion craft",
        desc: "GSAP + Lenis cinematic site, phone-frame gallery, generated explainer videos with code.",
      },
      {
        title: "Trust-first engineering",
        desc: "Approvals before sends, receipts after — the safety story is the product story.",
      },
    ],
  },
  roadmap: {
    label: "Roadmap",
    title: "From idea",
    title_italic: "to launch.",
    description: "Four gates. Two are done — MVP is now.",
    stages: [
      {
        phase: "Idea",
        title: "Personal agent with receipts",
        desc: "Problem framing: act, don't just answer — with approvals.",
        status: "Done",
      },
      {
        phase: "Prototype",
        title: "Browser + surfaces running",
        desc: "Chat, computer control, docs and finance screens. Demo video cut.",
        status: "Done",
      },
      {
        phase: "MVP",
        title: "Approvals + 5 surfaces",
        desc: "Gmail, Calendar, Computer, Docs, Finance behind approval gates.",
        status: "Now",
      },
      {
        phase: "Launched",
        title: "Onboarding + mobile polish",
        desc: "One-command run, mobile app polish, evals dashboard, public launch.",
        status: "Next",
      },
    ],
  },
  plan: {
    label: "Implementation plan",
    title: "How we",
    title_italic: "build it.",
    description:
      "Stages, technologies, and the AI tooling behind each step.",
    stages: [
      {
        title: "1 · Foundations",
        tech: "SvelteKit, Tailwind v4, adapter-auto",
        ai: "CopilotKit account + model access",
        desc: "Self-hosted shell, auth, accounts model, deploy pipeline.",
      },
      {
        title: "2 · Agent core",
        tech: "CopilotKit, Hono API",
        ai: "Plan-then-act loop, tool calls, eval scripts",
        desc: "Chat, planning, tool use, conversation memory in one thread.",
      },
      {
        title: "3 · Surfaces",
        tech: "Gmail, Calendar, Docs, Finance, Browser",
        ai: "RAG over inbox/docs, transaction categorizer",
        desc: "Five connectors behind a single approval interface.",
      },
      {
        title: "4 · Trust layer",
        tech: "Approvals inbox, receipts log",
        ai: "Pre-send policy checks, post-action summaries",
        desc: "Approve / edit / deny every outbound action, review receipts.",
      },
      {
        title: "5 · Web + demo",
        tech: "Svelte 5, GSAP, Lenis, ffmpeg",
        ai: "Scripted explainer generator (motion/zoha_explainer.py)",
        desc: "This site, screenshots gallery, /demo video and prototype links.",
      },
    ],
  },
  demo: {
    label: "Live demo",
    title: "Watch Zoha",
    title_italic: "work.",
    description:
      "A 28-second cut plus the full 1:14 version. Then try the running prototype.",
    video_title: "Watch Zoha (0:28)",
    video_desc:
      "Short cut: ask once, watch it browse live, finish the paperwork and sort spending — approvals gate every send.",
    video_src: "/demo/zoha-explainer-dark.mp4",
    runtime: "0:28 · MP4 · with sound",
    chapters: [
      { t: "0:00", label: "Intro" },
      { t: "0:07", label: "Browse live" },
      { t: "0:14", label: "Paperwork done" },
      { t: "0:21", label: "Spending sorted" },
    ],
    explainer_title: "Full version (1:14)",
    explainer_desc:
      "End-to-end run: chat like a colleague, operate the computer with you in control, connect email, calendar, documents and finance.",
    explainer_src: "/demo/zoha-demo.mp4",
    prototype_title: "Working prototype",
    prototype_desc:
      "Clone, install, sign in with your CopilotKit account, and start it. Your data stays with the accounts you connect.",
    prototype_url: "https://github.com/CopilotKit/Zoha",
    prototype_cta: "Open prototype on GitHub",
    run_steps: ["npm install", "Sign in with CopilotKit", "npm run dev"],
    qa_title: "Try the sample Q&A",
    qa_desc:
      "Mini client-side demo of the agent's answering style. Pick a question — no backend needed.",
    qa: [
      {
        q: "What is Zoha?",
        a: "Zoha is a personal AI agent. It chats like a colleague, operates a computer with you in control, and connects email, calendar, documents and finance.",
      },
      {
        q: "Where does it run?",
        a: "On your machine — self-hosted. Install, sign in with CopilotKit, and start. Your data stays with the accounts you connect.",
      },
      {
        q: "How do approvals work?",
        a: "Nothing outbound happens without you. Zoha stops and asks — you approve, edit, or deny, and every action leaves a receipt.",
      },
      {
        q: "Is it free?",
        a: "Yes — free to use. You bring your own model access through CopilotKit.",
      },
    ],
    qa_placeholder: "Ask about Zoha…",
    api_title: "API access (documented)",
    api_desc:
      "Prototype REST surface the demo exercises. Base URL is illustrative — see repo for the live server.",
    api_base: "https://api.zoha.example/v1",
    endpoints: [
      { method: "GET", path: "/health", desc: "Liveness + model access status" },
      { method: "POST", path: "/chat", desc: "Send a message, stream plan + steps" },
      { method: "POST", path: "/approvals", desc: "Approve / edit / deny a pending action" },
      { method: "GET", path: "/receipts", desc: "List completed actions with receipts" },
    ],
    curl_title: "Example request",
    api_note: "Status: documented for the demo. Live endpoints ship with the self-hosted server in the prototype repo.",
    back_home: "← Back home",
  },
  testimonials: {
    label: "Principles",
    list: [
      {
        name: "Transparent by default",
        role: "Full visibility",
        text: "Every step is visible on screen. Watch what Zoha does and take over at any moment.",
      },
      {
        name: "Yours to run",
        role: "Self-hosted",
        text: "The agent runs on your machine, against the accounts you connect. You hold the keys.",
      },
      {
        name: "Ask before acting",
        role: "Approvals",
        text: "Nothing leaves without your yes. Every send is gated, and every action leaves a receipt.",
      },
    ],
  },
  stats: {
    items: [
      { label: "Self-hosted", limit: 100, suffix: "%", prefix: "" },
      { label: "Core tabs", limit: 5, suffix: "", prefix: "" },
      { label: "Vendor lock-in", limit: 0, suffix: "", prefix: "" },
      { label: "Commands to run it", limit: 3, suffix: "", prefix: "" },
    ],
  },
  faq: {
    label: "FAQ",
    title: "Frequently",
    title_italic: "Asked",
    description:
      "What Zoha is, how it runs, and what keeps you in control of everything it does.",
    still_questions: "Still have questions?",
    items: [
      {
        q: "What is Zoha?",
        a: "Zoha is a personal AI agent. It chats like a colleague, operates a computer with you in control, and connects to the tools you already use — email, calendar, documents, and your finances.",
      },
      {
        q: "Where does it run?",
        a: "On your machine. Zoha is self-hosted: install, sign in with your CopilotKit account, and start it. Your data stays with the accounts you connect.",
      },
      {
        q: "How do approvals work?",
        a: "Nothing outbound happens without you. When Zoha wants to send an email or take an action, it stops and asks — you approve, edit, or deny, and every completed action leaves a receipt you can review.",
      },
      {
        q: "Is it free?",
        a: "Yes. Zoha is free to use. You bring your own model access through CopilotKit.",
      },
    ],
  },
  footer: {
    cta_title: "Give Zoha the",
    cta_italic: "first task.",
    lets_talk: "GitHub",
    description:
      "A personal agent that does the work and shows you how. Self-hosted.",
    nav_title: "Navigation",
    nav_home: "Home",
    nav_services: "Capabilities",
    nav_works: "Surfaces",
    nav_faq: "FAQ",
    socials_title: "Connect",
    social_twitter: "X (Twitter)",
    social_instagram: "CopilotKit",
    social_linkedin: "GitHub Org",
    social_github: "Zoha Repository",
    contact_title: "Contact",
    contact_hours:
      "Open an issue on GitHub — every one gets read.",
    copyright: "© 2026 Zoha. All rights reserved.",
    built_by: "Built on",
    privacy: "Privacy",
    terms: "Issues",
    built_by_agency: "CopilotKit",
  },
  seo: {
    title: "Zoha — Personal agent",
    description:
      "A personal AI agent that does the work and shows you how. Self-hosted, built on CopilotKit — with approvals before anything leaves.",
  },
};
