---
layout: post
title: Permutations   	
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
import java.util.ArrayList;
import java.util.List;
/**
 * Total Accepted: 149970
Total Submissions: 362282
Difficulty: Medium
Contributors: Admin
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
 * @author liujing
 *
 */
public class _46_Permutations {
	
	public List<List<Integer>> permute(int[] nums){
		
		if(nums == null || nums.length == 0) return null;
		
		List<List<Integer>> res = new ArrayList<List<Integer>>();
		solve(nums,new ArrayList<Integer>(), res);
		return res;
		
	}
	
	private void solve(int[] nums, List<Integer> used, List<List<Integer>> res){
		if(used.size() == nums.length){
			res.add(new ArrayList<Integer>(used));
			return;
		}
		for(int i = 0; i < nums.length; i++){
			if(!used.contains(nums[i])){
				used.add(nums[i]);
				solve(nums,used,res);
				used.remove(used.size()-1);
			}
		}
			
	}

	public static void main(String[] args) {
		_46_Permutations test = new _46_Permutations();
		int[] nums = {1,2,3};
		List<List<Integer>> res = test.permute(nums);
		for(List<Integer> l : res){
			System.out.println(l);
		}
	}

}
```
