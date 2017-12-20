---
layout: post
title: Maximum Depth of Binary Tree  
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
import java.util.LinkedList;
import java.util.Queue;

/**
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 *
 */
public class _104_MaxDepthOfBTree {
	
	/*
	 * 考虑递归的方法，树的深度等于左子树的深度与右子树的深度的最大值+1。
	 */
	public static int maxDepth(TreeNode root) {
		
		if(root == null) return 0;
		
		return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
	}
	/*
	 * 也可以使用广度遍历的方法，树的深度即为层数
	 */
	public int maxDepth1(TreeNode root) {
	    if(root == null) {
	        return 0;
	    }
	    Queue<TreeNode> queue = new LinkedList<>();
	    queue.offer(root);
	    int count = 0;
	    while(!queue.isEmpty()) {
	        int size = queue.size();
	        while(size-- > 0) {
	            TreeNode node = queue.poll();
	            if(node.left != null) {
	                queue.offer(node.left);
	            }
	            if(node.right != null) {
	                queue.offer(node.right);
	            }
	        }
	        count++;
	    }
	    return count;
	}

	public static void main(String[] args) {
		
	}

}
```
