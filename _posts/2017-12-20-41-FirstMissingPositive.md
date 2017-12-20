---
layout: post
title: First Missing Positive  
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java

public class _41_FirstMissingPositive {
	
	public int firstMissingPositive(int[] nums){
		if(nums == null || nums.length == 0) return 1;
		
		for(int i = 0; i < nums.length; i++){
			while(nums[i]>0 && nums[i]<nums.length && nums[nums[i]-1] != nums[i]){
				int tmp = nums[i]; 
				nums[i] = nums[nums[i]-1]; 
				nums[tmp-1] = tmp;
			}
		}
		for(int i = 0; i < nums.length; i++){
			if(nums[i] != i+1)
				return i+1;
		}
		
		return nums.length+1;
	}

	public static void main(String[] args) {
		_41_FirstMissingPositive test = new _41_FirstMissingPositive();
		int[] nums = {3,4,-1,1};
		System.out.println(test.firstMissingPositive(nums));
	}

}
```
