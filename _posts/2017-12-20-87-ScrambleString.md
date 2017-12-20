---
layout: post
title: Scramble String   	
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
/**
 * Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
 *
 */
public class _87_ScrambleString {
	/**
	 * 当字符串的长度为3时，可以通过不同的二叉树以及scramble获得所有6种排列方式，以此为基础进行推断
	 * 当字符串的长度为4时，在3的基础上，第4个字符可以通过scramble插入字符串的任意位置。
	 * 依此推断，只需要两个字符串所包含的字符是一样的，那么它们就是scrambled的。
	 * 难点在于两个字符串中有重复的字符时，重复字符的数量还要相等，所以不能简单地使用set来实现。
	 * 
	 * WRONG: abcd  bdac
	 */
	public static boolean isScramble1(String s1, String s2){
		
		int[] hash = new int[256];
		
		for(char c: s1.toCharArray()) {
			hash[c]++;
		}
		
		for(char c : s2.toCharArray()) {
			hash[c]--;
		}
		
		for(int x : hash) {
			if(x != 0) return false;
		}
		
		return true;
	}
	
	/**
	 * 前面过滤掉一些基本的情况后，后面使用递归进行求解。
	 */
	public static boolean isScramble(String s1, String s2) {
		
		if(s1.length() != s2.length()) return false;
		
		if(s1.equals(s2)) return true;
		
		int[] hash = new int[256];
		for(int i = 0; i < s1.length(); i++) {
			hash[s1.charAt(i)]++;
			hash[s2.charAt(i)]--;
		}
		//如果包含的字符集不一样，那么返回false
		for(int i = 0; i < hash.length; i++) {
			if(hash[i] != 0) return false;
		}
		
		int len = s1.length();
		//这里的i一定不能从0开始，如果i从0开始的话，那么每次两段会被分为0和len长度的两段，len长度的继续分为0和len两段
		//最终栈溢出
		for(int i = 1; i < len; i++) {
			if(isScramble(s1.substring(0, i), s2.substring(0, i)) 
					&& isScramble(s1.substring(i), s2.substring(i)))
				return true;
			if(isScramble(s1.substring(0, i), s2.substring(len-i)) && 
					isScramble(s1.substring(i), s2.substring(0,len-i)))
				return true;
		}
		return false;
	}

	public static void main(String[] args) {
		System.out.println(isScramble("great", "rgtae"));
	}

}
```
