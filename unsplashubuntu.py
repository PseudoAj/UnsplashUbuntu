#!/usr/bin/env python

#use package to scrape the image
import wget
import os

#some headers
__author__ = "Ajay Krishna Teja Kavuri"
__copyright__ = "copyright 2016"
__email__ = "ajaykrishnateja@gmail.coms"

class UnsplashUbuntu(object):

	def __init__(self):
		self.baseUrl = "https://source.unsplash.com/random"
		self.res = "/1920x1080"
		self.cwd = os.getcwd()
		self.filename="1920x1080"
		
	def getWallpaper(self):
		self.fullUrl = self.baseUrl + self.res
		self.filename = wget.download(self.fullUrl)

	def setWallpaper(self):
		self.setCmd = "gsettings set org.gnome.desktop.background picture-uri file:///"+self.cwd+"/"+self.filename
		os.system(self.setCmd)

	
	def removeWallpaper(self):
		self.filePath = self.cwd+"/"+self.filename
		if os.path.exists(self.filePath):
			os.remove(self.filePath)

thisWallpaper = UnsplashUbuntu()
thisWallpaper.removeWallpaper()
thisWallpaper.getWallpaper()
thisWallpaper.setWallpaper()



		