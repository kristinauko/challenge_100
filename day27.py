"""
This problem was asked by Amazon.

Implement run-length decoding. You can assume the string 
to be encoded have digits and alphabetic characters. 
You can assume the string to be decoded is valid.

The string "4A3B2C1D2A" would be decoded as "AAAABBBCCDAA".
"""

#I assume digits are less than 10

def decode(s):
    """Take string of numbers and letters and return string which consists of letters"""

    ints = "1234567890"

    numbers = ""
    letters = ""
    final_string = ""

    i = 0

    while i < len(s):
    
        if s[i] in ints:
            numbers += s[i]
              
        else:
            letters += s[i]

        i += 1

    for i, char in enumerate(numbers):

        final_string += int(char) * letters[i]

    return final_string
    

print(decode("4A3B2C1D2A"))
   


        