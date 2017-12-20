---
layout: post
title: Partition List   	
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
/**
Given a linked list and a value x, partition it such that all nodes less than x come 
before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
 *
 */
public class _86_PartitionList {
	
	/**
	 * 根据快排中partition的思想，若是数组或双向链表，可以从两端开始遍历进行交换
	 * 单向链表的话只能使用顺序遍历，先找到链尾节点，遍历时发现大于等于x的节点直接移动到链尾
	 * 该方法有一个关键在于保存链尾节点以及原始的链尾节点
	 */
	public static ListNode partition(ListNode head, int x){
		
		if(head == null || head.next == null) return head;
		
		ListNode dummy = new ListNode(Integer.MIN_VALUE);
		dummy.next = head;
		head = dummy; //这样可以解决head比x大情况
		
		//原始链尾节点
		ListNode originTail = head;
		while(originTail.next != null) originTail = originTail.next;
		
		//当前链尾节点，随着往后面插入新的节点而变化
		ListNode curTail = originTail;
		
		while(head.next != originTail){
			if(head.next.val < x){
				head = head.next;
			}else{
				//当head.next = head.next.next后，被扔掉链尾的节点需要用tmp来保存，用来设置其next节点为null
				ListNode tmp = head.next;
				
				curTail.next = head.next;
				head.next = head.next.next;
				tmp.next = null;
				
				curTail = curTail.next;
			}
		}
		//单独判断originTail节点
		if(originTail.val >= x){
			curTail.next = originTail;
			head.next = originTail.next;
			originTail.next = null;
		}
		
		return dummy.next;
	}
	
	public static ListNode partition1(ListNode head, int x){
		ListNode smallHead = new ListNode(0);//fake head
		ListNode bigHead = new ListNode(0);//fake head
		
		ListNode smallTail = smallHead;
		ListNode bigTail = bigHead;
		
		while(head != null){
			if(head.val < x){
				smallTail = smallTail.next = head;
			}else{
				bigTail = bigTail.next = head;
			}
			head = head.next;
		}
		
		smallTail.next = bigHead.next;
		bigTail.next = null;//避免bigTail的next还指向small链表后面的元素
							//比如[1,4,2]，x=3，把4添加到big链表后，其后面还需要与2断开
		return smallHead.next;
	}

	public static void main(String[] args) {
		ListNode head = new ListNode(new int[]{2,1});
		
		System.out.println(partition1(head,2));
	}

}
```
