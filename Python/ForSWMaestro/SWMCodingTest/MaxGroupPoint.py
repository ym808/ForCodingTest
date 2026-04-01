points = [1,3,6,5,4]
points.sort()
n = len(points)

required_groups = n // 3

def can_form_groups(max_dist):
    i = 0
    count = 0

    while i <= n - 3:
        if points[i+2] - points[i] <= max_dist:
            i += 3
            count += 1
        else:
            i += 1
        
    return count == required_groups

start = 0
end = points[-1] - points[0]
optimal_dist = end

while start <= end:
    mid = (start + end) // 2

    if can_form_groups(mid):
        end = mid - 1
        optimal_dist = mid
    else:
        start = mid + 1
    
print(optimal_dist)