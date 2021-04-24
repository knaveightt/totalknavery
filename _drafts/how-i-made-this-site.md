---
layout: post
author: knaveightt
title: How I Made This Site
category: Web Development
tags: [commentary, jekyll, totalknavery]
---
Well, this is my first post to this website! Not only that, this is my first foray into using the jekyll static site generator. What intrigued me about this set of tools, was really being able to seperate my layouts from content, have the ability to do some things data-driven, and ultimately manage a blog without the need of any backend data base technology. Serving this website as static pages is a plus too, as these pages should load pretty quickly! Add the fact that github has built-in jeckyll support for their github pages hosting, this was definitely a win to setup the new TotalKnavery website!

This is not my first personal webspace I've setup for myself, but that's some history for a differnet post :)

What I wanted to write about in this case, is just some of the things I was able to perform and take advantage of for this website using jekyll, as it truly has been an awesome expereince so far. This website is broken up into three sections essentially: Projects, Music, and Blog. For each section, I was able to take advantage of a particular capability of jekyll that drives how that section work. Just to dive right in and talk about Blog for a moment, jekyll really does excel at being able to manage blogs and blog posts with just a set of text files. Without going into how jekyll works specifically (maybe I'll do a seperate post on that in the future), one thing that I wanted to be able to do with this blog is to maintain a tag cloud and catagories page that relates my posts together. You'd think, how could i do this with a static site generater? Well, the key is Liquid my friends. There are som neat tips and tricks in being able to generate tag clouds just using this markup language. I'll have to do even another post on how I got the tag cloud setup (building on some work done by others in this space), but let's just say I was able to automate some of the manual process even further by writing a pythong script to generaete tag pages for me - all in all jekyll gives me the ability to manage my blog simply and efficiently. 


