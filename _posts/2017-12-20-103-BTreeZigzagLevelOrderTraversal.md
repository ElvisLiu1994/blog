---
layout: post
title: 103. Binary Tree Zigzag Level Order Traversal       
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
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
 *
 */
public class _103_BTreeZigzagLevelOrderTraversal {
    
    /*
     * 同样考虑使用队列来解决问题，设置一个标志变量，每遍历完一行，换一次顺序。
     *       1
     *      / \
     *     2   3
     *    /     \
     *   4       5
     * 对于这样的结构遍历结果应该为[[1],[3,2],[4,5]]
     * 实际运行结果为[[1],[3,2],[5,4]]，因为3先入的队列，于是会先将3的儿子先入队，导致5先遍历到
     */
    public static List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if(root == null) return res;
        
        LinkedList<TreeNode> queue = new LinkedList<TreeNode>();
        
        queue.offer(root);
        boolean order = false; //false表示从右往左，true表示从左往右
        while(!queue.isEmpty()) {
            int levelNum = queue.size();
            List<Integer> subList = new ArrayList<Integer>();
            for(int i = 0; i < levelNum; i++) {
                if(order) {
                    if(queue.peek().left != null) queue.add(queue.peek().left);
                    if(queue.peek().right != null) queue.add(queue.peek().right);
                } else {
                    if(queue.peek().right != null) queue.add(queue.peek().right);
                    if(queue.peek().left != null) queue.add(queue.peek().left);
                }
                subList.add(queue.poll().val);
            }
            order = !order;
            res.add(subList);
        }
        
        return res;
    }
    
    /*
     * 由于需要每一个level的遍历顺序与下一个level的遍历顺序相反，可以考虑使用两个栈结构，
     * 遍历当前level的栈时，将儿子都push到另一个栈，另一个栈出栈顺序刚好与当前栈相反，达到zigzag的效果
     */
    public static List<List<Integer>> zigzagLevelOrder1(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if(root == null) return res;
        
        LinkedList<TreeNode> stack1 = new LinkedList<TreeNode>();
        LinkedList<TreeNode> stack2 = new LinkedList<TreeNode>();
        
        stack1.push(root);
        while(!stack1.isEmpty() || !stack2.isEmpty()) {
            List<Integer> subList = new ArrayList<Integer>();
            if(!stack1.isEmpty()) {
                while(!stack1.isEmpty()) {
                    if(stack1.peek().left != null) stack2.push(stack1.peek().left);
                    if(stack1.peek().right != null) stack2.push(stack1.peek().right);
                    subList.add(stack1.pop().val);
                }
            }else {
                while(!stack2.isEmpty()) {
                    if(stack2.peek().right != null) stack1.push(stack2.peek().right);
                    if(stack2.peek().left != null) stack1.push(stack2.peek().left);
                    subList.add(stack2.pop().val);
                }
            }
            res.add(subList);
        }
        return res;
    }
    
    /*
     * 在插入数据时，换顺序即可
     */
    public static List<List<Integer>> zigzagLevelOrder2(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if(root == null) return res;
        
        LinkedList<TreeNode> queue = new LinkedList<TreeNode>();
        
        queue.offer(root);
        boolean order = true; //false表示从右往左，true表示从左往右
        while(!queue.isEmpty()) {
            int levelNum = queue.size();
            List<Integer> subList = new ArrayList<Integer>();
            for(int i = 0; i < levelNum; i++) {
                if(queue.peek().left != null) queue.add(queue.peek().left);
                if(queue.peek().right != null) queue.add(queue.peek().right);
                if(order) {
                    subList.add(queue.poll().val);
                } else {
                    subList.add(0, queue.poll().val);
                }
            }
            order = !order;
            res.add(subList);
        }
        
        return res;
    }
    
    public static void main(String[] args) {
        TreeNode root = new TreeNode(new int[] {1,2,4,-1,-1,-1,3,-1,5});
        List<List<Integer>> res = zigzagLevelOrder2(root);
        for(List<Integer> l : res) {
            System.out.println(l);
        }
    }

}
```
