import { getLocations } from '$lib/db';
import type Poi from '$lib/models/poi.model';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async () => {
	const locations: Poi[] = getLocations();
	const mappedData = locations.map((l) => [l.lat, l.lng]);

	const res = await fetch('localhost:5000/distance', {
		method: 'GET',
		body: JSON.stringify({ locations: mappedData })
	});

    const json = await res.json();
    const times: string[] = JSON.parse(json);

    for (let i = 0; i < locations.length; i++) {
        locations[i].time = times[i];
    }

	return {
		locations: locations
	};
};
