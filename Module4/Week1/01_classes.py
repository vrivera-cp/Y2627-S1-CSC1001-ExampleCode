class Cat:
    pass

x = Cat()
x.name = 'mosaic'
x.nicknames = ['mochi', 'momo']
x.age = 8
x.weight = 8.8


y = Cat()
y.name = 'Harvest'
y.sister = Cat()

y.sister.name = 'Pearl'

print(x)
print(x.name)

print(y)
print(y.name)

print(y.sister)
print(y.sister.name)

print(x is y)
