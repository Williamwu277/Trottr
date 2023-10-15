import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async () => {
	const res = await fetch('localhost:5000/distance', {
		method: 'GET',
	});

	const json = await res.json();
	const loc = JSON.parse(json);

	return {
		locations: loc
	};
};
