class Music:

# if you pass in artists while calling your class
# you need to add it to init
	def __init__(self, name, artists):
		self.name = name
		self.artists = artists


	# Pushing information to the array

	def display(self):
		print()
		print ("Your artists:")
		for artists in self.artists:
			print (artists)

	def add (self):
		# gather user input here
		add_artist = input('What artist do you want to add?')
		self.artists.append(add_artist)
		print ("Your artists:")
		for artists in self.artists:
			print (artists)

	def delete (self):
		#Deletes the last artist last given
		self.artists.pop()
		print ("Your artists:")
		for artists in self.artists:
			print (artists)

# what are you comparing to?
# how do you get that info?
	def compare_array(self, friend):
		compare = [thing for thing in self.artists if thing in friend.artists]
		# add value of compare to artist_array
		print(compare)



# for testing call your class and methods
# name = Music(pass in arguments)
estelle = Music('Estelle', ['La la las', 'Car Seat Head Rest'])
				# name,		#artist array
ben = Music('Ben', ['La la las', 'Food'])

while True:
	print("Enter 1 to display the list of artists")
	print("Enter 2 to add artists")
	print("Enter 3 to delete artists")
	print("Enter 4 to compare")
	print("Enter 5 to quit")
	userChoice = int(input())
	if userChoice is 1:
	    estelle.display()
	elif userChoice is 2:
		estelle.add()
	elif userChoice is 3:
		estelle.delete()
	elif userChoice is 4:
		Music.compare_array(estelle, ben)
	elif userChoice is 5:
		quit()
