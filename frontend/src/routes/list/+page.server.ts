import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async () => {
	const res = await fetch('http://localhost:5000/h', {
		method: 'POST',
	});

	const json = await res.json();
	const loc = JSON.parse(json);

	return {
		locations: loc
	};
};
