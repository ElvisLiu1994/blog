---
layout: post
title: Longest Valid Parentheses  
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
import java.util.LinkedList;

/**
 * Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
 *
 * For "(()", the longest valid parentheses substring is "()", which has length = 2.
 * 
 * Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
 * @author liujing
 *
 */
public class _32_LongestValidParentheses {
	
	public int longestValidParentheses(String s){
		if(s == null || s.length() == 0) return 0;
		
		char[] ch = s.toCharArray();
		LinkedList<Integer> stack = new LinkedList<Integer>();
		int longest = 0;
		
		for(int i = 0; i < ch.length; i++){
			if(ch[i] == '('){
				stack.push(i);
			}else{
				if(!stack.isEmpty()){
					if(ch[stack.peek()] == '(') stack.pop();
					else stack.push(i);
				}else{
					stack.push(i);
				}
			}
		}
		
		if(stack.isEmpty()) 
			return s.length();
		
		int a = s.length(), b = 0;
		while(!stack.isEmpty()){
			b = stack.pop();
			longest = Math.max(longest, a-b-1);
			a = b;
		}
		longest = Math.max(a, longest);
		return longest;
	}
	//one pass, the method upside need two pass of the stack
	public int longestValidParentheses1(String s){
		if(s == null || s.length() == 0) return 0;
		
		char[] ch = s.toCharArray();
		LinkedList<Integer> stack = new LinkedList<Integer>();
		int longest = 0;
		stack.push(-1);//
		
		for(int i = 0; i < ch.length; i++){
			int t = stack.peek();
			if(t != -1 && ch[i] == ')' && ch[t] == '('){
				stack.pop();
				longest = Math.max(longest, i-stack.peek());
				//can not use longest += 2!
				//()(()这种情况结果会是4！
				//在每次pop之后进行max求值，一定会保存最长被pop掉的长度！
			}else
				stack.push(i);
		}
		
		return longest;
	}
	
	//DP
	public int longestValidParentheses2(String s){
		if(s == null || s.length() <= 1) return 0;
		
		int[] dp = new int[s.length()];
		char[] ch = s.toCharArray();
		int longest = 0;
		for(int i = 1; i < s.length(); i++){
			if(s.charAt(i) == ')' && i-dp[i-1]-1>=0 && ch[i-dp[i-1]-1] == '('){
				dp[i] = dp[i-1] + 2 + ((i-dp[i-1]-2 >= 0 ? dp[i-dp[i-1]-2] : 0));
				longest = Math.max(longest, dp[i]);
			}
		}
		return longest;
	}

	public static void main(String[] args) {
		_32_LongestValidParentheses test = new _32_LongestValidParentheses();
		System.out.println(test.longestValidParentheses("()()"));
	}

}
```
