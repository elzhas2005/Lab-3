x=float(input())
def fun(y):
    y = (5/9)*(y-32)
    t=1
    if y%1==0 :
        y = int(y)
        print(int(y))
        t = 0
    if t==1 :
        print(round(y,5))
fun(x)