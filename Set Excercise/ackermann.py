#Ackermann's Function


#Start

#%%

def memoize(f):
    memo = {}
    def helper(m,n):
        if x not in memo:            
            memo[m,n] = f(m,n)
        return memo[m,n]
    return helper

#@memoize
def ackermann(m,n):
     if m == 0:
          return (n + 1)
     elif n == 0:
          return ackermann(m - 1, 1)
     else:
          return ackermann(m - 1, ackermann(m, n - 1))

ackermann = memoize(ackermann)

x=int(input("What is the value for m? "))
print(x)

y=int(input("What is the value for n? "))
print(y)

print("\nThe result of your inputs according to the Ackermann Function is:" )
print(ackermann(x, y)) 


# %%


