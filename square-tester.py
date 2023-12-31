# Marty McVry
# 2023-12-31

# Checking which numbers follow the rule stipulated in the video

# First, set starting number and ending number
intStart = 10
intEnd = 10000000

# We also print out this warning... You never know...
print("Warning: this program contains a loop.")
print("If you think it's taking too long, it can be stopped with CRTL+C.")

# We define a function to check an integer for its compliance to the stipulated rule
# Function followsRule(int intNumber) returns a boolean
def followsRule(intNumber):
    # Make number a string
    strNumber = str(intNumber)
    # The last digit is the remainder of a division by 10
    intLastDigit = intNumber % 10
    # The rest of the digits is the integer value of the first n-1 characters
    intFirstDigits = int(strNumber[:-1])
    # We make a string that concatenates the two multiplications
    strResult = "{0}{1}".format(intFirstDigits * (intFirstDigits + 1), intLastDigit ** 2)
    # And then check whether or not the result matches the expected output.
    if (strResult == str(intNumber ** 2)):
        return True
    else:
        return False

# Now, we open a file for appending
fh = open("succesful-squares.txt","a")

# And we start looping
for i in range(intStart, intEnd + 1):
    # Check if the number follows the rule
    if followsRule(i):
        # If so, write it to the file and start a new line
        fh.write("{0}\n".format(i))
    # Then we add one to the number and restart the loop!
    intStart += 1
