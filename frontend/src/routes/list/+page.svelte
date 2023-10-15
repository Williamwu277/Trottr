<script lang="ts">
	import type { PageServerData } from './$types';
	import PoiCard from '$lib/components/PoiCard.svelte';
	export let data: PageServerData;

	let width: number;
	let height: number;

	async function getLocation() {
		const gl = navigator.geolocation;
		return new Promise((resolve, reject) => {
			gl.getCurrentPosition(resolve, reject, { enableHighAccuracy: true });
		});
	}

	let loc: Promise<GeolocationPosition> = getLocation();
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
<div
	class="bg-light w-screen box-border bottom-0 left-0 rounded-t-[34px] flex flex-col items-center pt-5 pb-6 absolute"
>
	<div class="bg-sub rounded-full h-[6px] w-[245px] mb-4" />
	<div class="flex flex-col gap-[36px] mb-10 overflow-y-auto">
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
