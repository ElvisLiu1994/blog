---
layout: post
title: Remove Duplicates from Sorted List II   	
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
/**
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
 * @author liujing
 *
 */

public class _82_RemoveDuplicatesFromSortedListII {
	
	public ListNode deleteDuplicates(ListNode head) {
		
		if(head == null || head.next == null) 
			return head; 
		
		ListNode dummy = new ListNode(0);
		dummy.next = head;
		ListNode pre = dummy;
		
		while(head != null && head.next != null) {
			if(head.next.val != head.val) {
				pre = head;
				head = head.next;
			} else {
				while(head.next != null && head.next.val == head.val)
					head = head.next;
				head = head.next;
				pre.next = head;
			}
		}
		
		return dummy.next;
	}
	
	//改进后的代码
	public ListNode deleteDuplicates1(ListNode head) {
        if(head==null) return null;
        ListNode FakeHead=new ListNode(0);
        FakeHead.next=head;
        ListNode pre=FakeHead;
        ListNode cur=head;
        while(cur!=null){
            while(cur.next!=null&&cur.val==cur.next.val){
                cur=cur.next;
            }
            if(pre.next==cur){
                pre=pre.next;
            }
            else{
                pre.next=cur.next;
            }
            cur=cur.next;
        }
        return FakeHead.next;
    }
	//递归版本
	public ListNode deleteDuplicates3(ListNode head) {
	    if (head == null) return null;
	    
	    if (head.next != null && head.val == head.next.val) {
	        while (head.next != null && head.val == head.next.val) {
	            head = head.next;
	        }
	        return deleteDuplicates(head.next);
	    } else {
	        head.next = deleteDuplicates(head.next);
	    }
	    return head;
	}

	public static void main(String[] args) {
		_82_RemoveDuplicatesFromSortedListII test = new _82_RemoveDuplicatesFromSortedListII();
		ListNode head = new ListNode(new int[] {1,1});
		head = test.deleteDuplicates(head);
		System.out.print(head);
	}

}
```
