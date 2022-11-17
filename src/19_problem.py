def main():
    str = input('Ingrese una frase: ')
    array = str.split()
    dict_str = {str:len(str) for str in array }
    print(dict_str)

if __name__ == '__main__':
    main()