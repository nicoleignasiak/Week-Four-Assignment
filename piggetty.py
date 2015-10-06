# Nicole Ignasiak
# Dr. Neumann
# CIS 125 82A
# 10/1/15
# In coloboration with Josiah Hardacre, Nathan Pugh, Trevor Waite, Cynthia, and Rebekah

# Open the file *getty.txt* for reading.  
gettyfile = open("getty.txt", "r")

# Open a new file *piggy.txt* for writing.  
piggyfile = open("piggy.txt", "w")

# Read the getty.txt file into a string.  
address = gettyfile.read()

# Strip out bad characters (, - .).  
address = address.replace(".", "")
address = address.replace("-", "")
address = address.replace(",", "")

# Define a function called piggy(string) that returns a string
def piggy():

# Split the string into a list of words.  
	listaddress = address.split()

# Create a new empty string.  
	piggystring = ""
	
	vowels = "aeiouAEIOU"
	piggynewword = ""

# Loops through each word in the Gettysburg Address
	for word in listaddress:
# Checks the first letter in each word and changes the word into PigLatin appropriately
		if word[0] in vowels:
			piggynewword = (word + "yay")
# Add the pigified word (and a space) to the new string.  	
			piggystring = piggystring + " " + piggynewword
		else:
			n=0
# Finds the first vowel and then changes word to PigLatin
			for letter in word:
				if letter in vowels:
					piggynewword = (word[n:] + word[0:n] + "ay")
# Add the pigified word (and a space) to the new string.  
					piggystring = piggystring + " " + piggynewword
					break
				n+=1
	return piggystring
	
# Calls the fuction piggy()
finalpiggystring = piggy()

# Write the new string to piggy.txt.  
piggyfile.write(finalpiggystring)

# close the files.
piggyfile.close()
gettyfile.close()