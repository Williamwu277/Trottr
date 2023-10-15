import type Poi from "$lib/models/poi.model";
import type { PageServerLoad } from "./$types";

export const load: PageServerLoad = async () => {
    const locations: Poi[] = [
        {
            name: "mc donald",
            distance: "0.1",
            category: "food",
            address: "123 yonge st",
            location: "3294023 3294",
            time: "12:43 pm"
        },
        {
            name: "mc donald",
            distance: "0.1",
            category: "food",
            address: "123 yonge st",
            location: "3294023 3294",
            time: "12:43 pm"
        },
        {
            name: "mc donald",
            distance: "0.1",
            category: "food",
            address: "123 yonge st",
            location: "3294023 3294",
            time: "12:43 pm"
        },
    ]

    return {
        locations: locations
    };
}