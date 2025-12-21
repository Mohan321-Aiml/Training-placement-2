import java.util.*;
class Solution {
    public void inorder(TreeNode root,HashSet<Integer> nums)
    {
        if(root == null)
            return;
        inorder(root.left,nums);
        nums.add(root.val);
        inorder(root.right,nums);
    }
    public int findSecondMinimumValue(TreeNode root) {
        HashSet<Integer> nums = new HashSet<>();
        inorder(root,nums);
        ArrayList<Integer> list = new ArrayList<>(nums);
        Collections.sort(list);
        if(list.size()<2)
            return -1;
        else
            return list.get(1);
    }
}
