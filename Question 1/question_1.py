inputs = list(map(int, input("Input more than two numbers separated by spaces.").split()))
if len(inputs) < 2:
    print("Error: Did not enter more than two integers.")
else: 
    totalsum = 0
    for x in range(0, len(inputs)):
        totalsum += inputs[x]
    print("The sum is : " + totalsum)