---
layout: post
title: 58. Length of Last Word           
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
/**
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.
 * @author liujing
 *
 */
public class _58_LenOfLastWord {
    
    public int lengthOfLastWord(String s) {
        
        if(s == null || s.length() == 0) return 0;
        
        int len = 0;
        String[] ss = s.split(" ");
        if(ss.length != 0)
            len = ss[ss.length-1].length();
        return len;
    }
    
    public int lengthOfLastWord1(String s) {
        return s.trim().length()-s.trim().lastIndexOf(" ")-1;
    }
    
    public int lengthOfLastWord2(String s) {
        int len = s.length(), lastLen = 0;
        char[] cs = s.toCharArray();
        while(len > 0 && cs[len-1] == ' ')
            len--;
        while(len > 0 && cs[len-1] != ' '){
            lastLen++;
            len--;
        }
        return lastLen;
    }

    public static void main(String[] args) {
        _58_LenOfLastWord test = new _58_LenOfLastWord();
        System.out.println(" ".split(" ").length);
    }

}
```
