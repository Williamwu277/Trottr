<script lang="ts">
	import type { PageServerData } from './$types';
	import PoiCard from '$lib/components/PoiCard.svelte';
	export let data: PageServerData;
</script>

<div
	class="bg-light w-screen box-border bottom-0 left-0 rounded-t-[34px] flex flex-col items-center pt-5 pb-6 absolute"
>
	<div class="bg-sub rounded-full h-[6px] w-[245px] mb-4" />
	<div class="flex flex-col gap-[36px] mb-10">
		{#each data.locations as l}
			<PoiCard name={l.name} time={l.time} />
		{/each}
	</div>
	<div class="flex gap-2 font-bold text-[20px]">
		<a
			class="bg-sub text-accent rounded-[19px] flex justify-center items-center w-[143px] h-[65px]"
			href="/search">Add Place</a
		>
		<button
			class="bg-accent text-light rounded-[19px] flex justify-center items-center w-[199px] h-[65px]"
			>Use AI</button
		>
	</div>
</div>
