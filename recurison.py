# RECURSION

# First part is function defination and within that function def we call the
# same function ( Function calling itself)

def factorial(x):
    if (x == 1):
        return 1
    else:
        return x*(factorial(x-1))

answer = factorial(5)
print(answer)
