if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    index = 0
    max_number = None
    while index<n:
        if max_number<arr[index]:
            max_number = arr[index]
        index = index+1
    new_index = 0
    second_max = None
    while new_index<n:
        if max_number>arr[new_index] and second_max<arr[new_index]:
            second_max = arr[new_index]
        new_index = new_index+1
    print second_max
