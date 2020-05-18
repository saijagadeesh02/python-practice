def gen(N):

    for i in range(N):
        yield i**2
for n in gen(4):
    print(n)