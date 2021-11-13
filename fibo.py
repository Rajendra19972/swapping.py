#fibo

def fibo(n):
    a,b = 0,1
    while (b<n):
        print(a)
        print(b)
        a = a+b
        b= b+a

fibo(100)
