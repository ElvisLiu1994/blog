---
layout: post
title: 98. Validate Binary Search Tree       
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
import java.util.LinkedList;

/**
 * 
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.
 *
 */
public class _98_ValidateBST {
    
    /**
     * BST需要满足的条件为：根节点的值要在正确的区间，左子树为BST，右子树为BST
     * 这里的区间约束为自上而下递归变化地
     * 
     * 一开始的想法是，让root.val大于左子树的最大值，小于右子子树的最大值，但是这两个值的信息不知道，
     * 所以可以通过不限定root.val的值，而将root.val作为一个约束，让其子树满足约束条件
     * 这里的不限定是指一开始的root的约束为Integer.MIN_VALUE和Integer.MAX_VALUE
     */
    public boolean isValidBST(TreeNode root) {
        return isValidBST(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }
    
    public boolean isValidBST(TreeNode root, int minVal, int maxVal) {
        if(root == null) return true;
        if(root.val >= maxVal || root.val <= minVal) return false;
        return isValidBST(root.left, minVal, root.val) && isValidBST(root.right, root.val, maxVal);
    }
    
    /**
     * BST的中序遍历是有序的，可以通过中序遍历来判断
     */
    public boolean isValidBST1(TreeNode root) {
        if(root == null) return true;
        LinkedList<TreeNode> stack = new LinkedList<TreeNode>();
        TreeNode pre = null;
        while(root != null || !stack.isEmpty()) {
            while(root != null) {
                stack.push(root);
                root = root.left;
            }
            root = stack.pop();
            if(pre != null && root.val <= pre.val) return false;
            pre = root;
            root = root.right;
        }
        return true;
    }

    public static void main(String[] args) {
        // TODO Auto-generated method stub

    }

}
```
