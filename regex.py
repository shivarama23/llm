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

pattern = r'(?<=[_\s-])\d+([_\s-]\d+)+(?=[_\s-]|$)|(?<=[_\s])\d+(?=[_\s])'

import re

pattern = r'(?<=[_\s-])\d+(?:[_\s-]\d+)+(?![_\s-])|(?<=[_\s])\d+(?=[_\s])'

for text in inputs:
    matches = re.findall(pattern, text)
    if matches:
        print(matches)

import re

def is_valid_date_format(date_str):
    # Define the regex pattern for YYYY/MM/DD format
    pattern = r'^\d{4}/\d{2}/\d{2}$'
    # Use re.match to check if the string matches the pattern
    if re.match(pattern, date_str):
        return True
    else:
        return False

# Test the function
test_dates = ["2024/06/18", "2024/6/18", "24/06/18", "2024-06-18", "20240618"]
results = {date: is_valid_date_format(date) for date in test_dates}
results
