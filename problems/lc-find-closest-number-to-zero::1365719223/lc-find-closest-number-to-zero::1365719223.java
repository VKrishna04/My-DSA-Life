import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int findClosestNumber(int[] nums) {
        ArrayList<Integer> negative_list = new ArrayList<Integer>();
        ArrayList<Integer> positive_list = new ArrayList<Integer>();

        for (Integer integer : nums) {
            if (integer < 0) {
                negative_list.add(integer);
            } else {
                positive_list.add(integer);
            }
        }

        Collections.sort(negative_list, Collections.reverseOrder());
        Collections.sort(positive_list);

        if (negative_list.isEmpty() && positive_list.isEmpty()) {
            return 0;
        }

        if (negative_list.isEmpty()) {
            return positive_list.get(0);
        }
        if (positive_list.isEmpty()) {
            return negative_list.get(0);
        }

        int closestNegative = negative_list.get(0);
        int closestPositive = positive_list.get(0);

        if (Math.abs(closestNegative) < closestPositive) {
            return closestNegative;
        } else {
            return closestPositive;
        }
    }
}