def merge_sort(a):
    if len(a) <= 1:
        return a, 0

    mid = len(a) // 2

    left, inv_left = merge_sort(a[:mid])
    right, inv_right = merge_sort(a[mid:])

    merged = []
    i = j = 0
    inv_count = inv_left + inv_right

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_count += len(left) - i
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, inv_count


n = int(input())
a = list(map(int, input().split()))

_, answer = merge_sort(a)
print(answer)