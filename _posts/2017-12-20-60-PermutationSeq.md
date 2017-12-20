---
layout: post
title: Permutation Sequence   			
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
import java.util.ArrayList;
import java.util.List;

/**
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
 * @author liujing
 *
 */
public class _60_PermutationSeq {
	//这种递归回溯的方法提交后n=9时，有些数据超时
	public String getPermutation(int n, int k){
		if(k <= 0) return null;
		
		List<String> pers = new ArrayList<String>();
		solve(n, k, pers, new StringBuilder(""));
		return pers.get(pers.size()-1);
	}
	
	private void solve(int n, int k, List<String> pers, StringBuilder curPer){
		if(pers.size() == k)
			return;
		if(curPer.length() == n){
			pers.add(curPer.toString());
			return;
		}
		for(int i = 1; i <= n; i++){
			if(curPer.indexOf(String.valueOf(i)) == -1){
				curPer.append(i);
				solve(n, k, pers, curPer);
				curPer.deleteCharAt(curPer.length()-1);
			}
		}
	}
	
	public String getPermutation1(int n, int k){
		
		StringBuilder sb = new StringBuilder();
		
		//numbers = {1,2,3,4,...}
		List<Integer> nums = new ArrayList<Integer>();
		for(int i = 1; i <= n; i++)
			nums.add(i);
		
		int sum = 1;
		int[] factorial = new int[n+1];
		factorial[0] = 1;
		//fac[] = {1,1,2,6,24,...,n!}
		for(int i = 1; i <= n; i++){
			sum *= i;
			factorial[i] = sum; 
		}
		
		k--;
		
		for(int i = 1; i <= n; i++){
			int index = k/factorial[n-i];
			sb.append(String.valueOf(nums.get(index)));
			nums.remove(index);
			k -= index*factorial[n-i];
		}
		
		return String.valueOf(sb);
		
	}

	public static void main(String[] args) {
		_60_PermutationSeq test = new _60_PermutationSeq();
		System.out.println(test.getPermutation(9, 273815));
	}

}
```
