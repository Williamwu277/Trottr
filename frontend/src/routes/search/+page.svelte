<script lang="ts">
	import SearchBar from '$lib/components/NewSearchBar.svelte';
	import type { PageServerData } from './$types';

	let poiName: string;
</script>

<div class="w-screen pt-4 px-8">
	<div class="mt-8 flex flex-col items-center">
		<SearchBar bind:text={poiName} />
	</div>
	<h2 class="uppercase mt-6 text-accent font-bold text-[18px]">Suggested</h2>
	<div class="flex flex-col items-center gap-[15px]">

	</div>
</div>
