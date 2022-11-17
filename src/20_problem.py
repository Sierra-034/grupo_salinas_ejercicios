def fibo_gen(max: int):
    n1 = 0
    n2 = 1
    counter = 0

    while True:
        if counter == max:
            break

        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            counter += 1
            aux = n1 + n2
            n1, n2 = n2, aux
            yield aux

def main():
    n = int(input('Ingrese un número: '))
    fibonacci = fibo_gen(n)
    list_fibo = [elem for elem in fibonacci]
    print(list_fibo)

if __name__ == '__main__':
    main()