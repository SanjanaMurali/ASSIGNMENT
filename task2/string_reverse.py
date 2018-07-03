# python program to reverse words in a string

# function to reverse words
def reverse_words_in_string(string):
# for identifying end of string
	string += "\0"
# loop to split string to words and reverse it
# stores reversed words in list reversed_words
	temporary_word=""
	reversed_words=[]
	for i in string:
		if i==" " or i=="\0":
			reversed_words.append(temporary_word)
			temporary_word=""
		else:
			temporary_word = i+temporary_word
	output_string=''
# loop for concatenation
	for element in reversed_words:
		output_string=output_string+element+" "
			
	
	print output_string
string=raw_input("Enter the string\n")	
# function call	
reverse_words_in_string(string)
