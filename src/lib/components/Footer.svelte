<script>
	import { onMount } from "svelte";
	import Logo from "./logo.svelte";
	import { t } from "$lib/i18n/index.svelte.js";
</script>

<footer
	id="contact"
	class="w-full bg-[#050505] text-white pt-32 pb-12 relative overflow-hidden border-t border-white/10 border-b-8 border-b-white/5"
>
	<!-- CTA Section -->
	<div
		class="px-6 md:px-24 max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center mb-32 gap-12"
	>
		<h2
			class="text-[12vw] md:text-[7vw] font-serif leading-[0.85] tracking-tighter mix-blend-difference z-10 w-full md:w-2/3"
		>
			{t("footer.cta_title")}<br />
			<span class="italic text-white/40">{t("footer.cta_italic")}</span>
		</h2>
		<div class="w-full md:w-1/3 flex md:justify-end z-10">
			<a
				href="https://github.com/CopilotKit/Zoha"
				target="_blank"
				rel="noopener noreferrer"
				class="group relative flex items-center justify-center w-40 h-40 md:w-48 md:h-48 rounded-full bg-white text-black hover:scale-105 transition-transform duration-500 cursor-pointer"
			>
				<span
					class="absolute inset-0 bg-[#3B82F6] rounded-full transform scale-0 group-hover:scale-100 transition-transform duration-500 ease-out z-0"
				></span>
				<span
				class="font-sans font-medium text-lg relative z-10 group-hover:text-white transition-colors duration-500"
				>{t("footer.lets_talk")}</span
				>
			</a>
		</div>
	</div>

	<!-- Multi-Column Links Section -->
	<div
		class="px-6 md:px-24 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-12 md:gap-4 mb-24 z-10 relative"
	>
		<div class="col-span-1 md:col-span-1 flex flex-col gap-6">
			<div class="opacity-80"><Logo /></div>
			<p class="text-white/40 font-sans text-sm leading-relaxed max-w-xs">
				{t("footer.description")}
			</p>
		</div>

		<div class="col-span-1 flex flex-col gap-4">
			<h4
				class="font-mono text-xs uppercase tracking-widest text-[#3B82F6] mb-2"
			>
				{t("footer.nav_title")}
			</h4>
			<a
				href="#agency"
				class="text-white/60 hover:text-white font-sans text-sm transition-colors"
				>{t("footer.nav_home")}</a
			>
			<a
				href="#services"
				class="text-white/60 hover:text-white font-sans text-sm transition-colors"
				>{t("footer.nav_services")}</a
			>
			<a
				href="#work"
				class="text-white/60 hover:text-white font-sans text-sm transition-colors"
				>{t("footer.nav_works")}</a
			>
			<a
				href="#faq"
				class="text-white/60 hover:text-white font-sans text-sm transition-colors"
				>{t("footer.nav_faq")}</a
			>
			<a
				href="/demo"
				class="text-white hover:text-white font-sans text-sm font-semibold transition-colors"
				>{t("nav.demo")} →</a
			>
		</div>

		<div class="col-span-1 flex flex-col gap-4">
			<h4
				class="font-mono text-xs uppercase tracking-widest text-[#3B82F6] mb-2"
			>
				{t("footer.socials_title")}
			</h4>
			<a
				href="https://x.com/CopilotKit"
				target="_blank"
				rel="noopener noreferrer"
				class="text-white/60 hover:text-white font-sans text-sm transition-colors"
				>{t("footer.social_twitter")}</a
			>
			<a
				href="https://github.com/CopilotKit"
				target="_blank"
				rel="noopener noreferrer"
				class="text-white/60 hover:text-white font-sans text-sm transition-colors"
				>{t("footer.social_instagram")}</a
			>
			<a
				href="https://github.com/CopilotKit"
				target="_blank"
				rel="noopener noreferrer"
				class="text-white/60 hover:text-white font-sans text-sm transition-colors"
				>{t("footer.social_linkedin")}</a
			>
			<a
				href="https://github.com/CopilotKit/Zoha"
				target="_blank"
				rel="noopener noreferrer"
				class="text-[#3B82F6] hover:text-white font-sans text-sm transition-colors"
				>{t("footer.social_github")}</a
			>
		</div>

		<div class="col-span-1 flex flex-col gap-4">
			<h4
				class="font-mono text-xs uppercase tracking-widest text-[#3B82F6] mb-2"
			>
				{t("footer.contact_title")}
			</h4>
			<a
				href="https://github.com/CopilotKit/Zoha/issues"
				target="_blank"
				rel="noopener noreferrer"
				class="text-white/80 hover:text-white font-sans text-lg font-medium transition-colors"
			>
				github.com/CopilotKit/Zoha
			</a>
			<p class="text-white/40 font-sans text-sm mt-2">
				{t("footer.contact_hours")}
			</p>
		</div>
	</div>

	<!-- Copyright & Author Bar -->
	<div
		class="px-6 md:px-24 max-w-7xl mx-auto pt-8 border-t border-white/10 flex flex-col md:flex-row justify-between items-center gap-6 md:gap-4 text-xs font-mono text-base tracking-wider relative z-10"
	>
		<p class="text-white/30">{t("footer.copyright")}</p>

		<div class="flex flex-col md:flex-row items-center gap-4 md:gap-8">
			<span class="text-white/50 text-sm font-sans font-light">
				{t("footer.built_by")} <a
					href="https://github.com/CopilotKit"
					target="_blank"
					rel="noopener noreferrer"
					class="text-[#3B82F6] font-medium hover:text-white transition-colors duration-500 hover:underline underline-offset-4"
					>{t("footer.built_by_agency")}</a
				>
			</span>
			<div class="flex gap-6 text-white/30 hidden md:flex">
				<a
					href="#contact"
					class="hover:text-white/60 transition-colors"
					>{t("footer.privacy")}</a
				>
				<a
					href="https://github.com/CopilotKit/Zoha/issues"
					target="_blank"
					rel="noopener noreferrer"
					class="hover:text-white/60 transition-colors"
					>{t("footer.terms")}</a
				>
			</div>
		</div>
	</div>

	<!-- Giant background glow -->
	<div
		class="absolute bottom-0 left-1/2 -translate-x-1/2 w-screen h-[400px] bg-[#3B82F6] opacity-5 blur-[200px] pointer-events-none"
	></div>
</footer>
