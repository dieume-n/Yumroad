from flask_assets import Bundle

common_css = Bundle(
    "https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css",
    "css/styles.css",
    filter="cssmin",
    output="css/app.css",
)

common_js = Bundle(
    "https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.7.3/dist/alpine.min.js",
    filter="jsmin",
    output="js/app.js",
)
