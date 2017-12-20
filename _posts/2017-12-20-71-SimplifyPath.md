---
layout: post
title: Simplify Path   		
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
import java.util.LinkedList;

/**
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".

 *
 */
public class _71_SimplifyPath {
	
	public String simplifyPath(String path){
		
		StringBuilder sb = new StringBuilder();
		
		String[] splits = path.split("/");
		String[] stack = new String[splits.length];
		int top = 0;
		
		for(String s : splits){
			
			if(s.length() == 0 || s.equals(".")){
				continue;
			}else if(s.equals("..")){
				top = (top == 0 ? 0 : top-1);
			}else{
				stack[top++] = s;
			}
				
		}
		
		if(top == 0) return "/";
		
		for(int i = 0; i < top; i++){
			sb.append("/" + stack[i]);
		}
		
		return sb.toString();
	}

	public static void main(String[] args) {
		_71_SimplifyPath test = new _71_SimplifyPath();
		System.out.println(test.simplifyPath("/home//foo"));
	}

}
```
