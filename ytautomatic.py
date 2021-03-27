from pytube import YouTube

""" 
File name:	 ytautomatic.py               
Author:	     YAN BRASILIANO SILVA PENALVA     	            
Email: 				yanpenabr@gmail.com
---------------------------------------------------------------------
Date created:  				xxxxxxxx
Date last modified: 	26 MAR 2021
Python Version:				3.5
License: 							GPL License
Maintainer: 					YAN BRASILIANO SILVA PENALVA
Version: 							1.0
---------------------------------------------------------------------
Description:  
PT-BR: Este script tem como função baixar vídeos do youtube.
EN-US: This script has the function of downloading videos from youtube. 

"""
# user typed 
link = input("Enter the video link:  ")
path = input("Enter the directory that the video will be saved:  ")
yt = YouTube(link)

# details 
print(f"Title: {yt.title}.")
print(f"Number of vies: {yt.views}.")
print(f"Video duration {yt.length} seconds.")
print(f"Rating: {yt.rating}.")

# best resolution
ys = yt.streams.get_highest_resolution()

# download 
print("Download in progress ...")
ys.download(path)
print("Download completed.\nCheck your repository and enjoying the video.")