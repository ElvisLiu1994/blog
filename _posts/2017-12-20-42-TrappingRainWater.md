---
layout: post
title: Trapping Rain Water  
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
/**
 * Given n non-negative integers representing an elevation map where the width 
 * of each bar is 1, compute how much water it is able to trap after raining.
 * For example, Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
 * @author liujing
 *
 */
public class _42_TrappingRainWater {
	/**
	 * Here is my idea: instead of calculating area by height*width, 
	 * we can think it in a cumulative way. In other words, 
	 * sum water amount of each bin(width=1).
		Search from left to right and maintain a max height of left 
		and right separately, which is like a one-side wall of partial container. 
		Fix the higher one and flow water from the lower part. 
		For example, if current height of left is lower, 
		we fill water in the left bin. Until left meets right, 
		we filled the whole container.
	 * @param height
	 * @return
	 */
	public int trap(int[] height){
		int left = 0, right = height.length-1;
		int res = 0;
		int maxLeft = 0, maxRight = 0;
		while(left <= right){
			if(height[left] < height[right]){
				if(height[left] > maxLeft) maxLeft = height[left];
				else res += maxLeft-height[left];
				left++;
			}else{
				if(height[right] > maxRight) maxRight = height[right];
				else res += maxRight-height[right];
				right--;
			}
		}
		return res;
	}
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
```
