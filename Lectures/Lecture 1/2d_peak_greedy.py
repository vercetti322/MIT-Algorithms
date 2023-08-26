def find_peak_greedy(matrix):
    '''
    Find the 2-D peak element in a matrix using the greedy approach, assuming it exists.

    Args:
        matrix (List[List[int]]): A 2D list denoting a matrix.

    Returns:
        int: The peak element in the matrix.

    Algorithm:
        Start at matrix[0][0] and keep moving until a bigger number is found.
        When movement is not possible, the destination is the peak element.
    '''
    i = 0  # row index
    j = 0  # column index

    while i < len(matrix) and j < len(matrix[0]):
        if j < len(matrix[0]) - 1 and matrix[i][j] < matrix[i][j + 1]:
            j += 1
        elif i < len(matrix) - 1 and matrix[i][j] < matrix[i + 1][j]:
            i += 1
        elif i > 0 and matrix[i][j] < matrix[i - 1][j]:
            i -= 1
        elif j > 0 and matrix[i][j] < matrix[i][j - 1]:
            j -= 1
        else:
            return matrix[i][j]

    return -1


def main():
    '''
    Example usage of the find_peak_greedy function with a sample matrix.
    '''
    matrix = [[14, 13, 12], [15, 9, 11], [16, 17, 19]]
    print(find_peak_greedy(matrix))


if __name__ == '__main__':
    main()
