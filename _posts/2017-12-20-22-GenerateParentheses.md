---
layout: post
title: Generate Parentheses   	
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
 * Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
 * [
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
   ]
 * @author liujing
 *
 */
public class _22_GenerateParentheses {
	
	public List<String> generateParenthesis(int n){
		
		List<String> res = new ArrayList<String>();
		recursion(res, "", n, n);
		return res;
		
	}
	
	public void recursion(List<String> res, String s, int left, int right){
		if(left == 0 && right == 0){
			res.add(s);
			return;
		}
		if(left > 0)
			recursion(res, s+"(", left-1, right);
		if(right > left)
			recursion(res, s+")", left, right-1);
	}

	public static void main(String[] args) {
		_22_GenerateParentheses test = new _22_GenerateParentheses();
		System.out.println(test.generateParenthesis(4));
	}

}
```
