import type { PageServerLoad } from "./$types";
// import Recent from "$lib/models/recent.model";
// import Search from "$lib/models/search.model";

export const load: PageServerLoad = () => {
    return {
        recent: [],
        suggested: []
    };
}