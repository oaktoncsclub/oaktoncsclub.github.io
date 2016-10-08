Website for Oakton High School Computer Science Club(OCS)


![](https://img.shields.io/badge/jQuery-v3.1.1-blue.svg) ![](https://img.shields.io/badge/Bootstrap-3.3.7-blue.svg) ![](https://img.shields.io/badge/font--awesome-4.6.3-blue.svg) ![](https://img.shields.io/badge/bootstrap--notify-3.1.3-blue.svg)

![](https://img.shields.io/badge/html5shiv-3.7.0-lightgray.svg) ![](https://img.shields.io/badge/Respond-1.4.2-lightgray.svg)

# Guideline

> Use `.php` instead of `.html` in case of switching to PHP later

## Basic Structure
```HTML
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
	<!--Bootstrap-->
    <link rel="stylesheet" href="/css/style.css" />
    <link rel="icon" href="/img/favicon.png" type="image/png" />
  </head>

  <body>
    <nav class="navbar navbar-default navbar-fixed-top" id="navbar"></nav>
    <footer class="hidden-xs" id="footer"></footer>
	<!--jQuery-->
    <script src="/js/main.js" type="text/javascript"></script>
  </body>
</html>
```

## Style
- Indentation
	- HTML, PHP
		- 2 spaces
		- Indent and use a blank line to separate `<head>`, `<body>`
	- CSS, JS
		- 4 spaces
		
Using Atom IDE is reccomended
