---
layout: post
title: Binary Tree Level Order Traversal II  
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
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
 *
 */
public class _107_BinaryTreeLevelOrderTraversalII {
	
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        
        if(root == null) return res;
        
        LinkedList<TreeNode> queue = new LinkedList<TreeNode>();
        
        queue.offer(root);
        
        while(!queue.isEmpty()) {
        		int levelNum = queue.size();
        		List<Integer> sublist = new ArrayList<Integer>();
        		
        		for(int i = 0; i < levelNum; i++) {
    				TreeNode tmp = queue.poll();
    				sublist.add(tmp.val);
    				if(tmp.left != null) queue.offer(tmp.left);
    				if(tmp.right != null) queue.offer(tmp.right);
        		}
        		
        		res.add(0, sublist);
        }
        
        return res;
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
```
