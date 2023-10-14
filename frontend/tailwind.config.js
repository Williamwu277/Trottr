/** @type {import('tailwindcss').Config} */
export default {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		extend: {
      fontFamily: {
        sans: "Ubuntu"
      },
      colors: {
        accent: "#F774B3",
        sub: "#F8EFF3",
        light: "#FFFFFF"
      }
    }
	},
	plugins: []
};
