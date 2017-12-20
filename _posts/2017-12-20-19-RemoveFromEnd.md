---
layout: post
title: Remove Nth Node From End of List   	
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
/**
 * Given a linked list, remove the nth node from the end of list and return its head.
 * the n is valid
 */

class ListNode{
	int val;
	ListNode next;
	
	ListNode(int x){
		this.val = x;
	}
	
	ListNode(int[] nums){
		
		this.val = nums[0];
		ListNode tail = this;
		
		for(int i = 1; i < nums.length; i++) {
			ListNode tmp = new ListNode(nums[i]);
			tail.next = tmp;
			tail = tail.next;
		}
	}

	@Override
	public String toString() {
		
		ListNode cur = this;
		StringBuilder sb = new StringBuilder("[ ");
		while(cur != null) {
			sb.append(cur.val+" ");
			cur = cur.next;
		}
		return sb.toString()+"]";
	}
	
	
}

public class _19_RemoveFromEnd {
	public ListNode removeNthFromEnd(ListNode head, int n){
		if(head == null || n <= 0)
			return head;
		
		ListNode start = new ListNode(0);
		ListNode slow = start, fast = start;
		start.next = head;
		
		//move fast in front so that the gap between slow and fast becomes n
		int i;
		for(i = 0; i < n+1; i++){
			fast = fast.next;
		}
		
		while(fast != null){
			slow = slow.next;
			fast = fast.next;
		}
		
		slow.next = slow.next.next;
		
		//why don't return head?
		//because head may be deleted
		return start.next;
	}
	

	public static void main(String[] args) {
		_19_RemoveFromEnd test = new _19_RemoveFromEnd();
		ListNode head = new ListNode(1);
//		head.next = new ListNode(2);
//		head.next.next = new ListNode(3);
//		head.next.next.next = new ListNode(4);
//		head.next.next.next.next = new ListNode(5);
		
		head = test.removeNthFromEnd(head, 1);
		while(head != null){
			System.out.print(head.val+" ");
			head = head.next;
		}
	}

}


```
