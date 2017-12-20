---
layout: post
title: Convert Sorted Array to Binary Search Tree
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
import java.util.Arrays;

/**
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
 *
 */
public class _108_ConvertSortedArrayToBST {
	
	/*
	 * 首先考虑使用递归的方法，将中间的结点作为根结点，然后递归地创建左子树和右子树
	 * 
	 * 移位去处>>比加号+的优先级低，一开始没有加nums.length>>1的括号，导致无限递归，堆栈溢出
	 */
    public static TreeNode sortedArrayToBST(int[] nums) {
    	
        if(nums == null || nums.length == 0) return null;
        
        if(nums.length == 1) return new TreeNode(nums[0]);
        
        TreeNode root = new TreeNode(nums[nums.length >> 1]);
        root.left = sortedArrayToBST(Arrays.copyOfRange(nums, 0, nums.length>>1));
        root.right = sortedArrayToBST(Arrays.copyOfRange(nums, (nums.length>>1) + 1, nums.length));
        
        return root;
    }
    
    /*
     * 上面这种方法，虽然也方便，但是每一次拷贝数组也是一次不小的开销。
     * 这里考虑始终只使用nums一个数组，而每次递归使用不同的start和end指针。
     */
    public static TreeNode sortedArrayToBST1(int[] nums) {
    		if(nums == null || nums.length == 0) return null;
    		
    		return helper(nums,0,nums.length-1);
    }
    
    public static TreeNode helper(int[] nums, int s, int e) {
    		if(e < s) 
    			return null;
    		int mid = (s + e) >> 1;
    		TreeNode root = new TreeNode(nums[mid]);
    		root.left = helper(nums, s, mid - 1);
    		root.right = helper(nums, mid + 1, e);
    		return root;
    }

	public static void main(String[] args) {
		sortedArrayToBST(new int[] {-10,-3,0,5,9});
	}

}
```
