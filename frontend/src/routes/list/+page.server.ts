import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async () => {
	const res = await fetch('http://localhost:5420/h', {
		method: 'POST',
		mode: 'cors',
		headers: {
			'Content-Type':'application/json'
		}
	});

	const loc = await res.json();
	//const loc = JSON.parse(json).get('res');
	console.log(loc['res'])

	return {
		locations: loc['res']
	};
};
