def merge_sort(arr):
    global ans
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    left_index = right_index = 0
    new_list = []

    while left_index < len(left) and right_index < len(right) :
        if left[left_index] < right[right_index]:
            new_list.append(left[left_index])
            left_index += 1
        else :
            new_list.append(right[right_index])
            right_index += 1
    new_list += left[left_index:]
    new_list += right[right_index:]
    if left[-1] > right[-1]:
        ans += 1
    return new_list
t = int(input())
for tc in range(1, t+1):
    ans = 0
    n = int(input())
    lst = list(map(int,input().split()))
    ans_lst = merge_sort(lst)
    print(f'#{tc} {ans_lst[n//2]} {ans}')