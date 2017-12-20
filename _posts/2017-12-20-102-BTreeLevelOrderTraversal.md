---
layout: post
title: Binary Tree Level Order Traversal   	
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
/**
 * Given a binary tree, return the level order traversal of its nodes' values. 
 * (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
 *
 */
public class _102_BTreeLevelOrderTraversal {
	
	public static List<List<Integer>> levelOrder(TreeNode root) {
		
		List<List<Integer>> res = new ArrayList<List<Integer>>();
		
		if(root == null) return res;
		
		LinkedList<TreeNode> queue = new LinkedList<TreeNode>();
		
		queue.offer(root);
		while(!queue.isEmpty()) {
			
			int levelNum = queue.size();
			List<Integer> subList = new ArrayList<Integer>();
			
			for(int i = 0; i < levelNum; i++) {
				TreeNode tmp = queue.poll();
				subList.add(tmp.val);
				if(tmp.left != null) queue.offer(tmp.left);
				if(tmp.right != null) queue.offer(tmp.right);
			}
			
			res.add(subList);
		}
		
		return res;
	}

	public static void main(String[] args) {
		TreeNode root = new TreeNode(new int[] {3,9,-1,-1,20,15,-1,-1,7});
		List<List<Integer>> res = levelOrder(root);
		for(List<Integer> l : res) {
			System.out.println(l);
		}
	}

}
```
