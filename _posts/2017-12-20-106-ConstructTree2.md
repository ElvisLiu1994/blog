---
layout: post
title: 106. Construct Binary Tree from Inorder and Postorder Traversal       
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
import java.util.LinkedList;

/**
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

       13
     /    \
    2      3
   / \    /
  5   6  7
        / \
       8   9
            \
            10
            /
          12

5,  2,  6,  13,  8,  7,  9,  12,  10,  3
---left--- root  ---------right---------

5,  6,  2,  8,  12,  10,  9,  7,  3,  13
---left---    ---------right---------- root 
 *
 */
public class _106_ConstructTree2 {
    
    /*
     * 递归方法
     * The post order array will give you the root, the last one.
     * 1. With the root, you can go to the in order array, notice the traverse sequence: left, root, right.
     * 2. Then we know the left child array size, right child array size.
     * 3. With the size, we can then divide the post order array: left, right, root.
     * Then, we have everything!
     * The beauty is the root, with the root, you are able to divide two arrays~
     */
    public static TreeNode buildTree(int[] inorder, int[] postorder) {
        return helper(postorder.length-1, 0, inorder.length-1, inorder, postorder);
    }
    
    public static TreeNode helper(int postStart, int inStart, int inEnd, int[] inorder, int[] postorder) {
        if(postStart == postorder.length || inStart > inEnd) return null;
        TreeNode root = new TreeNode(postorder[postStart]);
        int inIndex = 0;
        for(int i = inStart; i <= inEnd; i++) {
            if(root.val == inorder[i])
                inIndex = i;
        }
        
        root.left = helper(postStart-(inIndex-inStart)-1, inStart, inIndex-1, inorder, postorder);
        root.right = helper(postStart-1, inIndex+1, inEnd, inorder, postorder);
        return root;
    }
    
    /*
     * postorder数组如果反过来访问，那们就相当于preorder中先根后右再左的访问顺序，所以这里跟105的区别就在于：
     * 反过来的遍历数组，并且优先创建右子树。
     */
    public static TreeNode buildTree1(int[] inorder, int[] postorder) {
        if(inorder.length == 0) return null;
        LinkedList<TreeNode> stack = new LinkedList<>();
        TreeNode root = new TreeNode(postorder[postorder.length-1]), cur = root;
        
        for(int i = postorder.length-2, j = inorder.length-1; i >= 0; i--) {
            if(cur.val != inorder[j]) {
                cur.right = new TreeNode(postorder[i]);
                stack.push(cur);
                cur = cur.right;
            } else {
                j--;
                while(!stack.isEmpty() && stack.peek().val == inorder[j]) {
                    cur = stack.pop();
                    j--;
                }
                cur.left = new TreeNode(postorder[i]);
                cur = cur.left;
            }
        }
        return root;
    }
    
    public static void main(String[] args) {
        // TODO Auto-generated method stub

    }

}
```
