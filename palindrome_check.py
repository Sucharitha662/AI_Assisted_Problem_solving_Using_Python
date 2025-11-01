
# Function to check if a string is a palindrome
def is_palindrome(s):
    # Remove spaces and convert to lowercase
    cleaned = ''.join(s.split()).lower()
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]


# Example usage
test_string = "A man a plan a canal Panama"
if is_palindrome(test_string):                      
    print(f'"{test_string}" is a palindrome.')
else:
    print(f'"{test_string}" is not a palindrome.')
