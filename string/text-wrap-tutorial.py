import textwrap

long_text = "This is a very long string that needs to be wrapped into multiple lines to fit within a specific width for better readability."

# Using fill() to wrap and return a single string
wrapped_text = textwrap.fill(long_text, width=30)
print("Wrapped text using fill():")
print(wrapped_text)

# Using wrap() to get a list of lines
wrapped_lines = textwrap.wrap(long_text, width=30)
print("\nWrapped lines using wrap():")
for line in wrapped_lines:
    print(line)