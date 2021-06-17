def show_artists(artists):
    for artist in artists: # Loop over the artists.
       name, songs = artist # Unpack name and songs.
       print(name)
       for song in songs: # Loop over the songs.
             print(" ", song)

 # Create a list of artists.
performers = [
["Weird Al", ["Like a Surgeon", "Perform this Way"]],
["Lady Gaga", ["Bad Romance", "Born this Way"]],
 ["Madonna", ["Like a Virgin", "Papa Don’t Preach"]]]
print (show_artists(performers))

shoes = [["Manolo Blahnik", 120], ["Bontoni", 96],
 ["Maud Frizon", 210], ["Tinker Hatfield", 54],
["Lauren Jones", 88], ["Beatrix Ong", 150]]
for designer, price in shoes:
 print(designer, ": $", price, sep="")


# note there is a diff between this :

# xlist =ylist  this pass by reference as change for one change to other unless you didnt change the pointer of one of them
# xlist = ylist[:] here simply just copy the list


#another note

# lists are global variables like when u change in it inside a fun for ex it appear changed  out of the scope of this function
#which is good
