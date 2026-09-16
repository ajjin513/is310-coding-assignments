# Assignment 1: Inspecting the Cultural Web
By Hong Ju Jin

**Site inspected:** MoMA Museum(https://www.moma.org/collection/) <br>
**GitHub repository:** github.com/MuseumofModernArt/collection (https://github.com/MuseumofModernArt/collection)

## About the site

MoMA's online collection lets visitors browse, search, and filter almost
200,000 works of modern and contemporary art. Each artwork has its own page
with an image, title, date, medium, and other catalog information.

## Web technologies used on the website

- **HTML structure:** The page follows the standard structure we covered in
  class. It starts with `<!DOCTYPE html>`, followed by an `<html>` element
  containing a `<head>` and a `<body>`.

- **CSS:** Styling appears to be bundled together with the site's JavaScript
  into hashed/minified files. This is different from the simple `<style>`
  tag example we looked at in class. It suggests the site is built with a
  modern front-end framework that compiles CSS and JS together instead of
  keeping separate, readable files.

- **JavaScript:** JavaScript makes a lot of the interactivity in this website. The search bar, the filters for artwork type/date/theme, and buttons all behave
  dynamically without reloading the page.

- **An unfamiliar file/domain:** Several images on the page are served from
  `cdn.sanity.io`. This was new to me. I think It's the domain for Sanity, which is
  a content management service. This suggests that MoMA manages some of its
  content, like images for magazine articles and store products are through a
  separate content system.

## Who built this website?

- I couldn't find any developer or design credits directly on the website
  itself. There was no footer credit, and no "About this site" tech section.

- I found a 2015 blog post from MoMA's own Digital Media Department,
  "Mutant Materials and Video Spaces: 20 years of MoMA on the web," https://medium.com/digital-moma/mutant-materials-and-video-spaces-20-years-of-moma-on-the-web-27a29fd83375
  which explains that MoMA's web presence started in 1995 with two curators,
  Paola Antonelli and Barbara London.

- To dig further, I also looked for a GitHub repository, the same way we
  looked at the contributors' graph for whatisdigitalhumanities.com in
  class. I found:
  github.com/MuseumofModernArt/collection https://github.com/MuseumofModernArt/collection

  It is an official MoMA repository. It contains a public dataset of over
  160,000 catalog records for MoMA's collection, released under a public
  domain license.

# Assignment 2: Styling the Cultural Web
The file called `index.html` shows Vincent van Gogh's *The Starry Night* (1889)
from MoMA's collection. It shows metadata, description, image, link, sources, and little interaction with javascript.