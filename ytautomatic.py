from pytube import YouTube

"""

Created by: Yan Brasiliano Silva Penalva
Objective: Download automatic videos youtube.

"""

print()
print('Author: Yan Brasiliano Silva Penalva - hiyan')
print()

# user typed #
link = input("Enter the video link:  ")
path = input("Enter the directory that the video will be saved:  ")
yt = YouTube(link)

# details#
print(f"Title: {yt.title}.")
print(f"Number of vies: {yt.views}.")
print(f"Video duration {yt.length} seconds.")
print(f"Rating: {yt.rating}.")

# best resolution
ys = yt.streams.get_highest_resolution()

# download #
print("Download in progress ...")
ys.download(path)
print("Download completed.\nCheck your repository and enjoying the video.")