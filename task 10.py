import re

def clean_whitespace(s):
    stripped_string = s.strip()
    cleaned_string = re.sub(r'\s+', ' ', stripped_string)
    
    return cleaned_string
result = clean_whitespace("  Hello   world! This   is   a   test.  ")
print(result)  # Output: "Hello world! This is a test."
