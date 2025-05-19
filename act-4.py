x=frozenset([50,90,80])
y=frozenset([50,70,80])

print(x.isdisjoint(y))
print(x.difference(y))
print(x|y)