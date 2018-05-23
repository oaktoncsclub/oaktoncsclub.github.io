# Oakton Computer Science Club

Information

[![Join the chat at gitter.im/oaktoncsclub/public](https://badges.gitter.im/OCS-Website/Lobby.svg)](https://gitter.im/oaktoncsclub/public)

Dependencies

![](https://img.shields.io/badge/jQuery-v3.1.1-blue.svg) ![](https://img.shields.io/badge/Bootstrap-3.3.7-blue.svg) ![](https://img.shields.io/badge/font--awesome-4.6.3-blue.svg) ![](https://img.shields.io/badge/bootstrap--notify-3.1.3-blue.svg)

![](https://img.shields.io/badge/html5shiv-3.7.0-lightgray.svg) ![](https://img.shields.io/badge/Respond-1.4.2-lightgray.svg)

## Welcome!
This is the repository for our website!

Websites are written in a "language" called HTML. HTML is a form of XML, which is a type of Markup Language.
HTML pages tell browsers how to show text to users

Our website supports 2 languages:
 - HTML/JS/CSS - if it can be done in a browser, you can do it with these langauges. Not easy to master, but super-duper powerful
 - Markdown - Super-duper easy to master, this README file is written in Markdown (you can tell beacuse of the .md file extention)
 
In order to give users a consistent experience across our website, we require everything that is officially Oakton CS Club to be HTML/JS/CSS or a PDF. You can read more about those guidlines below.
**The exception to this rule is for sites under the /members and /templates directories - part of our "lame attempt to revive home-directory culture"**

## Term Definition

> GHP: GitHub Pages

## Important Notice

### Do
Load **ALL** external resources(*css, js, etc...*) that are using `https`, or GHP (or the user's browser) will block them

### Don't
Use files hosted on GitHub. They'll only be loaded as plain text because GHP doesn't seem to send Content-Type headers. We are looking for a way to mess with _config.yml to change that
Use `.php` or any server-side dynamic scripting instead of `.html`, but GHP will not display the file correctly. Exception is templates for member pages with auto-refill attributes

## Basic Page Structure
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

## Analytics:
[Simple Analytics](http://dgramop.xyz/analytics/viewer.php?uid=oakcsclub.win)
Analytics running on some really old php that was written around 4 years ago, should work fine
