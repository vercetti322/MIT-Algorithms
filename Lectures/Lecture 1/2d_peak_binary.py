# Find the peak of a 2D matrix using columnar binary search
# Complexity : O(nlogm) if m is number of columns

def find_peak_binary(matrix, col_start, col_end):
    '''
    Input -> 2d array, start of column, end of column
    Output -> peak element (assuming it exists)
    
    Algorithm:
    
    Look at the j = m / 2 column, find the max of the column (i, j):
        if (i, j - 1) > (i, j):
            repeat in cols[1...i - 1]
        else if (i, j + 1) > (i, j):
            repeat in cols[i + 1....n]
        else:
            return (i, j)
    '''
    mid_col = (col_end - col_start) // 2
    
    max_value = -1
    for i in range(1, len(matrix)):
        if matrix[i][mid_col] > max_value:
            max_value = matrix[i][mid_col]
            max_col = i
     
    if matrix[max_col][mid_col - 1] > matrix[max_col][mid_col]:
        return find_peak_binary(matrix, col_start, (max_col - 1))
    
    elif matrix[max_col][mid_col + 1] > matrix[max_col][mid_col]:
        return find_peak_binary(matrix, (max_col + 1), col_end)
    
    else:
        return matrix[max_col][mid_col]
    
def main():
    matrix = [[10, 8, 10, 10], [14, 13, 12, 11], [15, 9, 11, 21], [16, 17, 19, 20]]
    print(find_peak_binary(matrix, 0, 3))
    
    
if __name__ == '__main__':
    main()