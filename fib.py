
def fib(n):
    if n == 1:
        return 1
    if n==2:
        return 1
    return fib(n-1)+fib(n-2)

def main():
    number = int(input("what number shall we use for fibonacci:"))
    result = fib(number)
    print(f"fibonacci of {number} is {result}")

main()