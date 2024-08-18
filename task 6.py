def substring_between_indices(s, start, end):

    if start < 0:
        start = 0
    if start > len(s):
        start = len(s)
    
  
    if end < 0:
        end = 0
    if end > len(s):
        end = len(s)
    

    return s[start:end]
print(substring_between_indices("hello world", 2, 5))  # Output: "llo"
print(substring_between_indices("hello world", -3, 5))  # Output: "hello"
print(substring_between_indices("hello world", 2, 50))  # Output: "llo world"
print(substring_between_indices("hello world", 5, 2))  # Output: ""
