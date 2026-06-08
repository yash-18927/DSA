import sys

def can_place_cows(stalls: list[int], num_cows: int, min_dist: int) -> bool:
    count = 1
    last_placed_position = stalls[0]
    
    for i in range(1, len(stalls)):
        if stalls[i] - last_placed_position >= min_dist:
            count += 1
            last_placed_position = stalls[i]
            if count >= num_cows:
                return True
    return False

def get_max_min_distance(stalls: list[int], num_cows: int) -> int:
    stalls.sort()
    low = 1
    high = stalls[-1] - stalls[0]
    ans = 0
    
    while low <= high:
        mid = (low + high) // 2
        if can_place_cows(stalls, num_cows, mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return ans

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    t = int(input_data[0])
    idx = 1
    
    for _ in range(t):
        if idx >= len(input_data):
            break
        n = int(input_data[idx])
        c = int(input_data[idx + 1])
        idx += 2
        
        stalls = []
        for _ in range(n):
            stalls.append(int(input_data[idx]))
            idx += 1
            
        print(get_max_min_distance(stalls, c))

if __name__ == "__main__":
    main()
