def is_palindrome(s):
    # Base case: if the string is empty or has only one character, it's a palindrome
    if len(s) <= 1:
        return True
    # Recursive case: check if the first and last characters are the same,
    # then recursively check the substring excluding the first and last characters
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

# Take user input for the string
user_input = input("Enter a string to check if it's a palindrome: ")

# Remove whitespace and convert to lowercase for case-insensitive comparison
user_input = user_input.replace(" ", "").lower()

# Check if the input string is a palindrome
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")
