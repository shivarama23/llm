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


def extract_pattern(text):
    # Regular expression patterns
    pattern_hyphen = r"(?:(?<=^)|(?<=[-]))\d+[-\s_]\d+(?:(?=$)|(?=[-.]))"
    pattern_underscore = r"(?:(?<=^)|(?<=[_]))\d+[-\s_]\d+(?:(?=$)|(?=[_.]))"
    pattern_space = r"(?:(?<=^)|(?<=[\s]))\d+[-\s_]\d+(?:(?=$)|(?=[\s.]))"

    # Finding matches
    match_hyphen = re.search(pattern_hyphen, text)
    match_underscore = re.search(pattern_underscore, text)
    match_space = re.search(pattern_space, text)

    # Extracting the matched patterns
    output_hyphen = match_hyphen.group() if match_hyphen else None
    output_underscore = match_underscore.group() if match_underscore else None
    output_space = match_space.group() if match_space else None

    # combine outputs of all three patterns and return the first match

    if output_underscore:
        return output_underscore
    elif output_hyphen:
        return output_hyphen
    elif output_space:
        return output_space
    else:
        return None


# Test the function
test_dates = ["2024/06/18", "2024/6/18", "24/06/18", "2024-06-18", "20240618"]
results = {date: is_valid_date_format(date) for date in test_dates}
results
