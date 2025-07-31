# Importing the pandas library to work with CSV files and dataframes
import pandas

# Reading the CSV file into a DataFrame
df = pandas.read_csv("nato_phonetic_alphabet.csv")

# Creating a dictionary where each letter maps to its phonetic code
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}

# Asking the user to input a word and converting it to uppercase
user_words = input("Enter a word: ").upper()

# Creating a list of phonetic codes corresponding to each letter in the input word
words_of_list = [nato_dict[word] for word in user_words]

# Printing the final list of phonetic codes
print(words_of_list)
