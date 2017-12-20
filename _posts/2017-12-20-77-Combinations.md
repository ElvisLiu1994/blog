---
layout: post
title: Combinations   		
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

/**
 * Given two integers n and k, return all possible combinations of k numbers out
 * of 1 ... n.
 *
 */
public class _77_Combinations {

	public List<List<Integer>> combine(int n, int k) {

		List<List<Integer>> res = new ArrayList<List<Integer>>();
		if(n == 0 || k == 0 || n < k) return res;
		
		res = solveBFS(n, k);

		return res;
	}

	//BFS 最后一个test超时，n = 20, k = 16
	private List<List<Integer>> solveBFS(int n, int k) {

		LinkedList<List<Integer>> queue = new LinkedList<List<Integer>>();
		queue.add(new ArrayList<Integer>());

		for (int i = 0; i < k; i++) {//k次循环，得到长度为k的所有组合
			
			while (queue.peek().size() == i) {//对当前长度为i的所有组合加上一个比目前最大的数还要大的数
				List<Integer> head = queue.remove();
				int curMax = head.size() == 0 ? 0 : head.get(head.size() - 1);//当前组合中最大的数
				for (int j = curMax + 1; j <= n; j++) {//因为是求组合数，不用考虑排列，所以可以这样加
					List<Integer> tmp = new ArrayList<Integer>(head);
					tmp.add(j);
					queue.add(tmp);
				}
			}

		}
		return queue;

	}
	
	//DFS 递归回溯
    public static List<List<Integer>> combine1(int n, int k) {
		List<List<Integer>> combs = new ArrayList<List<Integer>>();
		combine1(combs, new ArrayList<Integer>(), 1, n, k);
		return combs;
	}
	public static void combine1(List<List<Integer>> combs, List<Integer> comb, int start, int n, int k) {
		if(k==0) {
			combs.add(new ArrayList<Integer>(comb));
			return;
		}
		for(int i=start;i<=n;i++) {
			comb.add(i);
			combine1(combs, comb, i+1, n, k-1);
			comb.remove(comb.size()-1);
		}
	}

	public static void main(String[] args) {
		_77_Combinations test = new _77_Combinations();
		List<List<Integer>> res = test.combine(4, 2);
		for (List<Integer> l : res) {
			System.out.println(l);
		}
	}

}
```
