"""Convert decimal number to binary (str) and binary number to decimal (str)"""


def decimal_to_binary(num):
    """Take number and return the str of its binary"""

    binary = ''

    while num != 0:

        remainder =  num % 2
        num = num // 2

        binary = str(remainder) + binary

    return binary


print(decimal_to_binary(122))
print(decimal_to_binary(5))
print(decimal_to_binary(160))


def binary_to_decimal(binary):
    """Take the binary str and return dec value of the binary number"""

    dec_value = 0
    base = 0

    for i in range(-1, -1 * len(binary) - 1, -1):

        if binary[i] == "1":
            dec_value += 2 ** base

        base += 1

    return dec_value


print(binary_to_decimal('111'))
print(binary_to_decimal('101'))
print(binary_to_decimal('0101111'))
print(binary_to_decimal('101100101'))

