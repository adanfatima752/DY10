def count_char_occurrences(s, char):
    count = 0
    
    for c in s:
        if c == char:
            count += 1
    return count

# Example usage
print(count_char_occurrences("hello world", 'l'))  # Output: 3
print(count_char_occurrences("hello world", 'o'))  # Output: 2
print(count_char_occurrences("hello world", 'x'))  # Output: 0
