import re

text = "Dog runs past the Cat"
pattern = r"Cat"

# re.match() Example
match_result = re.match(pattern, text)
if match_result:
    print(f"Match found by re.match(): {match_result.group()}")
else:
    print("re.match() found nothing.") # This will be the output

# re.search() Example
search_result = re.search(pattern, text)
if search_result:
    print(f"Match found by re.search(): {search_result.group()}") # This will be the output
else:
    print("re.search() found nothing.")
