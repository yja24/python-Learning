#default arguments
def bag(w1='giorgio ' ,w2=' armani'):
    merge=w1+w2
    print('Brand is-',merge)

bag('jack &',' jones')
bag('emporio')
bag()

#keyword arguments
def show(n1, n2):
    print("n1 is ", n1)
    print("n2 is ", n2)


show(10, 20)
show(n2=200, n1=100)

#variable argument
def multiply(*num):
    n1=1
    for i in num:
        n1=n1*i
    print('product is-',n1)

multiply(11,10)

def multiple(**yes):
    sum=0
    for i, j in yes.items():
        sum=sum+j
    print('sum is',sum)

multiple(n1=72,n2=69)
    