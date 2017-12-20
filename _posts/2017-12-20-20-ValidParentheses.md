---
layout: post
title: 20. Valid Parentheses  
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
import java.util.LinkedList;

public class _20_ValidParentheses {
    /**
     * Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
        The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
     * @param s
     * @return
     */
    public boolean isValid(String s){
        if(s == null || s.length() == 0)
            return true;
        
        LinkedList<Character> stack = new LinkedList<Character>();
        char[] ch = s.toCharArray();
        for(int i = 0; i < ch.length; i++){
            
            if(!stack.isEmpty() && isMatch(stack.peek(),ch[i])){
                stack.pop();
                continue;
            }else{
                stack.push(ch[i]);
            }
            
        }
        if(stack.isEmpty())
            return true;
        
        return false;
    }
    
    public boolean isMatch(char c1, char c2){
        if(c1 == '(' && c2 == ')' || c1 == '{' && c2 == '}' || c1 == '[' && c2 == ']')
            return true;
        return false;
    }

    public static void main(String[] args) {
        _20_ValidParentheses test = new _20_ValidParentheses();
        System.out.println(test.isValid("(){}[]"));
    }

}
```
