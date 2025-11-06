In Python, a set is an unordered collection of unique elements. This means: [1, 2]  

• Unordered: Elements in a set do not have a defined order, and their position cannot be accessed using an index. 
• Unique: A set automatically eliminates duplicate elements; each element can appear only once. 
• Mutable: You can add or remove elements from a set after it's created. 
• Immutable Elements Only: The elements within a set must be immutable (e.g., numbers, strings, tuples). Lists or other sets cannot be direct elements of a set. [3]  

Creating Sets: 
Using curly braces {}. 
    my_set = {1, 2, 3, 4, 2, 3}
    print(my_set) # Output: {1, 2, 3, 4} (duplicates are removed)

Using the set() constructor. 
    my_list = [1, 2, 3, 4, 2, 3]
    my_set = set(my_list)
    print(my_set) # Output: {1, 2, 3, 4}

To create an empty set, you must use set(), not {} (which creates an empty dictionary). 
    empty_set = set()
    print(empty_set) # Output: set()

Common Set Operations and Methods: 

• Adding elements: 
	• add(element): Adds a single element. 
	• update(iterable): Adds multiple elements from an iterable (like a list or another set). 

• Removing elements: 
	• discard(element): Removes an element if present, does nothing if not found. 
	• remove(element): Removes an element, raises a KeyError if not found. 
	• pop(): Removes and returns an arbitrary element, raises KeyError if the set is empty. 
	• clear(): Removes all elements from the set. 

• Mathematical Set Operations: 
	• Union: set1 | set2 or set1.union(set2) (returns a new set with all unique elements from both sets). 
	• Intersection: set1 & set2 or set1.intersection(set2) (returns a new set with common elements). 
	• Difference: set1 - set2 or set1.difference(set2) (returns a new set with elements in set1 but not in set2). 
	• Symmetric Difference: set1 ^ set2 or set1.symmetric_difference(set2) (returns a new set with elements in either set, but not in both). 

• Other useful methods: 
	• isdisjoint(other_set): Returns True if two sets have no common elements. 
	• issubset(other_set): Returns True if all elements of the current set are in other_set. 
	• issuperset(other_set): Returns True if all elements of other_set are in the current set. 

AI responses may include mistakes.

[1] https://hyperskill.org/university/python/set-and-set-in-python
[2] https://www.tutorialspoint.com/python/python_sets.htm
[3] https://www.geeksforgeeks.org/python/python-set-function/

