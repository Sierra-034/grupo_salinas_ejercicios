def func(x):
    numerator = x**2 - 5*x + 6
    denominator = x**2 - 7*x + 12
    return (numerator/denominator)**2

def main():
    x = float(input('Ingrese el valor de x: '))
    result = func(x)
    print(result)

if __name__ == '__main__':
    main()