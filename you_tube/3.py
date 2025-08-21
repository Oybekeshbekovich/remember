n,w,h=map(int,(input().split()))
def minimal_square_side(n, w, h):
    def can_fit(side):
        return (side // w) * (side // h) >= n
    left = 0
    right = max(w, h) * n
    answer = right
    while left <= right:
        mid = (left + right) // 2
        if can_fit(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
print(minimal_square_side(n, w, h))