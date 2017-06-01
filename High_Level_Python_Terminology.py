#Iterators

s = 'PRATIK'
it = iter(s)
print it.next()
print it.next()
print it.next()
print it.next()
print it.next()
print it.next()

#Generators
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

print reverse('FOOTBALL').next()
print reverse('FOOTBALL').next()
print reverse('FOOTBALL').next()

#Generator Expressions

print sum(i*i for i in range(4))

xvec = [10, 20, 30]
yvec = [7, 5, 3]
print sum(x*y for x,y in zip(xvec, yvec))

data = 'golf'
print list(data[i] for i in range(len(data)-1,-1,-1))