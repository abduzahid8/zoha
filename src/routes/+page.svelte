<script>
	import Hero from "$lib/components/Hero.svelte";
	import Manifesto from "$lib/components/Manifesto.svelte";
	import ProblemSolution from "$lib/components/ProblemSolution.svelte";
	import Brands from "$lib/components/Brands.svelte";
	import Showcase from "$lib/components/Showcase.svelte";
	import WorksList from "$lib/components/WorksList.svelte";
	import Gallery from "$lib/components/Gallery.svelte";
	import Team from "$lib/components/Team.svelte";
	import WhyUs from "$lib/components/WhyUs.svelte";
	import Roadmap from "$lib/components/Roadmap.svelte";
	import ImplementationPlan from "$lib/components/ImplementationPlan.svelte";
	import Testimonials from "$lib/components/Testimonials.svelte";
	import Stats from "$lib/components/Stats.svelte";
	import Faq from "$lib/components/Faq.svelte";
	import Footer from "$lib/components/Footer.svelte";
	import Seo from "$lib/components/Seo.svelte";
</script>

<Seo />

<div class="bg-[#050505] text-white">
	<Hero />
	<Manifesto />
	<ProblemSolution />
	<Brands />
	<Showcase />
	<WorksList />
	<Gallery />
	<Team />
	<WhyUs />
	<Roadmap />
	<ImplementationPlan />
	<Testimonials />
	<Stats />
	<Faq />
	<Footer />
</div>
