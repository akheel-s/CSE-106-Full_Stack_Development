sentence = input("Please enter the sentence you want repeated.")
repeat = int(input("Please enter the number of times you want the sentence repeated."))
y = 0
with open('CompletedPunishment.txt', 'w') as x:
    while y < repeat:
        x.write(sentence + '\n')
        y += 1