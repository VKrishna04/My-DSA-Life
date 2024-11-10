class Solution {
    public boolean isPossibleToSplit(int[] nums) {
        Map<Integer, Integer> frequencyMap = new HashMap<>();

        // Count occurrences of each number
        for (int num : nums) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }

        // Check if any number has a frequency higher than 2
        for (int frequency : frequencyMap.values()) {
            if (frequency > 2) {
                return false;
            }
        }

        return true;
    }
}