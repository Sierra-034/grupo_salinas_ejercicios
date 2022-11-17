def diagonal_sum(matrix):
    # diagonal_list = [diag_elem = elem[index][index] for elem in  ]
    diagonal_list = []
    index = 0
    while index < len(matrix):  # Podría hacerse con list comprehension
        diagonal_list.append(matrix[index][index])
        index += 1
    
    sum = 0
    for elem in diagonal_list:  # Podría hacerse con foonctools.reduce()
        sum += elem

    return sum

def main():
    sum = diagonal_sum([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    print(sum)

if __name__ == '__main__':
    main()