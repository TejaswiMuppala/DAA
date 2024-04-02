def string_to_int(string):
    # Base case: if the string is empty, return 0
    if len(string) == 0:
        return 0
    # Recursive case: convert the string excluding the last character to int,
    # and multiply it by 10 then add the last character converted to int
    return string_to_int(string[:-1]) * 10 + int(string[-1])

# Test the function
string = input("Enter a string of digits: ")
integer = string_to_int(string)
print("The integer representation of '{}' is: {:,}".format(string, integer))  # Formatting the output with commas for readability
