# Unsplash Ubuntu

![logo](./logo/logo.png)

## Why did I make this?

I am a big fan of the serious opensource communities. One such photo sharing portal is [unsplash.com](https://unsplash.com). Also, I always wanted to make some cool Ubuntu utility. So one fine day I thought "Okay, why not achieve both". This project is result of that. This is by no means a complex project(yet).

## What does it do?
A simple utility written in python that picks a high resolution random image from [unsplash.com](https://unsplash.com) and puts it as your wallpaper; updates it every hour with a new wallpaper.    

## Cool, how can I install?
1. Clone and download the [repository](https://github.com/PseudoAj/UnsplashUbuntu)
1. Install the dependencies:
 1. wget
 1. Tkinter
 1. urllib2

1. Open terminal and change directory:
  1. `cd UnsplashUbuntu`
  1. add permissions: `chmod +x unsplashubuntu.py`
  1. Run the program: `./unsplashubuntu.py`

1. (optional) Add the program on startup by going into launcher->startup applications

## Demo:
![demo](http://i.giphy.com/3oEjHWvmcRT2rzahWM.gif)

## Features:
1. Lightweight process
2. Supports multiple monitors
3. Intelligent, checks for network before attempting

## To-do
1. Add topics filtering
1. Multiple platform support, move to electron?
