word_input = input("Please enter a word.")
python_file = open("PythonSummary.txt", "r")
file_string = python_file.read()
file_string_lowercased = file_string.lower()
print(file_string_lowercased.count(word_input))