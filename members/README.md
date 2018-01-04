# The auto-website-from-issue bot is UNSTABLE, PERIODICALLY OFFLINE, and is STILL MISSING CRITICAL FEATURES. Continue at own risk!

# Oakton Computer Science Club Member Pages
This is @dgramop's sad attempt to revive the practice of "public home directories"

## Background
Ok so let's go way back to "mainframes" and when people shared the same server/computer to do stuff. Way back then each user got their own folder. Home directories in unix (```~```) are usually stored for all users (except root) at the /home folder. And basically the sysadmin would put up a webserver and everybody would like create files in a special folder of their home directory marked public served ```/~<username>``` .
  
## Ok cool. I'm leaving
Colleges and workplaces *will* google you. And you kinda don't have direct control of what they see, so putting up your own little page is enough for you to write all sorts of crap that they'll take at face value.

## But I can't code
Alright I'm not kidding you you can literally know HTML tags and write like a half-decent web page that kinda works
  - `<br/>` - break, goes to the next line (like hitting enter)
  - `<hr/>` - draws a vertical line
  - `<b>*bold stuff*</b>` to make things bold
  - `<i>_italic stuff_</i>` to make things italic
  - `<a href="https://google.com">Search the web with G00gle</a>` create a link.
There are plenty of tutorials online. Pages can be really simple, they don't have to look fancy or anything. It's a great place to document your work, maybe create some sort of brag sheet, or a page that links people to stuff that you do/did. Creating your own page makes you look a lot better than using Wix, it eliminates any of the BS ads that they push into your site, and it allows people to focus on what's important. The design on Wix and most web builders often _distracts_ from the point you're trying to get across.

## Ok cool I have a few minutes let's start
Alright, cool, so first, you need a github account. Ideally have it include your first name and last name in some sense (like dgramop for Dhruv Gramopadhye). Note that accounts are public.
### Make a GitHub account
Follow this tutorial here: https://help.github.com/articles/signing-up-for-a-new-github-account/ , then come back
### Create an issue
Alright so go and cause some problems. Just kidding, here's how you really create an Issue:
  - Go to our github repo
  - Click "Issues"
  - Click the green button that says "New issue"
  - In the box that says "title", just throw in a title that says "request to create site"
  - In the textarea where it says "Leave a comment" type up stuff that you want people to know before you create the site (optional).
  - Go ahead and paste the following inside that same textarea:
  ```
  Hi! I'm <first name> <lastname>
  ==== web request ====
  {
  "name":"<firstname> <lastname>",
  "aliases":["<nickname>","<nickname>","<nickname>"],
  "template":"<template name>"
  }
  ==== end web request ====
  ```
  - Replace <firstname> with your firstname
  - Replace <lastname> with your lastname
  - Replace <nickname> with your nickname, and get rid of all the nicknames if you only have one
  - If you have no nicknames, make sure the line with ```"aliases"``` on it looks like ```"aliases":[],"```. It's a simple list, so make sure that the last string (a string is a set of characters/words/phrases/spaces enclosed by quotes) does NOT have a comma after it, the first string doesn't have a comma before it. All the strings have to be enclosed by []. Think of it like a box that stores all your nicknames, or like drawing a sideways shopping list
  - Click "Create issue"
  - Click "<> Code"
  - Click "members"
  - Click on your profile name
  - Those are the files to your site!
  - Your site is now live at https://oakcsclub.win/members/<your username>
  - Remember to replace <your username> with... your username!

## Rules:
  - Be a decent person
  - Don't be mean to other people
  - No NSFW
  - No links or other references to NSFW (a reference is something like an image that you call up from somewhere else `<img src="nsfwstuff"/>`, not "that's what she said", though remember, colleges can (and will) google you.
  - Only create the site or start a page if you want to. Understand that all the stuff you write is public, and webcrawlers can archive your content (like web.archive.org)
  - School Rules apply (pretty much)
  - (pending rule) - all pages must contain a visible link for reporting abuse. Although this rule is pending, bare in mind that we may add this link to your site at any time
  - Have fun, write blogs blah blah blah. "In darkness, democracy dies". 
Break the rules, and you're site will be taken down. 
