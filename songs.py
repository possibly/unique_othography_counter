import os
song_dir = os.getcwd()+'/songs/'
songs = {}
for filename in os.listdir(song_dir):
  f = open(song_dir+filename, "r")
  songs[filename] = str(f.read())