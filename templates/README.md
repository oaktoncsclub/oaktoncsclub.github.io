# Templates for Web Request

## Creating a template
A template is a one-pager HTML file. The bot I wrote currently does not support multi-page templates, that might be for a later release

It's a two-step process:
 - Create a pull request with <templatename>.html
 - Create a pull request to this README file so your template is listed

### Dynamic (ish) variables
 - Dynamic variables are parts of the config file that are auto-filled in your template. If you decide to "create" a template variable, just make sure that you make a pull request to the instructions README.md at /members .
 - For example:
   ${username} -> replaced with username
   ${uid} -> replaced with GitHub user ID. Note that this will never change, although usernames can change on github
   ${name} -> name of the user
 - Things are parsed strictly:
   ```${name}``` works
   ```${ name }``` doesn't
   - But that means that having $ signs and curly braces can be weird so be careful. If you have a need to put in curly braces or dollar signs, use HTML escape code (google em)

## Templates:
Format: filename; template name; description; author
 - retro.html; retro, a simple, bare-bones page; dgramop
