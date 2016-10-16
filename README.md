Website for Oakton High School Computer Science Club(OCS)

Information

[![Join the chat at https://gitter.im/OCS-Website/Lobby](https://badges.gitter.im/OCS-Website/Lobby.svg)](https://gitter.im/OCS-Website/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Dependencies

![](https://img.shields.io/badge/jQuery-v3.1.1-blue.svg) ![](https://img.shields.io/badge/Bootstrap-3.3.7-blue.svg) ![](https://img.shields.io/badge/font--awesome-4.6.3-blue.svg) ![](https://img.shields.io/badge/bootstrap--notify-3.1.3-blue.svg)

![](https://img.shields.io/badge/html5shiv-3.7.0-lightgray.svg) ![](https://img.shields.io/badge/Respond-1.4.2-lightgray.svg)

# Guideline

> GHP: GitHub Pages

## Important Notice

### Do
Load **All** external resources(*css, js, etc...*) that are using `https`, or GHP will block them

### Don't
Use files hosted on GitHub. They'll only be loaded as plain text

Use `.php` instead of `.html`, but GHP will not display the file correctly

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

# License
[dGRAMOP Development](https://github.com/BrainyBrian/dgramop): [Creative Commons 4.0](https://creativecommons.org/licenses/by/4.0/)
