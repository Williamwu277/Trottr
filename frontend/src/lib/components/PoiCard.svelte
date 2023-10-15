<script lang="ts">
	export let name: string;
	export let time: string;
</script>

<div class="bg-sub rounded-[19px] h-[65px] w-[347px]">
	<div class="bg-sub text-accent py-3 px-5 flex justify-between">
		<div>
			<h2 class="text-[20px] font-bold text-ellipsis">{name}</h2>
			<h3 class="text-[20px]">{time}</h3>
		</div>
	</div>
</div>
