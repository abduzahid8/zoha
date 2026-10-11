<script>
    import { onMount } from "svelte";
    import { gsap } from "gsap";
    import { ScrollTrigger } from "gsap/ScrollTrigger";
    import { afterNavigate } from "$app/navigation";
    import Lenis from "lenis";
    import "lenis/dist/lenis.css";
    import "./layout.css";
    import favicon from "$lib/assets/favicon.svg";
    import Header from "$lib/components/header.svelte";
    import Cursor from "$lib/components/Cursor.svelte";

    let { children } = $props();
    let lenis;

    // Reset scroll on route changes. Lenis lives in the layout and survives
    // client-side navigations, so it kept enforcing the previous page's
    // scroll position (landing users at the bottom of /demo). Hash
    // navigations are skipped so #section links keep working.
    afterNavigate((navigation) => {
        ScrollTrigger.refresh();
        if (navigation?.to?.url?.hash) return;
        if (!lenis) return;
        lenis.scrollTo(0, { immediate: true });
        window.scrollTo(0, 0);
    });

    onMount(() => {
        gsap.registerPlugin(ScrollTrigger);

        // Lenis'i başlat (Smooth Scrolling)
        lenis = new Lenis({
            autoRaf: true,
            duration: 1.2,
            easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
            direction: "vertical",
            gestureDirection: "vertical",
            smooth: true,
            smoothTouch: false,
            touchMultiplier: 2,
        });

        // GSAP ScrollTrigger'ın Scroll güncellemelerini Lenis'e bağla
        lenis.on("scroll", ScrollTrigger.update);

        gsap.ticker.add((time) => {
            lenis.raf(time * 1000);
        });

        gsap.ticker.lagSmoothing(0);

        return () => {
            const instance = lenis;
            lenis = null;
            instance.destroy();
            gsap.ticker.remove(instance.raf);
        };
    });
</script>

<svelte:head>
    <link rel="icon" href={favicon} />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
        href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@300;400;500;600&display=swap"
        rel="stylesheet"
    />
</svelte:head>

<Cursor />
<Header />

<main class="app-wrapper">
    {@render children()}
</main>
