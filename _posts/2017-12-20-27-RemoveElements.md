---
layout: post
title: Remove Element  
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
/**
 * Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
 * @author liujing
 *
 */
public class _27_RemoveElements {
	
	public int removeElement(int[] nums, int val){
		if(nums == null) return 0;
		
		int index = 0;
		for(int i = 0; i < nums.length; i++){
			if(nums[i] != val){
				nums[index++] = nums[i];
			}
		}
		return index;
	}
	
	public int removeElement1(int[] nums, int val){
	    int i = 0;
	    int n = nums.length;
	    while (i < n) {
	        if (nums[i] == val) {
	            nums[i] = nums[n - 1];
	            // reduce array size by one
	            n--;
	        } else {
	            i++;
	        }
	    }
	    return n;
	}

	public static void main(String[] args) {
		_27_RemoveElements test = new _27_RemoveElements();
		int[] nums = {3,2,2,3};
		System.out.println(test.removeElement(nums, 3));
	}

}
```
