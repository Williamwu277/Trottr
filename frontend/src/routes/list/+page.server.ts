import { getLocations } from '$lib/db';
import type Poi from '$lib/models/poi.model';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async () => {
	let locations: Poi[] = getLocations();
	const mappedData = locations.map((l) => [l.lat, l.lng]);

	const res = await fetch('localhost/distance', {
		method: 'GET',
		body: JSON.stringify({ locations: mappedData })
	});

    const json = await res.json();
    locations = JSON.parse(json);

	return {
		locations: locations
	};
};
