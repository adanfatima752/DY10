def replace_term_in_string(s, search_term, replacement_term):

    modified_string = s.replace(search_term, replacement_term)
    return modified_string

result = replace_term_in_string("hello world, hello universe", "hello", "hi")
print(result)  # Output: "hi world, hi universe"
