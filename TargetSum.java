public class TargetSum {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
                    int addNumber = target - nums[i];
                    for (int j = 0; j < nums.length; j++) {
                        if (i != j && nums[j] == addNumber) {
                            return new int[] { i, j };
                        }
                    }
                }
                return new int[0]; // If no solution found (though the prompt says there always is one)
            }
        }