---
layout: post
title: Merge Sorted Array   	
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
import java.util.Arrays;

/**
 * Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) 
to hold additional elements from nums2. The number of elements initialized in 
nums1 and nums2 are m and n respectively. 
 *
 */
public class _88_MergeSortedArray {
	
	public static void merge(int[] nums1, int m, int[] nums2, int n){
		
		if(n == 0) return;
		
		if(m == 0) {
			for(int i = 0; i < n; i++)
				nums1[i] = nums2[i];
			return;
		}
		
		int[] tmp = Arrays.copyOf(nums1, m);
		
		int count = 0, i = 0, j = 0;
		while(i < m && j < n){
			if(tmp[i] < nums2[j])
				nums1[count++] = tmp[i++];
			else
				nums1[count++] = nums2[j++];
		}
		
		while(i < m) nums1[count++] = tmp[i++];
		while(j < n) nums1[count++] = nums2[j++];
			
	}
	
	public static void merge1(int[] nums1, int m, int[] nums2, int n){
		int i = m-1, j = n-1, k = m+n-1;
		while(i >= 0 && j >= 0) nums1[k--] = (nums1[i] > nums2[j]) ? nums1[i--] : nums2[j--];
		while(j >= 0) nums1[k--] = nums2[j--];
	}

	public static void main(String[] args) {
		int[] nums1 = new int[6];
		nums1[0]=1; nums1[1]=3; nums1[2]=5;
		int[] nums2 = {2,4,6};
		merge(nums1, 3, nums2, 3);
		System.out.println(Arrays.toString(nums1));
	}

}
```
