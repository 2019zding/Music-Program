class Music:

	def __init__(self):
		self.artists = [ ]

	# Pushing information to the array

	def display(self):
		print()
		print ("Here is the list of artists: ")
		for artists in self.artists:
			print (artists)

	def add (self, artists):
		self.artists.append(artists)

	def delete (self, artists):
		a = [ ]
		if self.artists == a
			print (‘ERROR SHUTDOWN’)
			return false
		else:
			self.artists.remove(artists)
			print "Artists : ", self.artists

	def compare (self,artists):
		quit ()




# for testing call your class and methods
music = Music(['BoA', 'Younha', 'BTS'])

while True:
	print("Enter 1 to display the list of artists")
	print("Enter 2 to add artists")
	print("Enter 3 to delete artists")
	print("Enter 4 to compare")
	print("Enter 5 to quit")
	userChoice = int(input())
	if userChoice is 1:
	    music.display()
	elif userChoice is 2:
		music.add()
	elif userChoice is 3:
		music.delete()
	elif userChoice is 4:
		music.compare()
	elif userChoice is 5:
		quit()
