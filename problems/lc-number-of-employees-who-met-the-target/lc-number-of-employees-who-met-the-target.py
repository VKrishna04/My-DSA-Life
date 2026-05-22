class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return len([i for i in range(len(hours)) if hours[i] >= target])