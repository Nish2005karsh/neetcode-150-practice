def jump(nums):
    """
    Determine the minimum number of jumps required to reach the last index in the given list of non-negative integers.

    Args:
        nums (List[int]): A list of non-negative integers representing the maximum jump length at each position.

    Returns:
        int: The minimum number of jumps required to reach the last index.

    Constraints:
        - 1 <= len(nums) <= 1000
        - 0 <= nums[i] <= 10^5

    Example:
        >>> jump([2, 3, 1, 1, 4])
        2
        >>> jump([2, 3, 0, 1, 4])
        2
    """
    n = len(nums)
    if n <= 1:
        return 0

    max_reach = nums[0]
    steps = nums[0]
    jumps = 1

    for i in range(1, n - 1):
        max_reach = max(max_reach, i + nums[i])
        steps -= 1

        if steps == 0:
            jumps += 1
            steps = max_reach - i

    return jump
