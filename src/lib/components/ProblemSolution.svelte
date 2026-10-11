<script>
	import { onMount } from "svelte";
	import gsap from "gsap";
	import ScrollTrigger from "gsap/ScrollTrigger";
	import { t } from "$lib/i18n/index.svelte.js";

	const problems = t("problem.problems");
	const points = t("problem.solution_points");

	let gridRef = $state();

	onMount(() => {
		gsap.registerPlugin(ScrollTrigger);
		const cards = gridRef.querySelectorAll(".problem-card");
		gsap.fromTo(
			cards,
			{ y: 60, autoAlpha: 0 },
			{
				y: 0,
				autoAlpha: 1,
				duration: 1.2,
				stagger: 0.15,
				ease: "expo.out",
				scrollTrigger: { trigger: gridRef, start: "top 80%" },
			},
		);
	});
</script>

<section
	id="problem"
	class="w-full bg-[#050505] text-white py-32 md:py-48 border-t border-white/5 relative z-10 overflow-hidden"
>
	<div
		class="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[400px] bg-[#3B82F6] opacity-[0.03] blur-[200px] rounded-full pointer-events-none"
	></div>

	<div class="max-w-7xl mx-auto px-6 md:px-24 relative z-10">
		<span
			class="text-xs font-mono text-white/30 uppercase tracking-[0.3em] mb-6 block"
			>{t("problem.label")}</span
		>
		<div
			class="flex flex-col md:flex-row justify-between items-start md:items-end gap-6 mb-16"
		>
			<h2 class="text-5xl md:text-8xl font-serif tracking-tight">
				{t("problem.title")}<br /><span class="italic text-white/40"
					>{t("problem.title_italic")}</span
				>
			</h2>
			<p class="text-white/50 font-sans max-w-sm text-lg leading-relaxed">
				{t("problem.description")}
			</p>
		</div>

		<div
			bind:this={gridRef}
			class="grid grid-cols-1 md:grid-cols-3 gap-6 md:gap-8 mb-8"
		>
			{#each problems as problem, i}
				<div
					class="problem-card rounded-3xl border border-white/10 bg-[#0A0A0A] p-8 flex flex-col gap-4"
				>
					<div class="font-serif text-5xl text-white/10">0{i + 1}</div>
					<h3 class="text-2xl font-serif tracking-tight">{problem.title}</h3>
					<p class="text-sm text-white/50 font-sans leading-relaxed">
						{problem.desc}
					</p>
				</div>
			{/each}
		</div>

		<div
			class="rounded-3xl border border-[#3B82F6]/30 bg-[#3B82F6]/5 p-8 md:p-12"
		>
			<h3 class="text-3xl md:text-5xl font-serif tracking-tight mb-4">
				{t("problem.solution_title")}
			</h3>
			<p class="text-white/60 font-sans text-lg max-w-3xl mb-8">
				{t("problem.solution_desc")}
			</p>
			<ul class="grid grid-cols-1 md:grid-cols-2 gap-4">
				{#each points as point}
					<li class="flex items-start gap-3 text-sm text-white/80 font-sans">
						<span
							class="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-[#3B82F6] text-xs text-white"
							>✓</span
						>
						{point}
					</li>
				{/each}
			</ul>
		</div>
	</div>
</section>
