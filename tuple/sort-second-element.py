def sort_second_element(students):
    sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
    return sorted_students

students = [("Alice", 88), ("Bob", 95), ("Charlie", 70)]
print(sort_second_element(students))
