"""
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. 
The basic idea is to represent repeated successive characters as a 
single count and character. For example, the string "AAAABBBCCDAA" 
would be encoded as "4A3B2C1D2A".

Implement run-length encoding. You can assume the string 
to be encoded have no digits and consists solely of alphabetic characters. 
You can assume the string to be decoded is valid.
"""


def encode(s):
    """Take a string and encode it that the amount of symbols would be 
    represented by integer and the symbol"""

    encoded = ""
    counter = 1
    last_seen = s[0]

    for i in range(1, len(s)):

        if last_seen == s[i]:
            counter += 1
         
        else:
            encoded += str(counter) + last_seen
            counter = 0
            last_seen = s[i]
            counter += 1

    #append last last_seen to encoded
    encoded += str(counter) + last_seen

    return encoded


print(encode("AAAABBBCCDAA")) #4A3B2C1D2A
print(encode("AAAABBBCCDAABDAAAA")) #4A3B2C1D2A1B1D4A
print(encode("AAAABBBCCDAABDAAAAC")) #4A3B2C1D2A1B1D4AC
