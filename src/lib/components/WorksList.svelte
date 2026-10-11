<script>
	import { t } from "$lib/i18n/index.svelte.js";

	const works = [
		{
			id: "01",
			name: "Gmail",
			category: "Email",
			year: "Live",
			url: "https://github.com/CopilotKit/Zoha",
		},
		{
			id: "02",
			name: "Calendar",
			category: "Scheduling",
			year: "Live",
			url: "https://github.com/CopilotKit/Zoha",
		},
		{
			id: "03",
			name: "Computer",
			category: "Agent browser — take control",
			year: "Live",
			url: "https://github.com/CopilotKit/Zoha",
		},
		{
			id: "04",
			name: "Docs",
			category: "Documents",
			year: "Live",
			url: "https://github.com/CopilotKit/Zoha",
		},
		{
			id: "05",
			name: "Finance",
			category: "Spending tracker",
			year: "Live",
			url: "https://github.com/CopilotKit/Zoha",
		},
	];
</script>

<section
	id="work"
	class="w-full bg-[#050505] text-white py-32 border-t border-white/10 min-h-screen"
>
	<div
		class="px-6 md:px-24 mb-24 max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-end gap-6"
	>
		<h2 class="text-5xl md:text-8xl font-serif tracking-tight">
			{t("works.title")}<br /><span class="italic text-white/40">{t("works.title_italic")}</span>
		</h2>
		<p
			class="text-white/50 font-sans max-w-sm text-lg leading-relaxed pb-2"
		>
			{t("works.description")}
		</p>
	</div>

	<div class="px-6 md:px-24 max-w-7xl mx-auto flex flex-col">
		<!-- Table Header -->
		<div
			class="flex border-b border-white/20 pb-4 mb-4 text-xs font-mono text-white/40 uppercase tracking-widest px-4"
		>
			<div class="w-16">{t("works.col_id")}</div>
			<div class="flex-1">{t("works.col_project")}</div>
			<div class="hidden md:block w-1/3">{t("works.col_category")}</div>
			<div class="w-16 text-right">{t("works.col_year")}</div>
		</div>

		<!-- Table Rows -->
		{#each works as work}
			<a
				href={work.url}
				target="_blank"
				rel="noopener noreferrer"
				class="group flex items-center border-b border-white/10 py-8 md:py-12 px-4 hover:bg-white/5 transition-colors duration-500 cursor-pointer relative overflow-hidden"
			>
				<div
					class="absolute inset-0 bg-linear-to-r from-[#3B82F6]/0 via-[#3B82F6]/5 to-[#3B82F6]/0 transform translate-y-full group-hover:translate-y-0 transition-transform duration-500 pointer-events-none"
				></div>

				<div
					class="w-16 text-sm font-mono text-white/30 group-hover:text-white/80 transition-colors z-10"
				>
					{work.id}
				</div>
				<div class="flex-1 z-10">
					<h3
						class="text-4xl md:text-6xl font-serif text-white/70 group-hover:text-white group-hover:translate-x-4 transition-all duration-500 transform-gpu"
					>
						{work.name}
					</h3>
				</div>
				<div
					class="hidden md:block w-1/3 text-lg font-sans font-light text-white/40 group-hover:text-white/80 transition-colors z-10"
				>
					{work.category}
				</div>
				<div
					class="w-16 text-right text-sm font-mono text-white/40 group-hover:text-white/90 transition-colors z-10"
				>
					{work.year}
				</div>
			</a>
		{/each}

		<div class="mt-16 flex justify-center w-full">
			<a
				href="#contact"
				class="px-8 py-3 rounded-full border border-white/20 text-white/80 hover:bg-white hover:text-black transition-colors duration-500 font-sans cursor-pointer text-sm font-medium inline-block"
			>
				{t("works.cta")}
			</a>
		</div>
	</div>
</section>
