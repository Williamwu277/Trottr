<script lang="ts">
	import type Poi from "$lib/models/poi.model";
    import { Restaurant } from "~icons/material-symbols/restaurant-rounded";
    import { Activity } from "~icons/material-symbols/local-activity-rounded";
    export let poi: Poi;
</script>

<div class="bg-sub rounded-[19px] w-[347px] h-[94px] px-4 py-8 text-accent flex items-center">
    {#if poi.category === "food"}
        <Restaurant class="w-[30px] h-[30px]"/>
    {:else}
        <Activity class="w-[30px] h-[30px]" />
    {/if}
    <div class="flex flex-col gap-1">

    </div>
</div>