<script>
	import Footer from "$lib/components/Footer.svelte";
	import { t } from "$lib/i18n/index.svelte.js";

	const chapters = t("demo.chapters");
	const endpoints = t("demo.endpoints");

	const curl = `curl -X POST ${t("demo.api_base")}/chat \\
  -H "Content-Type: application/json" \\
  -d '{"message": "Organize my spending", "approve": "manual"}'`;
</script>

<svelte:head>
	<title>{t("demo.title")} {t("demo.title_italic")} — Zoha</title>
	<meta name="description" content={t("demo.description")} />
</svelte:head>

<div class="bg-[#050505] text-white min-h-screen pt-32 pb-0">
	<div class="max-w-7xl mx-auto px-6 md:px-24">
		<a href="/" class="text-sm font-sans text-white/50 hover:text-white transition-colors">
			{t("demo.back_home")}
		</a>

		<span
			class="text-xs font-mono text-white/30 uppercase tracking-[0.3em] mt-8 mb-6 block"
			>{t("demo.label")}</span
		>
		<h1 class="text-5xl md:text-8xl font-serif tracking-tight">
			{t("demo.title")}<br /><span class="italic text-white/40"
				>{t("demo.title_italic")}</span
			>
		</h1>
		<p class="text-white/50 font-sans max-w-2xl text-lg leading-relaxed mt-6">
			{t("demo.description")}
		</p>

		<!-- 6.1 Demo video -->
		<div class="mt-16 rounded-3xl overflow-hidden border border-white/10 bg-black">
			<video
				controls
				preload="metadata"
				poster="/screenshots/computer.png"
				src={t("demo.video_src")}
				class="w-full aspect-video"
			>
				<track kind="captions" />
			</video>
		</div>
		<div class="mt-6 flex flex-col md:flex-row md:items-center gap-4 justify-between">
			<div>
				<h2 class="text-2xl font-serif">{t("demo.video_title")}</h2>
				<p class="text-white/50 font-sans text-sm mt-2 max-w-2xl">
					{t("demo.video_desc")}
				</p>
			</div>
			<div class="flex flex-col items-start md:items-end gap-3">
				<span
					class="rounded-full border border-white/15 px-4 py-1.5 font-mono text-xs text-white/60"
					>{t("demo.runtime")}</span
				>
				<div class="flex flex-wrap gap-2">
					{#each chapters as ch}
						<span
							class="rounded-full bg-white/5 px-3 py-1 font-mono text-[11px] text-white/50"
							>{ch.t} · {ch.label}</span
						>
					{/each}
				</div>
			</div>
		</div>

		<!-- Secondary explainer -->
		<div class="mt-12 grid grid-cols-1 md:grid-cols-2 gap-6 items-stretch">
			<div class="rounded-3xl overflow-hidden border border-white/10 bg-black">
				<video
					controls
					preload="metadata"
					poster="/screenshots/finance.png"
					src={t("demo.explainer_src")}
					class="w-full aspect-video"
				>
					<track kind="captions" />
				</video>
			</div>
			<div
				class="rounded-3xl border border-white/10 bg-[#0A0A0A] p-8 flex flex-col justify-center gap-4"
			>
				<h3 class="text-3xl font-serif">{t("demo.explainer_title")}</h3>
				<p class="text-white/50 font-sans">{t("demo.explainer_desc")}</p>
			</div>
		</div>

		<!-- Optional: API access -->
		<div class="mt-12 rounded-3xl border border-white/10 bg-[#0A0A0A] p-8 md:p-12 mb-24">
			<h2 class="text-3xl md:text-5xl font-serif tracking-tight mb-4">
				{t("demo.api_title")}
			</h2>
			<p class="text-white/50 font-sans mb-2">{t("demo.api_desc")}</p>
			<p class="font-mono text-sm text-[#3B82F6] mb-8">{t("demo.api_base")}</p>

			<div class="flex flex-col gap-3 mb-8">
				{#each endpoints as ep}
					<div
						class="flex flex-col md:flex-row md:items-center gap-2 md:gap-6 rounded-2xl bg-white/5 border border-white/10 px-6 py-4"
					>
						<span
							class="font-mono text-xs font-bold w-16 {ep.method === 'GET'
								? 'text-emerald-300'
								: 'text-[#7aa5ff]'}">{ep.method}</span
						>
						<code class="font-mono text-sm text-white/85">{ep.path}</code>
						<span class="font-sans text-sm text-white/50 md:ml-auto">{ep.desc}</span>
					</div>
				{/each}
			</div>

			<h3 class="font-mono text-xs uppercase tracking-widest text-white/40 mb-3">
				{t("demo.curl_title")}
			</h3>
			<pre
				class="rounded-2xl bg-black/60 border border-white/10 p-6 font-mono text-xs md:text-sm text-white/75 overflow-x-auto whitespace-pre">{curl}</pre>
			<p class="font-sans text-sm text-white/40 mt-6">{t("demo.api_note")}</p>
		</div>
	</div>

	<Footer />
</div>
