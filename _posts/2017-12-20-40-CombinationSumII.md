---
layout: post
title: Combination Sum II   	
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

public class _40_CombinationSumII {
	//每个数只能被使用一次
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
		if (candidates == null || candidates.length == 0)
			return null;
		
		List<List<Integer>> res = new ArrayList<List<Integer>>();
		Arrays.sort(candidates);
		
		solve(candidates,target,0,res,new ArrayList<Integer>());
		
		return res;
    }
    
    private void solve(int[] candidates, int target, int start, List<List<Integer>> res, List<Integer> cur){
    	if(target == 0){
    		res.add(new ArrayList<Integer>(cur));//不能直接add(cur)，因为cur是要重复使用的
    		return;
    	}
//    	if(target < 0) return;//加上这一句，可以去掉下面for循环中的后半个条件，但是会多一层递归，结果导致超时。
    	for(int i = start; i < candidates.length && candidates[i] <= target; i++){
    		if(i > start && candidates[i] == candidates[i-1]) continue;//过滤
    		cur.add(candidates[i]);
    		solve(candidates,target-candidates[i],i+1,res,cur);//i+1保证每一个数最多只使用了一次，
    		//但由于candidates中可能有重复数据，所以结果集中也会出现重复结果。
    		
    		cur.remove(cur.size()-1);
    	}
    }

	public static void main(String[] args) {
		_40_CombinationSumII test = new _40_CombinationSumII();
		int[] candidates = new int[] {10, 1, 2, 7, 6, 1, 5};
		int target = 8;
		List<List<Integer>> res = test.combinationSum(candidates, target);
		for (List<Integer> l : res) {
			System.out.println(l);
		}
	}

}
```
