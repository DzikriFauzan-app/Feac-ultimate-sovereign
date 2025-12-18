/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        'sov-bg': '#0a0f14',
        'sov-card': '#111821',
        'sov-emerald': '#10b981',
        'sov-gold': '#d4af37',
        'sov-border': '#1e293b'
      }
    },
  },
  plugins: [],
}
