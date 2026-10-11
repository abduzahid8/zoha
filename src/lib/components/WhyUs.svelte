<script>
	import { onMount } from "svelte";
	import gsap from "gsap";
	import ScrollTrigger from "gsap/ScrollTrigger";
	import { t } from "$lib/i18n/index.svelte.js";

	const points = t("why.points");

	let gridRef = $state();

	onMount(() => {
		gsap.registerPlugin(ScrollTrigger);
		const cards = gridRef.querySelectorAll(".why-card");
		gsap.fromTo(
			cards,
			{ y: 60, autoAlpha: 0 },
			{
				y: 0,
				autoAlpha: 1,
				duration: 1.2,
				stagger: 0.12,
				ease: "expo.out",
				scrollTrigger: { trigger: gridRef, start: "top 80%" },
			},
		);
	});
</script>

<section
	id="why"
	class="w-full bg-[#050505] text-white py-32 md:py-48 border-t border-white/5 relative z-10 overflow-hidden"
>
	<div
		class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[700px] h-[700px] bg-[#3B82F6] opacity-[0.03] blur-[200px] rounded-full pointer-events-none"
	></div>

	<div class="max-w-7xl mx-auto px-6 md:px-24 relative z-10">
		<span
			class="text-xs font-mono text-white/30 uppercase tracking-[0.3em] mb-6 block"
			>{t("why.label")}</span
		>
		<div
			class="flex flex-col md:flex-row justify-between items-start md:items-end gap-6 mb-16"
		>
			<h2 class="text-5xl md:text-8xl font-serif tracking-tight">
				{t("why.title")}<br /><span class="italic text-white/40"
					>{t("why.title_italic")}</span
				>
			</h2>
			<p class="text-white/50 font-sans max-w-sm text-lg leading-relaxed">
				{t("why.description")}
			</p>
		</div>

		<div
			bind:this={gridRef}
			class="grid grid-cols-1 md:grid-cols-2 gap-6 md:gap-8"
		>
			{#each points as point, i}
				<div
					class="why-card rounded-3xl border border-white/10 bg-[#0A0A0A] p-8 md:p-10 flex gap-6"
				>
					<div class="font-serif text-4xl text-[#3B82F6]/60">0{i + 1}</div>
					<div>
						<h3 class="text-2xl font-serif tracking-tight mb-3">
							{point.title}
						</h3>
						<p class="text-sm text-white/50 font-sans leading-relaxed">
							{point.desc}
						</p>
					</div>
				</div>
			{/each}
		</div>

		<div class="mt-10 flex justify-center">
			<a
				href="/demo"
				class="px-8 py-3 rounded-full bg-white text-black font-sans text-sm font-medium hover:bg-[#3B82F6] hover:text-white transition-colors duration-500"
			>
				{t("nav.demo")} →
			</a>
		</div>
	</div>
</section>
