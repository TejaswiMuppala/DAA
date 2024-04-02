def reverse_string(s):
    # Base case: if the string is empty or has only one character, return itself
    if len(s) <= 1:
        return s
    # Recursive case: return the last character of the string concatenated with
    # the reverse of the string excluding the last character
    return s[-1] + reverse_string(s[:-1])

# Test the function
input_string = input("Enter a string: ")
reversed_string = reverse_string(input_string)
print("The reverse of '{}' is: {}".format(input_string, reversed_string))
