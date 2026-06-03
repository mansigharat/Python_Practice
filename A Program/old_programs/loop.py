library = {
    'Book1': {'title': 'Clean Code', 'author': 'Robert Martin', 'pages': 431},
    'Book2': {'title': 'The Pragmatic Programmer', 'author': 'Hunt & Thomas', 'pages': 352},
}

print(library['Book1']['author'])

library['Book3'] = {'title': 'My Real Truth', 'author': 'Atharva', 'pages': 960}
print(library)