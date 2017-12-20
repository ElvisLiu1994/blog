---
layout: post
title: 94. Binary Tree Inorder Traversal   
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

/**
 * Given a binary tree, return the inorder traversal of its nodes' values.
 * 
 * For example: Given binary tree [1,null,2,3], 
 * 1 
 *  \ 
 *   2 
 *  / 
 * 3 
 * 
 * return [1,3,2].
 * 
 * Note: Recursive solution is trivial, could you do it iteratively?
 *
 */
public class _94_BinaryTreeInorderTraversal {

    // 递归方法
    public static List<Integer> inorderTraversal(TreeNode root) {

        if (root == null)
            return new ArrayList<Integer>();

        List<Integer> res = new ArrayList<Integer>();

        res.addAll(inorderTraversal(root.left));
        res.add(root.val);
        res.addAll(inorderTraversal(root.right));

        return res;

    }

    // Method 1: Using one stack and the binary tree node will be changed. Easy
    // ,not Practical
    public static List<Integer> inorderTraversal1(TreeNode root) {

        List<Integer> res = new ArrayList<Integer>();

        if (root == null)
            return res;

        LinkedList<TreeNode> stack = new LinkedList<TreeNode>();

        stack.push(root);
        while (!stack.isEmpty()) {

            TreeNode top = stack.peek();
            if (top.left != null) {
                stack.push(top.left);
                top.left = null; // 其左子树后入栈会被先访问到，所以可以设置其左儿子为空，这样不会死循环
            } else {
                res.add(top.val);
                stack.pop();
                if (top.right != null) {
                    stack.push(top.right);
                }
            }

        }

        return res;
    }

    // Method 2: Using one stack and one unordered_map, this will not changed
    // the node. Better
    public static List<Integer> inorderTraversal2(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();

        if (root == null)
            return res;

        LinkedList<TreeNode> stack = new LinkedList<TreeNode>();
        Map<TreeNode, Boolean> map = new HashMap<TreeNode, Boolean>();
        // left child has been visited:true.

        stack.push(root);
        while (!stack.isEmpty()) {

            TreeNode top = stack.peek();
            // 如果左孩子不为空，并且还没有被访问过
            if (top.left != null && !map.get(top)) {
                stack.push(top.left);
                map.put(top.left, true);
            } else {
                res.add(top.val);
                stack.pop();
                if (top.right != null)
                    stack.push(top.right);
            }
        }

        return res;
    }

    // Method 3: Using one stack and will not changed the node. Best(at least in
    // this three solutions)
    public static List<Integer> inorderTraversal3(TreeNode root) {

        List<Integer> res = new ArrayList<Integer>();

        if (root == null)
            return res;

        LinkedList<TreeNode> stack = new LinkedList<TreeNode>();

        TreeNode cur = root;
        while (cur != null || !stack.isEmpty()) {

            if (cur != null) {
                stack.push(cur);
                cur = cur.left;
            } else {
                TreeNode top = stack.pop();
                res.add(top.val);
                cur = top.right;
            }

            /*
             * 下面这种写法与上面是一样的 
             * while(cur != null){ 
             *     stack.push(cur); 
             *     cur = cur.left; 
             * } 
             * TreeNode top = stack.pop(); 
             * res.add(top.val); 
             * cur = top.right;
             */

        }

        return res;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        root.right = new TreeNode(2);
        root.right.left = new TreeNode(3);

        TreeNode root1 = new TreeNode(new int[] { 1, -1, 2, 3 });

        System.out.println(inorderTraversal1(root1));
    }

}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
    
    private int counter = 0;
    // 递归创建二叉树，这里提供的数组是前序遍历的数组，包含Null，比如[1, null, 2, 3]对应题目中的情况    
    TreeNode(int[] nums) {
        this.counter = 0;
        this.val = nums[counter++];
        this.left = createTreeNode(nums);
        this.right = createTreeNode(nums);
    }

    TreeNode createTreeNode(int[] nums) {
        if (counter < nums.length) {
            if (nums[counter] == -1) {
                counter++;
                return null;
            } else {
                TreeNode node = new TreeNode(nums[counter++]);
                node.left = createTreeNode(nums);
                node.right = createTreeNode(nums);
                return node;
            }
        }else{
            return null;
        }
    }
}
```
