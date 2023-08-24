# Calculate 2-D peak of a matrix by using greedy approach assuming it exists
# Complexity : O(mn)

def find_peak_greedy(matrix):
    '''
    Input -> a 2D list of lists denoting a matrix
    Output -> the peak element
    
    Algorithm:
    
    Start at matrix[0][0] and keep on moving till u find a bigger
    number, when u can't move any more u have found ur destination.
    '''
    i = 0 # row index
    j = 0 # column index
    
    while i < len(matrix) and j < len(matrix[0]):
        if j < len(matrix[0]) - 1 and (matrix[i][j] < matrix[i][j + 1]):
            j += 1
        
        elif  i < len(matrix) - 1 and matrix[i][j] < matrix[i + 1][j]:
            i += 1
            
        elif i > 0  and matrix[i][j] < matrix[i - 1][j]:
            i -= 1

        elif j > 0 and matrix[i][j] < matrix[i][j - 1]:
            j -= 1
            
        else:
            return matrix[i][j]
        
    return -1

def main():
    matrix = [[14, 13, 12], [15, 9, 11], [16, 17, 19]]
    print(find_peak_greedy(matrix))
    

if __name__ == '__main__':
    main()