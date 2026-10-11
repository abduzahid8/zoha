<script>
	import { onMount } from "svelte";
	import gsap from "gsap";
	import ScrollTrigger from "gsap/ScrollTrigger";
	import { t } from "$lib/i18n/index.svelte.js";

	const members = t("team.members");

	let gridRef = $state();

	onMount(() => {
		gsap.registerPlugin(ScrollTrigger);
		const cards = gridRef.querySelectorAll(".team-card");
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
	id="team"
	class="w-full bg-[#050505] text-white py-32 md:py-48 border-t border-white/5 relative z-10 overflow-hidden"
>
	<div class="max-w-7xl mx-auto px-6 md:px-24 relative z-10">
		<span
			class="text-xs font-mono text-white/30 uppercase tracking-[0.3em] mb-6 block"
			>{t("team.label")}</span
		>
		<div
			class="flex flex-col md:flex-row justify-between items-start md:items-end gap-6 mb-16"
		>
			<h2 class="text-5xl md:text-8xl font-serif tracking-tight">
				{t("team.title")}<br /><span class="italic text-white/40"
					>{t("team.title_italic")}</span
				>
			</h2>
			<p class="text-white/50 font-sans max-w-sm text-lg leading-relaxed">
				{t("team.description")}
			</p>
		</div>

		<div
			bind:this={gridRef}
			class="grid grid-cols-1 md:grid-cols-2 gap-6 md:gap-8 max-w-5xl mx-auto"
		>
			{#each members as member}
				<article
					class="team-card rounded-3xl border border-white/10 bg-[#0A0A0A] p-8 flex flex-col gap-6 hover:border-white/20 transition-colors duration-500"
				>
					<div
						class="flex h-16 w-16 items-center justify-center rounded-full bg-[#3B82F6]/15 border border-[#3B82F6]/30 font-serif text-xl text-white"
					>
						{member.initials}
					</div>
					<div>
						<h3 class="text-2xl font-serif tracking-tight">{member.name}</h3>
						<p class="font-mono text-xs uppercase tracking-widest text-[#3B82F6] mt-2">
							{member.role}
						</p>
					</div>
					<div>
						<p class="font-mono text-[11px] uppercase tracking-widest text-white/30 mb-3">
							Skills
						</p>
						<div class="flex flex-wrap gap-2">
							{#each member.skills as skill}
								<span
									class="rounded-full border border-white/15 px-3 py-1 text-xs font-sans text-white/70"
									>{skill}</span
								>
							{/each}
						</div>
					</div>
					<div>
						<p class="font-mono text-[11px] uppercase tracking-widest text-white/30 mb-3">
							Stack
						</p>
						<div class="flex flex-wrap gap-2">
							{#each member.stack as tech}
								<span
									class="rounded-full bg-white/5 px-3 py-1 text-xs font-sans text-white/60"
									>{tech}</span
								>
							{/each}
						</div>
					</div>
				</article>
			{/each}
		</div>
	</div>
</section>
