<script lang="ts">
	import Search from '~icons/material-symbols/search-rounded';
	import ArrowBack from '~icons/material-symbols/arrow-back-ios-rounded';

	export let text: string;

</script>

<div
	class="drop-shadow-lg w-[332px] bg-accent h-[51px] rounded-[28px] py-3 px-5 focus-within:bg-accent text-light focus-within:text-light flex justify-between items-center transition-all"
>
	<a href="/">
		<ArrowBack class="w-[30px] h-[30px] block" />
	</a>
	<input
		type="text"
		placeholder="Search"
		bind:value={text}
		class="font-bold focus:font-normal outline-none placeholder:text-light bg-transparent focus:placeholder:text-light text-[20px] w-[224px]"
	/>
	<Search class="w-[32px] h-[32px] block"/>
</div>
