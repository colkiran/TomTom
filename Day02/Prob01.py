def fun(*args):
   print(*args)


fun()
fun(1)
fun(1, 2)
fun(1, 2, 3)
fun(1, 2, 3, 4, 5)
fun([1, 2, 3, 4])

print("-" * 60)
def fun1(**kwargs):
   print(kwargs)
   print(type(kwargs))


fun1(name='Sachin', age=32, runs=120, oppn='AUS', venue='PERTH')



def add(a, b, c):
    print(a + b + c)

add(c = 10, a = 20, b = 15)