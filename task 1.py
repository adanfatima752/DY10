def concatenate_and_convert(str1, str2):
    result = str1 + str2
    
    if result.isdigit():
        # Convert the string to an integer
        return int(result)
    else:
        # Return the concatenated string as is
        return result
print(concatenate_and_convert("123", "456"))  # Output: 123456 (as an integer)
print(concatenate_and_convert("123", "abc"))  # Output: "123abc" (as a string)
