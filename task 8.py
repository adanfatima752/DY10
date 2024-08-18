def transform_string_cases(s):

    return {
        "lowercase": s.lower(),
        "uppercase": s.upper(),
        "titlecase": s.title()
    }
result = transform_string_cases("hello world")
print(result)
# Output: {'lowercase': 'hello world', 'uppercase': 'HELLO WORLD', 'titlecase': 'Hello World'}
