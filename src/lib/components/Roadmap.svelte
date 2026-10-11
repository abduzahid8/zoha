<script>
	import { onMount } from "svelte";
	import gsap from "gsap";
	import ScrollTrigger from "gsap/ScrollTrigger";
	import { t } from "$lib/i18n/index.svelte.js";

	const stages = t("roadmap.stages");

	let gridRef = $state();

	function statusStyle(status) {
		if (status === "Done" || status === "Tayyor")
			return "bg-emerald-400/10 text-emerald-300 border-emerald-400/30";
		if (status === "Now" || status === "Hozir")
			return "bg-[#3B82F6]/10 text-[#7aa5ff] border-[#3B82F6]/40";
		return "bg-white/5 text-white/50 border-white/15";
	}

	onMount(() => {
		gsap.registerPlugin(ScrollTrigger);
		const cards = gridRef.querySelectorAll(".roadmap-card");
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
	id="roadmap"
	class="w-full bg-[#050505] text-white py-32 md:py-48 border-t border-white/5 relative z-10 overflow-hidden"
>
	<div class="max-w-7xl mx-auto px-6 md:px-24 relative z-10">
		<span
			class="text-xs font-mono text-white/30 uppercase tracking-[0.3em] mb-6 block"
			>{t("roadmap.label")}</span
		>
		<div
			class="flex flex-col md:flex-row justify-between items-start md:items-end gap-6 mb-16"
		>
			<h2 class="text-5xl md:text-8xl font-serif tracking-tight">
				{t("roadmap.title")}<br /><span class="italic text-white/40"
					>{t("roadmap.title_italic")}</span
				>
			</h2>
			<p class="text-white/50 font-sans max-w-sm text-lg leading-relaxed">
				{t("roadmap.description")}
			</p>
		</div>

		<div
			bind:this={gridRef}
			class="grid grid-cols-1 md:grid-cols-4 gap-6"
		>
			{#each stages as stage, i}
				<div
					class="roadmap-card relative rounded-3xl border border-white/10 bg-[#0A0A0A] p-8 flex flex-col gap-4"
				>
					<div class="flex items-center justify-between">
						<span class="font-mono text-xs uppercase tracking-widest text-white/40">
							{i + 1} · {stage.phase}
						</span>
						<span
							class="rounded-full border px-3 py-1 font-mono text-[11px] uppercase tracking-widest {statusStyle(
								stage.status,
							)}"
						>
							{stage.status}
						</span>
					</div>
					<h3 class="text-xl font-serif tracking-tight">{stage.title}</h3>
					<p class="text-sm text-white/50 font-sans leading-relaxed">
						{stage.desc}
					</p>
				</div>
			{/each}
		</div>
	</div>
</section>
