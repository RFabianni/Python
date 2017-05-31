"""
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
 Once 'done' is entered, print out the largest and smallest of the numbers.
 If the user enters anything other than a valid number catch it with a
 try/except and put out an appropriate message and ignore the number.
 Enter the numbers from the book for problem 5.1 and Match the desired output as shown. """
largest = float('-inf') # Always smaller than any number
smallest = float('inf') # Always larger than any number
while True:
    num = raw_input("Enter a number: ")        
    if num == "done" : break
    if len(num) < 1 : break        
    try :
        num = int(num)
    except :    
        print "Invalid input"
        continue
    # set largest and smallest
    # initial inf forces first entry to reset the value
    largest = max(largest, num)
    smallest = min(smallest, num)
    # Because None is always smaller than any integer

print "Maximum is", largest
print "Minimum is", smallest