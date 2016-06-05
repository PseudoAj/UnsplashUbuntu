#!/usr/bin/env python

#use package to scrape the image
import wget
import os
import Tkinter as tk
import time
import threading
import urllib2

#some headers
__author__ = "Ajay Krishna Teja Kavuri"
__email__ = "ajaykrishnateja@gmail.com"

#The main class that initiates the url and screen parameters
class UnsplashUbuntu(object):

	def __init__(self, interval):
		try:
			print "Initializing"
			self.baseUrl = "https://source.unsplash.com/random"
			self.myScreen = tk.Tk()
			self.screen_width = self.myScreen.winfo_screenwidth()
			self.screen_height = self.myScreen.winfo_screenheight()
			self.res = "/"+str(self.screen_width)+"x"+str(self.screen_height)
			self.cwd = os.getcwd()
			self.filename=str(self.screen_width)+"x"+str(self.screen_height)
			self.interval = interval
			wpThread = threading.Thread(target=self.run)
			wpThread.daemon = True
			wpThread.setName('UnsplashUbuntu')
			wpThread.start()
			wpThread.join()

		except:
			print "Exception"

	#Obtain the baserurl and concat the string
	def getWallpaper(self):
		try:
			self.fullUrl = self.baseUrl + self.res
			self.filename = wget.download(self.fullUrl)
		except:
			print "Exception"

	#Run the command to change the wallpaper
	def setWallpaper(self):
		try:
			self.setCmd = "gsettings set org.gnome.desktop.background picture-uri file:///"+self.cwd+"/"+self.filename
			os.system(self.setCmd)
		except:
			print "Exception"

	#Remove the previous wallpaper before setting/downloading new one
	def removeWallpaper(self):
		self.filePath = self.cwd+"/"+self.filename
		if os.path.exists(self.filePath):
			os.remove(self.filePath)

	#Check for the internet connection
	def chkNetwork(self):
		try:
			res=urllib2.urlopen('http://wvu.edu',timeout=1)
			return True
		except urllib2.URLError as err:
			pass
		return False

	#The main logic implementation
	def run(self):
		while True:
			try:
				if self.chkNetwork():
					print("Daemon Running....")
					self.removeWallpaper()
					self.getWallpaper()
					self.setWallpaper()
					time.sleep(self.interval)
				else:
					time.sleep(self.interval/60)
			except:
				print "Exception"

#Initialize and call the class
thisWallpaper = UnsplashUbuntu(3600)
