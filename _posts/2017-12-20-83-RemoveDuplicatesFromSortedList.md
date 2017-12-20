---
layout: post
title: Remove Duplicates from Sorted List   
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
/**

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

 *
 */
public class _83_RemoveDuplicatesFromSortedList {
	
    public ListNode deleteDuplicates(ListNode head) {
        
    	if(head == null || head.next == null)
    		return head;
    	
    	ListNode fakeHead = new ListNode(0);
    	fakeHead.next = head;
    	ListNode pre = fakeHead;
    	
    	while(head != null) {
    		while(head.next != null && head.next.val == head.val) {
    			head = head.next;
    		}
    		if(pre.next == head) {
    			pre = head;
    			head = head.next;
    		}else {
    			pre.next = head;
    		}
    	}
    	
    	return fakeHead.next;
    }

	public static void main(String[] args) {
		_83_RemoveDuplicatesFromSortedList test = new _83_RemoveDuplicatesFromSortedList();
		ListNode head = new ListNode(new int[] {1,1,2});
		System.out.println(test.deleteDuplicates(head));
	}

}
```
