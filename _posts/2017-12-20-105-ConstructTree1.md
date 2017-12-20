---
layout: post
title: 105. Construct Binary Tree from Preorder and Inorder Traversal       
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
import java.util.LinkedList;

/**
 * Given preorder and inorder traversal of a tree, construct the binary tree.
 *
 */
public class _105_ConstructTree1 {
    
    /*
     * 使用递归方法，preorder的第一个值肯定是root结点的值，然后在inorder中找到root的位置，其左边的部分即为左子树的所有值，右边为右子树的值。
     * 因为inorder数组中需要记录两边子树的范围，所以需要inStart和inEnd，通过从中找到root的位置inIndex，
     * 然后将该区间分为[inStart, inIndex-1]和[inIndex+1, inEnd]递归创建左子树和右子树
     */
    public static TreeNode buildTree(int[] preorder, int[] inorder) {
        return helper(0, 0, inorder.length-1, preorder, inorder);
    }
    
    public static TreeNode helper(int preStart, int inStart, int inEnd, int[] preorder, int[] inorder) {
        if(preStart == preorder.length || inStart > inEnd) {
            return null;
        }
        TreeNode root = new TreeNode(preorder[preStart]);
        int inIndex = 0; // Index of current root in inorder
        for(int i = inStart; i <= inEnd; i++) {
            if(inorder[i] == root.val)
                inIndex = i;
        }
        root.left = helper(preStart+1, inStart, inIndex-1, preorder, inorder);
        root.right = helper(preStart+inIndex-inStart+1, inIndex+1, inEnd, preorder, inorder);
        return root;
    }
    
    /*
     * 使用非递归的方法
     * 这里的思路与前面的递归方法稍微有些不同，它不用去inorder中找到root的位置。
     * 先通过preorder递归地创建左子树，当最左的结点被建立时，此时该结点的值与inorder的第一个数正好是相等的，
     * 然后通过比较栈中与inorder相等地的结点，将这些结点直接出栈，在不等的地方创建右子结点，然后再循环。
     * 
     * 1. Keep pushing the nodes from the preorder into a stack (and keep making the tree by adding nodes to the left of the previous node) until the top of the stack matches the inorder.
     * 2. At this point, pop the top of the stack until the top does not equal inorder (keep a flag to note that you have made a pop).
     * 3. Repeat 1 and 2 until preorder is empty.
     */
    public static TreeNode buildTree1(int[] preorder, int[] inorder) {
        if(preorder.length == 0) return null;
        LinkedList<TreeNode> stack = new LinkedList<>();
        TreeNode root = new TreeNode(preorder[0]), cur = root;
        
        for(int i = 1, j = 0; i < preorder.length; i++) {
            if(cur.val != inorder[j]) { // 递归地创建左子结点，直到与inorder[j]相等，说明没有更左的结点了
                cur.left = new TreeNode(preorder[i]);
                stack.push(cur);
                cur = cur.left;
            } else { // cur.val == inorder[j]
                j++;
                while(!stack.isEmpty() && stack.peek().val == inorder[j]) {
                    cur = stack.pop(); // 依次出栈直到碰到第一个右子结点
                    j++;
                }
                cur.right = new TreeNode(preorder[i]);
                cur = cur.right;
            }
        }
        return root;
    }

    public static void main(String[] args) {
        // TODO Auto-generated method stub

    }

}
```
