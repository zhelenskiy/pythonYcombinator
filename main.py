y = lambda pred, then, next, other: lambda arg: (lambda x: x(pred, then, next, other)(arg)(x))(lambda pred, then, next, other: lambda arg: (lambda _: other) if not pred(arg) else (lambda x: then(arg, x(pred, then, next, other)(next(arg))(x))))
factorial = y(pred=lambda x: x > 0, then=lambda cur, got: cur * got, next=lambda x: x - 1, other=1)
fibanacci = y(pred=lambda x: x > 0, then=lambda _, pair: (pair[1], pair[0] + pair[1]), next=lambda x: x - 1, other=(0, 1))
for n in range(10):
    print(n, "->", factorial(n))
print()
for n in range(10):
    print(n, "->", fibanacci(n)[0])
