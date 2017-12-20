---
layout: post
title: 23. Merge k Sorted Lists  
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
import java.util.Comparator;
import java.util.PriorityQueue;

public class _23_MergeKLists {
    //也可以利用分治法和MergeTwoLists来实现，复杂度同样是O(nlogk)，但是空间复杂度不同
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0)
            return null;

        PriorityQueue<ListNode> que = new PriorityQueue<ListNode>(lists.length, new Comparator<ListNode>() {
            @Override
            public int compare(ListNode o1, ListNode o2) {
                if(o1.val < o2.val)
                    return -1;
                else if(o1.val == o2.val)
                    return 0;
                else 
                    return 1;
            }
        });
        
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        
        for(ListNode node : lists){
            if(node != null)
                que.add(node);
        }
        
        while(!que.isEmpty()){
            tail.next = que.poll();
            tail = tail.next;
            
            if(tail.next != null){
                que.add(tail.next);
            }
        }
        return dummy.next;
    }

    public static void main(String[] args) {
        // TODO Auto-generated method stub
        _23_MergeKLists test = new _23_MergeKLists();
        ListNode l1 = new ListNode(2);
        l1.next = new ListNode(3);
        ListNode l2 = new ListNode(1);
        ListNode[] lists = new ListNode[2];
        lists[0] = l1;
        lists[1] = l2;
        ListNode res = test.mergeKLists(lists);
        while (res != null) {
            System.out.print(res.val + " ");
            res = res.next;
        }
    }

}
```
