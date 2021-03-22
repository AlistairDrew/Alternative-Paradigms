# Ackermann's Function


# Start

# %%

def memoize(f):
    memo = {}

    def helper(x, y):
        if str(x)+','+str(y) not in memo:
            memo[str(x)+','+str(y)] = f(x, y)
        return memo[str(x)+','+str(y)]
    return helper


def ackermann(m, n):
    if m == 0:
        return (n + 1)
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


# The ackermann function is now decorated by the memoize function.
ackermann = memoize(ackermann)

# Asking for first argument of the ackermann function
x = int(input("What is the value for m? "))
print(x)

# Asking for second arugment of ackermann function
y = int(input("What is the value for n? "))
print(y)

print("\nThe result of your inputs according to the Ackermann Function is:")
print(ackermann(x, y))


# %%


# %%
