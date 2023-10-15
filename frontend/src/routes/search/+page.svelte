<script lang="ts">
	import SearchBar from '$lib/components/NewSearchBar.svelte';
	import SuggestedCard from '$lib/components/SuggestedCard.svelte';
	import type { PageServerData } from './$types';

	export let data: PageServerData;
	let poiName: string = '';

	$: searchResults = fetch('http://localhost:5420/search', {
		method: 'post',
		body: JSON.stringify({ query: poiName })
	});
</script>

<div class="w-screen pt-4 px-8">
	<div class="mt-8 flex flex-col items-center">
		<SearchBar bind:text={poiName} />
	</div>
	{#if poiName === ''}
		<h2 class="uppercase mt-6 text-accent font-bold text-[18px]">Suggested</h2>
		<div class="flex flex-col items-center gap-[15px]">
			{#each data.suggested as poi}
				<SuggestedCard {poi} />
			{/each}
		</div>
	{:else}
		<h2 class="uppercase mt-6 text-accent font-bold text-[18px]">Search Results</h2>
		{#await searchResults}
			<p class="text-accent">Loading...</p>
		{:then results}
			{#each results as result}
				<SuggestedCard poi={result} />
			{/each}
		{:catch error}
			<p class="text-accent">{error.message}</p>
		{/await}
	{/if}
</div>
