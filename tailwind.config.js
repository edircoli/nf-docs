/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/nf_docs/templates/**/*.html"],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: "#0DC09D",
          light: "#E6F9F5",
          dark: "#0A9A7D",
        },
      },
    },
  },
  plugins: [],
};
