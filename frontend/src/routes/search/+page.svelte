<script lang="ts">
	import SearchBar from '$lib/components/NewSearchBar.svelte';

	let width: number;
	let height: number;

	async function getLocation() {
		const gl = navigator.geolocation;
		return new Promise((resolve, reject) => {
			gl.getCurrentPosition(resolve, reject, { enableHighAccuracy: true });
		});
	}

	let loc = getLocation();
</script>

<svelte:window bind:innerWidth={width} bind:innerHeight={height} />;
<div class="flex flex-col items-center absolute top-10 left-0 w-screen">
	<SearchBar />
</div>
