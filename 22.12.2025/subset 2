class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
     //STEPS-->  sort, recurssion(include,exclude), store, skip duplicate,choose current element, baktrack
     List<List<Integer>> result = new ArrayList<>();
     Arrays.sort(nums); // 1- sorting the ArrayList
     backtrack(result,new ArrayList<>(), nums,0);
     return result;   
    }
    private void backtrack(List <List<Integer>> result,List<Integer> tempList,int[] nums,int start){
        result.add(new ArrayList<>(tempList));
        for(int i=start;i<nums.length;i++){
            //3-skip dupliate
            if(i>start && nums[i]== nums[i-1]) continue;
            // 4- choose current element
            tempList.add(nums[i]);
            // 5- explore further subsets-including this elements
            backtrack(result,tempList,nums,i+1);// recurssion
            //6-->backtrack-remove the last element before next iteration

            tempList.remove(tempList.size()-1);

        }
    }
}
