# generate value on fly
def my_generator():
    for i in range(5):
        yield i # u will get generator
        
gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

for j in gen:
    print(j)