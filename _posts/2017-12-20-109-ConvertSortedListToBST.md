---
layout: post
title: 109. Convert Sorted List to Binary Search Tree   
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
/**
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
 *
 */

public class _109_ConvertSortedListToBST {
    
    /*
     * 通过双指针法可以找到链表的中间节点
     */
    public static TreeNode sortedListToBST(ListNode head) {
        if(head == null) return null;
        // 这里的tail使用null,表示是一个左闭右开的区间，这样做的好处是不用通过遍历的方式寻找链表的尾节点
        return solve(head, null);
    }
  
    public static TreeNode solve(ListNode head, ListNode tail) {
        ListNode slow = head;
        ListNode fast = head;
        if(head == tail) return null;
      
        while(fast != tail && fast.next != tail) {
            fast = fast.next.next;
            slow = slow.next;
        }
        TreeNode tmp = new TreeNode(slow.val);
        tmp.left = solve(head,slow);
        tmp.right = solve(slow.next,tail);
        return tmp;
    }

    public static void main(String[] args) {
        // TODO Auto-generated method stub

    }

}
```
