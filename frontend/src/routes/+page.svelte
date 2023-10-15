<script lang="ts">
	import SearchBar from '$lib/components/HomeSearchBar.svelte';

	let width: number;
	let height: number;

	async function getLocation() {
		const gl = navigator.geolocation;
		return new Promise((resolve, reject) => {
			gl.getCurrentPosition(resolve, reject, { enableHighAccuracy: true });
		});
	}

	let loc: Promise<GeolocationPosition> = getLocation();

	loc
		.then((res) => {
			// initialize server with starting location.
			fetch('http://localhost:5000/init', {
				method: 'POST',
				body: JSON.stringify({
					lat: res.coords.latitude,
					long: res.coords.longitude
				})
			});
		})
		.catch((err) => console.log(err.message));

	function generate() {
		fetch('http://localhost:5000/add', {
			method: 'POST'
		});
	}
</script>

<svelte:window bind:innerWidth={width} bind:innerHeight={height} />
{#await loc}
	<div class="w-screen h-screen bg-light" />
{:then loc}
	<iframe
		title="Map"
		{width}
		height={height - 194}
		style="border:0"
		class="slide-up"
		loading="lazy"
		allowfullscreen
		referrerpolicy="no-referrer-when-downgrade"
		src="https://www.google.com/maps/embed/v1/place?key=AIzaSyD3N1Mn6mI9_TQD-1ftS2HPKC-1duMMb7I&q={loc
			.coords.latitude}%2C{loc.coords.longitude}&zoom=14"
	/>
{:catch err}
	<iframe
		title="Map"
		{width}
		height={height - 194}
		style="border:0"
		class="slide-up"
		loading="lazy"
		allowfullscreen
		referrerpolicy="no-referrer-when-downgrade"
		src="https://www.google.com/maps/embed/v1/view?key=AIzaSyD3N1Mn6mI9_TQD-1ftS2HPKC-1duMMb7I&center={43.786800409248144}%2C{-79.18969364191958}&zoom=14"
	/>
{/await}

<div class="flex flex-col items-center absolute top-12 left-0 w-screen">
	<a href="/search">
		<SearchBar />
	</a>
</div>
<div
	class="bg-light w-screen box-border h-[194px] absolute bottom-0 left-0 rounded-t-[34px] p-4 flex flex-col gap-[15px] slide-up"
>
	<a
		class="rounded-[19px] font-bold bg-accent text-light w-full text-[24px] h-[75px] flex justify-center items-center"
		href="/list"
		on:click={generate}>Be a Trotter</a
	>
	<a
		class="rounded-[19px] bg-sub text-accent w-full text-[18px] h-[51px] flex justify-center items-center"
		href="/search">Create your own journey</a
	>
</div>
