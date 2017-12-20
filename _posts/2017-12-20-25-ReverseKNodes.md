---
layout: post
title: 25. Reverse Nodes in k-Group  
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
/**
 * Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
 * @author liujing
 *
 */
public class _25_ReverseKNodes {
    
    //recursion
    public ListNode reverseKGroup(ListNode head, int k){
        if(head == null || k == 1)
            return head;
        //recursion exit
        ListNode temp = head; //从head开始，所以i从1开始
        for(int i = 1; i < k; i++){
            temp = temp.next;
            if(temp == null)
                return head;
        }
        
        ListNode prev = new ListNode(0);
        prev.next = head;
        
        ListNode first = prev.next;
        ListNode last = temp;
        last.next = reverseKGroup(last.next, k);
        for(int i = 1; i < k; i++){
            prev.next = first.next;
            first.next = last.next;
            last.next = first;
            
            first = prev.next;
        }
        
        return prev.next;
        
    }
    //iterative solution
    public ListNode reverseKGroup1(ListNode head, int k){
        if(head == null || k == 1)
            return head;
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy, first, tail = prev;
        while(true){
            int i;
            for(i = 0; i < k; i++){
                tail = tail.next;
                if(tail == null) break;
            }
            if(i != k) break;
            
            head = prev.next;//for next loop
            
            for(i = 1; i < k; i++){
                first = prev.next;
                prev.next = first.next;
                first.next = tail.next;
                tail.next = first;
            }
            
            prev = head;
            tail = head;
        }
        return dummy.next;
    }

    public static void main(String[] args) {
        _25_ReverseKNodes test = new _25_ReverseKNodes();
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);
        
        head = test.reverseKGroup(head, 3);
        while(head != null){
            System.out.print(head.val+" ");
            head = head.next;
        }
    }

}
```
