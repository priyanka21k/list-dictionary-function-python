"""
Q.7 Take a String input from user and
find frequency of each character such that
frequency will be stored in dictionary.
The character will be key and the frequency will be value
"""
# initializing string
test_str = "REGexSoftwareServices"

# using naive method to get count
# of each element in string
all_freq = {}

for i in test_str:
	if i in all_freq:
		all_freq[i] += 1
	else:
		all_freq[i] = 1

# printing result
print ("Count of all characters in REGexSoftwareServices is :\n " + str(all_freq))
