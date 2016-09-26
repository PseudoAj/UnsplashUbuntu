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
			#self.baseUrl = "https://source.unsplash.com/category/objects"
			self.baseUrl = "https://source.unsplash.com/random"
			self.myScreen = tk.Tk()
			#self.screen_width = self.myScreen.winfo_screenwidth()
			self.screen_width = 1920
			#self.screen_height = self.myScreen.winfo_screenheight()
			self.screen_height = 1920
			self.res = "/"+str(self.screen_width)+"x"+str(self.screen_height)
			self.cwd = os.getcwd()
			self.filename=str(self.screen_width)+"x"+str(self.screen_height)
			self.interval = interval
			self.fileExt = ".jpg"
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

	# Apply filter with primitive
	def applyPrimitive(self):
		try:
			self.filtrCmd="primitive -i "+self.filePath+" -o "+self.filePath+self.fileExt+" -s "+str(self.screen_width)+" -n "+str(self.screen_width)
			print("Executing \t"+str(self.filtrCmd))
			os.system(self.filtrCmd)
		except:
			print "Exception"


	#Run the command to change the wallpaper
	def setWallpaper(self):
		try:
			self.setCmd = "gsettings set org.gnome.desktop.background picture-uri file:///"+self.cwd+"/"+self.filename+self.fileExt
			os.system(self.setCmd)
		except:
			print "Exception"

	#Remove the previous wallpaper before setting/downloading new one
	def removeWallpaper(self):
		self.filePath = self.cwd+"/"+self.filename
		self.filtFilePath = self.cwd+"/"+self.filename+self.fileExt
		if os.path.exists(self.filePath):
			os.remove(self.filePath)
		if os.path.exists(self.filtFilePath):
			os.remove(self.filtFilePath)

	#Check for the internet connection
	def chkNetwork(self):
		try:
			res=urllib2.urlopen('http://google.com',timeout=1)
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
					self.applyPrimitive()
					self.setWallpaper()
					time.sleep(self.interval)
				else:
					time.sleep(self.interval/60)
			except:
				print "Exception"

#Initialize and call the class
thisWallpaper = UnsplashUbuntu(1800)
