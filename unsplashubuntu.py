#!/usr/bin/env python

#use package to scrape the image
import wget
import os

__author__ = "Ajay Krishna Teja Kavuri"
__copyright__ = "copyright 2016"
__email__ = "ajaykrishnateja@gmail.coms"

class UnsplashUbuntu(object):

	def __init__(self):
		self.baseUrl = "https://source.unsplash.com/random"
		self.res = "/1920x1080"
		
		
	def getWallpaper(self):
		self.fullUrl = self.baseUrl + self.res
		self.filename = wget.download(self.fullUrl)

	def setWallpaper(self):
		self.cwd = os.getcwd()
		self.setCmd = "gsettings set org.gnome.desktop.background picture-uri file:///"+self.cwd+"/"+self.filename
		os.system(self.setCmd)
	
	def removeWallpaper(self):
		self.filePath = self.cwd+"/"+self.filename
		os.remove(self.filePath)


thisWallpaper = UnsplashUbuntu()
thisWallpaper.getWallpaper()
thisWallpaper.setWallpaper()
thisWallpaper.removeWallpaper()

		