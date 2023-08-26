# Find the peak (an element greater than it's neighbours) using binary search algorithm

def find_peak(array, start, end):
    """
    Input -> list of numbers, starting index, ending index
    Output -> peak element

    Algorithm:

    Check for n / 2 element,
    if a[n / 2 - 1] > a[n / 2]:
        search for a[1....n/2 - 1]
    else if a[n / 2 + 1] > a[n / 2]:
        search for a[n/2 + 1...n]
    else:
        return a[n / 2], n / 2
    """
    mid = (end - start) // 2

    if array[mid - 1] > array[mid]:
        return find_peak(array, 0, mid - 1)

    elif array[mid + 1] > array[mid]:
        return find_peak(array, mid + 1, mid)

    else:
        return array[mid]


def main():
    array = [6, 7, 4, 3, 2, 1, 4, 5]
    print(find_peak(array, 0, 7))


if __name__ == '__main__':
    main()
