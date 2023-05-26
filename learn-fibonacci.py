# rumus fibonaci f(n) = 0 
# f(1) = 1
# jika n tidak sama dengan 0 atau 1
# maka f(n) = (n -1) + (n -2 )

def fibonacci(n):
    # Jika n = 0 atau n = 1 maka return n
    if n == 0 or n == 1:
        return n
    
    # jika tidak maka masukkan kedalam rumus method fibonaci
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    n = int(input("Enter the number of terms: "))
    print("The first {} Fibonacci numbers are:".format(n))
    for i in range(n):
        print(fibonacci(i))


if __name__ == "__main__":
    main()
