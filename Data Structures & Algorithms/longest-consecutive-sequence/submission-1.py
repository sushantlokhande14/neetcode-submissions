class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0  # No elements, so no sequence possible

    # -------------------------------
    # Step 2: Create a HashSet of nums
        # -------------------------------
        num_set = set(nums)  # O(n) time and space
        max_length = 0  # Tracks the longest sequence found

        # -------------------------------
        # Step 3: Check each number if it's the start of a sequence
        # -------------------------------
        for num in num_set:
            # Only try to build a sequence if `num - 1` isn't in the set
            # This ensures we start at the beginning of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1  # At least this one number is in the sequence

                # -------------------------------
                # Step 4: Count the streak length
                # -------------------------------
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # Update max_length if we found a longer streak
                max_length = max(max_length, current_streak)

        # -------------------------------
        # Step 5: Return the result
        # -------------------------------
        return max_length