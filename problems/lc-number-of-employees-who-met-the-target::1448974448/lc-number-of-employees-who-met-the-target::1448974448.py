class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        # return len(hours) % 2 == 0 and max(Counter(hours).values()) < target
        return len([i for i in range(len(hours)) if hours[i] >= target])