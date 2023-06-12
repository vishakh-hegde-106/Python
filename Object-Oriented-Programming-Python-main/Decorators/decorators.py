import time

def timeit(func):
    def timed(*args,**kw):
        print("before")
        ts=time.time()
        result= func(*args,**kw)
        te=time.time()
        minutes,seconds=divmod((te-ts),60)
        print(minutes,seconds)
        print("time taken %8.2f"%((te-ts)*10**6))
        print("after")
        return result
    return timed
@timeit
def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
num=int(input("enter the number for fibo"))
f=fib()

for x in range(num):
    print(next(f))
        