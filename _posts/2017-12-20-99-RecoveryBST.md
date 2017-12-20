---
layout: post
title: Recover Binary Search Tree  
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
import java.util.LinkedList;

/**
 * Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
 */
public class _99_RecoveryBST {
	
	/**
	 * BST的中序遍历是有序的，所以只需要通过寻找中序遍历中需要被交换的两个数即可，比如：6 3 4 5 2，这里只需要将6和2交换后
	 * 即变为有序的了
	 */
	public static void recoverTree(TreeNode root) {
		
		LinkedList<TreeNode> stack = new LinkedList<TreeNode>();
		
		TreeNode first = null, second = null;
		
		TreeNode cur = root;
		TreeNode pre = null;
		while(cur != null || !stack.isEmpty()) {
			while(cur != null) {
				stack.push(cur);
				cur = cur.left;
			}
			cur = stack.pop();
			if(first == null && pre != null && pre.val >= cur.val) {
				first = pre;
			}
			if(first != null && pre != null && pre.val >= cur.val) {
				second = cur;
			}
			pre = cur;
			cur = cur.right;
		}
		
		int tmp = first.val;
		first.val = second.val;
		second.val = tmp;
		
	}
	
	/**
	 * 也可以用递归的方法
	 */
	static TreeNode first, second;
	static TreeNode pre;
	public static void recoverTree1(TreeNode root) {
		
		traverse(root);
		int tmp = first.val;
		first.val = second.val;
		second.val = tmp;
	}
	
	public static void traverse(TreeNode root) {
		if(root == null) return;
		
		traverse(root.left);
		
		if(first == null && pre != null && pre.val >= root.val) {
			first = pre;
		}
		if(first != null && pre != null && pre.val >= root.val) {
			second = root;
		}
		/**
		 * 注意，下面两个if语句中间一定不能加else，否则将会出现second为空的错误
		 * 比如，中序遍布为1，0时，遍历0时，满足第一个if，然后first被赋为1，如果此时加了else，则second不会被赋值而为空，后面将会抛出异常
		 */
		if(pre != null && pre.val >= root.val) {
			if(first == null) first = pre;
			if(first != null) second =root;
		}
		
		pre = root;
		
		traverse(root.right);
	}
	
	public static void main(String[] args) {
		TreeNode root = new TreeNode(new int[] {0,1});
		recoverTree(root);
	}

}
```
