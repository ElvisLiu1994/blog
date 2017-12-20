---
layout: post
title: 24. Swap Nodes in Pairs       
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
/**
 * 
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
 * @author liujing
 *
 */
public class _24_SwapNodePairs {
    
    public ListNode swapPairs(ListNode head){
        if(head == null || head.next == null)
            return head;
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        
        ListNode prev = dummy;
        ListNode first;
        ListNode second;
        while(prev.next != null && prev.next.next != null){
            first = prev.next;
            second = prev.next.next;
            
            first.next = second.next;
            second.next = first;
            prev.next = second;
            
            prev = prev.next.next;
        }
        
        return dummy.next;
    }
    
    //recursion, so smart!!!
    public ListNode swapPairs1(ListNode head) {
        if ((head == null)||(head.next == null))
            return head;
        ListNode n = head.next;
        head.next = swapPairs(head.next.next);
        n.next = head;
        return n;
    }

    public static void main(String[] args) {
        _24_SwapNodePairs test = new _24_SwapNodePairs();
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);
        
        head = test.swapPairs(head);
        while(head != null){
            System.out.print(head.val+" ");
            head = head.next;
        }
        
    }

}
```
