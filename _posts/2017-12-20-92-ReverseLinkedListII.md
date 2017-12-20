---
layout: post
title: 92. Reverse Linked List II   
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
/**
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
 *
 */
public class _92_ReverseLinkedListII {
    
    public static ListNode reverseBetween(ListNode head, int m, int n) {
        
        if(head == null || head.next == null) return head;
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        
        ListNode prev = dummy, tail = head;
        
        // 移动head指向第m个Node，tail指向第n个Node
        for(int i = 1; i < n; i++)
            tail = tail.next;
        for(int i = 1; i < m; i++) {
            head = head.next;
            prev = prev.next; // 保持prev指向head，交换顺序时需要用到prev引用
        }
        
        // 需要进行reverse的node个数为(n-m+1)，需要将前(n-m)个node依次移到tail后面，所以循环次数是(n-m)
        for(int i = m; i < n; i++) {
            prev.next = head.next;
            head.next = tail.next;
            tail.next = head;
            
            head = prev.next;
        }
        
        return dummy.next;
        
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(new int[] {1,2,3,4,5}) ;
        head = reverseBetween(head, 1, 5);
        System.out.println(head);
    }

}
```
