---
layout: post
title: Combination Sum   	
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Given a set of candidate numbers (C) (without duplicates) and a target number
 * (T), find all unique combinations in C where the candidate numbers sums to T.
 * 
 * The same repeated number may be chosen from C unlimited number of times.
 * 
 * Note: All numbers (including target) will be positive integers. The solution
 * set must not contain duplicate combinations. For example, given candidate set
 * [2, 3, 6, 7] and target 7, A solution set is: [ [7], [2, 2, 3] ]
 * 
 * @author liujing
 *
 */
public class _39_CombinationSum {

	public List<List<Integer>> combinationSum(int[] candidates, int target) {
		if (candidates == null || candidates.length == 0)
			return null;

		List<List<Integer>> res = new ArrayList<List<Integer>>();
		Arrays.sort(candidates);
		// solve(candidates, target, 0, 0,res, new ArrayList<Integer>());
		solve(candidates, target, 0, res, new ArrayList<Integer>());
		return res;
	}

	// 这是自己的做法，一开始没有使用start，导致结果中老是出现重复的结果
	private void solve(int[] candidates, int target, int curSum, int start, List<List<Integer>> res,
			List<Integer> cur) {

		for (int i = start; i < candidates.length; i++) {
			if (curSum + candidates[i] == target) {
				cur.add(candidates[i]);
				res.add(new ArrayList<Integer>(cur));
				cur.remove(cur.size() - 1);// 这一句也很重要，不然组合中会包含之前多余的数据
				return;
			} else if (curSum + candidates[i] < target) {
				cur.add(candidates[i]);
				solve(candidates, target, curSum + candidates[i], i, res, cur);
				cur.remove(cur.size() - 1);// 重要
			} else {
				return;
			}

		}
	}

	private void solve(int[] candidates, int target, int start, List<List<Integer>> res, List<Integer> combination) {
		if (target == 0) {
			res.add(new ArrayList<Integer>(combination));
			return;//回溯
		}
		for (int i = start; i < candidates.length && target >= candidates[i]; i++) {
			combination.add(candidates[i]);
			solve(candidates, target-candidates[i], i, res, combination);//递归
			combination.remove(combination.size() - 1);
		}
	}

	public static void main(String[] args) {
		_39_CombinationSum test = new _39_CombinationSum();
		int[] candidates = new int[] { 2, 3, 6, 7 };
		int target = 7;
		List<List<Integer>> res = test.combinationSum(candidates, target);
		for (List<Integer> l : res) {
			System.out.println(l);
		}
	}

}
```
