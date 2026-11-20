a = {'primary': 'red', 'secondary': 'green', 'tertiary': 'blue'}
b = input('Enter a type: ')
print(a.get(b))
c = input('Enter a type to update: ')
d = input('Enter the new color: ')
a.update({c: d})
print(a)