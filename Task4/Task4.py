import sys

def min_moves(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    return sum(abs(num - median) for num in nums)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        nums = list(map(int, f.readlines()))
    print(min_moves(nums))
