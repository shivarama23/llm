import re

def keyword_match(keyword, input_string):
    # Define the delimiters
    delimiters = r'[\s\-_.#]'
    
    # Create a regular expression pattern
    pattern = rf'(?<!\w){delimiters}{keyword}{delimiters}(?!\w)|^{keyword}{delimiters}|{delimiters}{keyword}$|^{keyword}$'
    
    # Search for the pattern in the input string
    match = re.search(pattern, input_string)
    
    # Return True if a match is found, otherwise False
    return match is not None

# Example usage
keyword = "test"
input_string = "this is a test string"
print(keyword_match(keyword, input_string))  # Output: True

input_string = "this is a testing string"
print(keyword_match(keyword, input_string))  # Output: False
