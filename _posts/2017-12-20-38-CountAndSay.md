---
layout: post
title: 38. Count and Say  
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
/*
 * The count-and-say sequence is the sequence of integers beginning as follows:
    1, 11, 21, 1211, 111221, ...

    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.
    Given an integer n, generate the nth sequence
 */
public class _38_CountAndSay {
    
    public String countAndSay(int n) {
        String result = "1";
        
        for(int c = 1; c < n; c++){
            String prev = result;
            result = "";
            int count = 1;
            char say = prev.charAt(0);
            
            for(int i = 1; i < prev.length(); i++){
                if(prev.charAt(i) == say)
                    count++;
                else{
                    result = result + count + say;//count为整型，但是会被自动转为字符串，这里如果用(count+'0')的话会是一个Ascall码的数字，如果count是1，则(count+'0')为49
                    count = 1;
                    say = prev.charAt(i);
                }
            }
            result = result + count + say;
        }
        
        return result;
    }

    public static void main(String[] args) {
        _38_CountAndSay test = new _38_CountAndSay();
        System.out.println(test.countAndSay(6));
    }

}
```
