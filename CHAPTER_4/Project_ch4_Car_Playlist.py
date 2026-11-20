song = ["Running Up that hill", "Que Sera Sera", "The Sound of Silence",]
b = input("Enter the name you want to add to the playlist: ")
e = song.sort()
song.append(b)
d = song.pop(0)
print("The playlist is: " + str(song))