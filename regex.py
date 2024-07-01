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


______________________________________________________________________________
import re

def replace_first_date(input_string):
    # Regex pattern to match the entire date format
    full_pattern = r'_\d{2}/\d{2}/\d{4}_\d{2}[A-Za-z]{3}\d{4}'

    # Check if the input string matches the entire pattern
    if re.search(full_pattern, input_string):
        # Regex pattern to match the first date format
        first_date_pattern = r'_\d{2}/\d{2}/\d{4}_'
        
        # Replace the first matched date with a space
        output_string = re.sub(first_date_pattern, ' ', input_string, count=1)
        return output_string
    else:
        return input_string

# Example input string
input_string = "some_text_01/05/2022_01May2014"
output_string = replace_first_date(input_string)
print(output_string)
_______________________________________________________________________________

import re

def clean_string(input_string):
    # Define the regex pattern to match _alphanumeric_DDMMMYYYY format
    pattern = r'_[A-Z0-9-]{9,}_[0-3][0-9][A-Za-z]{3}[0-9]{4}$'
    
    # Check if the pattern is found
    if re.search(pattern, input_string):
        # Define the replacement pattern to only replace the alphanumeric part
        replacement_pattern = r'_([A-Z0-9-]{9,})_([0-3][0-9][A-Za-z]{3}[0-9]{4})'
        # Replace the alphanumeric part with a blank
        cleaned_string = re.sub(replacement_pattern, r' \2', input_string)
        return cleaned_string
    else:
        # Return the original string if the pattern is not found
        return input_string

# Test the function
test_string = "calibration certificate_2020061399_23May2024"
print(clean_string(test_string))  # Output should be "some-test__23May2024"

