---
layout: post
title: 95. Unique Binary Search Trees II   
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
 * 
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
 *
 */
public class _95_UniqueBinarySearchTreeII {
    
    public static List<TreeNode> generateTrees(int n) {
        
        if(n == 0) return new ArrayList<TreeNode>();
        
        List<TreeNode> res = generate(1,n);
        
        return res;
    }
    // 利用96题中递归的思想
    private static List<TreeNode> generate(int start, int end) {
        
        List<TreeNode> res = new ArrayList<TreeNode>();
        
        if(start > end) {
            res.add(null);
            return res;
        }
        
        List<TreeNode> left, right;
        for(int i = start; i <= end; i++) {
            left = generate(start,i-1);
            right = generate(i+1,end);
            
            for(TreeNode lnode : left) {
                for(TreeNode rnode : right) {
                    TreeNode root = new TreeNode(i);
                    root.left = lnode;
                    root.right = rnode;
                    res.add(root);
                }
            }
        }
        
        return res;
    }

    public static void main(String[] args) {
        // TODO Auto-generated method stub

    }

}
```
