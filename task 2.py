def char_at_index(s, index):
  
    if index < 0 or index >= len(s):
        return "Index out of bounds"
    else:
        return s[index]
print(char_at_index("hello", 1))  # Output: "e"
print(char_at_index("hello", 5))  # Output: "Index out of bounds"
print(char_at_index("hello", -1))  # Output: "Index out of bounds"
