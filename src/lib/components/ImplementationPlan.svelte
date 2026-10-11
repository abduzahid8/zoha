<script>
	import { onMount } from "svelte";
	import gsap from "gsap";
	import ScrollTrigger from "gsap/ScrollTrigger";
	import { t } from "$lib/i18n/index.svelte.js";

	const stages = t("plan.stages");

	let listRef = $state();

	onMount(() => {
		gsap.registerPlugin(ScrollTrigger);
		const rows = listRef.querySelectorAll(".plan-row");
		gsap.fromTo(
			rows,
			{ y: 40, autoAlpha: 0 },
			{
				y: 0,
				autoAlpha: 1,
				duration: 1,
				stagger: 0.1,
				ease: "expo.out",
				scrollTrigger: { trigger: listRef, start: "top 80%" },
			},
		);
	});
</script>

<section
	id="plan"
	class="w-full bg-[#050505] text-white py-32 md:py-48 border-t border-white/5 relative z-10 overflow-hidden"
>
	<div class="max-w-7xl mx-auto px-6 md:px-24 relative z-10">
		<span
			class="text-xs font-mono text-white/30 uppercase tracking-[0.3em] mb-6 block"
			>{t("plan.label")}</span
		>
		<div
			class="flex flex-col md:flex-row justify-between items-start md:items-end gap-6 mb-16"
		>
			<h2 class="text-5xl md:text-8xl font-serif tracking-tight">
				{t("plan.title")}<br /><span class="italic text-white/40"
					>{t("plan.title_italic")}</span
				>
			</h2>
			<p class="text-white/50 font-sans max-w-sm text-lg leading-relaxed">
				{t("plan.description")}
			</p>
		</div>

		<div bind:this={listRef} class="flex flex-col gap-4">
			{#each stages as stage}
				<div
					class="plan-row rounded-3xl border border-white/10 bg-[#0A0A0A] p-8 md:p-10 grid grid-cols-1 md:grid-cols-[1fr_1fr] gap-6"
				>
					<div>
						<h3 class="text-2xl md:text-3xl font-serif tracking-tight mb-3">
							{stage.title}
						</h3>
						<p class="text-sm text-white/50 font-sans leading-relaxed max-w-xl">
							{stage.desc}
						</p>
					</div>
					<div class="flex flex-col gap-3 text-sm font-sans">
						<div class="rounded-2xl bg-white/5 border border-white/10 p-4">
							<p class="font-mono text-[11px] uppercase tracking-widest text-white/40 mb-1">
								Tech
							</p>
							<p class="text-white/80">{stage.tech}</p>
						</div>
						<div class="rounded-2xl bg-[#3B82F6]/5 border border-[#3B82F6]/20 p-4">
							<p class="font-mono text-[11px] uppercase tracking-widest text-[#3B82F6] mb-1">
								AI
							</p>
							<p class="text-white/80">{stage.ai}</p>
						</div>
					</div>
				</div>
			{/each}
		</div>
	</div>
</section>
