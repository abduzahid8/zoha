<script>
	import { onMount } from "svelte";
	import gsap from "gsap";
	import ScrollTrigger from "gsap/ScrollTrigger";
	import { t } from "$lib/i18n/index.svelte.js";

	const items = t("gallery.items");

	let gridRef = $state();

	onMount(() => {
		gsap.registerPlugin(ScrollTrigger);

		const cards = gridRef.querySelectorAll(".gallery-card");

		gsap.fromTo(
			cards,
			{ y: 60, autoAlpha: 0 },
			{
				y: 0,
				autoAlpha: 1,
				duration: 1.2,
				stagger: 0.15,
				ease: "expo.out",
				scrollTrigger: {
					trigger: gridRef,
					start: "top 80%",
				},
			},
		);
	});
</script>

<section
	id="gallery"
	class="w-full bg-[#050505] text-white py-32 md:py-48 border-t border-white/5 relative z-10 overflow-hidden"
>
	<div
		class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-[#3B82F6] opacity-[0.02] blur-[200px] rounded-full pointer-events-none"
	></div>

	<div class="max-w-7xl mx-auto px-6 md:px-24 relative z-10">
		<div
			class="flex flex-col md:flex-row justify-between items-start md:items-end gap-6 mb-16 md:mb-24"
		>
			<div>
				<span
					class="text-xs font-mono text-white/30 uppercase tracking-[0.3em] mb-6 block"
					>{t("gallery.label")}</span
				>
				<h2 class="text-5xl md:text-8xl font-serif tracking-tight">
					{t("gallery.title")}<br /><span class="italic text-white/40"
						>{t("gallery.title_italic")}</span
					>
				</h2>
			</div>
			<p
				class="text-white/50 font-sans max-w-sm text-lg leading-relaxed pb-2"
			>
				{t("gallery.description")}
			</p>
		</div>

		<div
			bind:this={gridRef}
			class="grid grid-cols-1 md:grid-cols-3 gap-6 md:gap-8"
		>
			{#each items as item, i}
				<figure
					class="gallery-card group relative rounded-3xl overflow-hidden border border-white/10 bg-[#0A0A0A] hover:border-white/20 transition-colors duration-700"
				>
					<div
						class="absolute top-6 left-6 z-20 font-serif text-5xl text-white/10 group-hover:text-white/20 transition-colors duration-700"
					>
						0{i + 1}
					</div>
					<div class="overflow-hidden h-[55vh] md:h-[60vh]">
						<img
							src={item.src}
							alt={item.alt}
							loading="lazy"
							class="w-full h-full object-cover object-top transform group-hover:scale-[1.02] transition-transform duration-700 ease-out"
						/>
					</div>
					<figcaption
						class="p-6 md:p-8 flex flex-col gap-2 border-t border-white/10"
					>
						<h3 class="text-2xl font-serif tracking-tight">
							{item.title}
						</h3>
						<p class="text-sm text-white/50 font-sans leading-relaxed">
							{item.desc}
						</p>
					</figcaption>
				</figure>
			{/each}
		</div>
	</div>
</section>
