def find_missing_number(arr: list, n: int) -> int:
    x1 = arr[0]
    x2 = 1
    for i in range(1, len(arr)):
        x1 ^= arr[i]
    for i in range(2, n + 1):
        x2 ^= i
    return x1 ^ x2
