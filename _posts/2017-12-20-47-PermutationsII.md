---
layout: post
title: Permutations II   	
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
/**
 * Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
 * @author liujing
 *
 */
public class _47_PermutationsII {
	
	public List<List<Integer>> permuteUnique(int[] nums){
		if(nums == null || nums.length == 0) return null;
		
		List<List<Integer>> res = new ArrayList<List<Integer>>();
		Arrays.sort(nums);
		boolean[] flag = new boolean[nums.length];
		solve(nums,new ArrayList<Integer>(),flag,res);
		return res;
	}
	
	private void solve(int[] nums, List<Integer> used, boolean[] flag, List<List<Integer>> res){
		if(used.size() == nums.length){
			res.add(new ArrayList<Integer>(used));
			return;
		}
		for(int i = 0; i < nums.length; i++){
			if(flag[i] || i > 0 && nums[i] == nums[i-1] && !flag[i-1]) continue;
			if(!flag[i]){
				used.add(nums[i]);
				flag[i] = true;
				solve(nums,used,flag,res);
				used.remove(used.size()-1);
				flag[i] = false;
			}
		}
	}

	public static void main(String[] args) {
		_47_PermutationsII test = new _47_PermutationsII();
		int[] nums = {1,1,2};
		List<List<Integer>> res = test.permuteUnique(nums);
		for(List<Integer> l : res){
			System.out.println(l);
		}
	}

}
```
