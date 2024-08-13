def sub(x,y):
    return x-y

def total(a,b,callback):
    print(callback(a,b))
    
total(20,10,sub)

# callback is name not a function..
data=[13,34,56,14,26,9,86,44]

def add_num(n):
    return n+5

data=list(map(add_num,data))
print(data)


users=['ram','sita','hari','sophia','gp']
