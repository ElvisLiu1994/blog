---
layout: post
title: 65. Valid Number               
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Validate if a given string is numeric.
 * 
 * Some examples: "0" => true " 0.1 " => true "abc" => false "1 a" => false
 * "2e10" => true Note: It is intended for the problem statement to be
 * ambiguous. You should gather all requirements up front before implementing
 * one.
 * 
 * @author liujing
 *
 */
public class _65_ValidNumber {
    // 使用正则表达式来判断
    public boolean isNumber(String s) {
        String regex = "\\s*[-+]?(([0-9]+(\\.[0-9]*)?)|\\.[0-9]+)(e[-+]?[0-9]+)?\\s*";
        return Pattern.compile(regex).matcher(s).matches();
    }

    public boolean isNumber1(String s) {
        s = s.trim();

        boolean pointSeen = false;//出现了'.'
        boolean eSeen = false;//出现了'e'
        boolean numberSeen = false;//出现了数字
        boolean numberAfterE = true;//如果出现了e的话，后面必须要出现数字

        for (int i = 0; i < s.length(); i++) {
            if ('0' <= s.charAt(i) && s.charAt(i) <= '9') {
                numberSeen = true;
                numberAfterE = true;
            } else if (s.charAt(i) == '.') {
                if (eSeen || pointSeen) {
                    return false;
                }
                pointSeen = true;
            } else if (s.charAt(i) == 'e') {
                if (eSeen || !numberSeen) {
                    return false;
                }
                numberAfterE = false;
                eSeen = true;
            } else if (s.charAt(i) == '-' || s.charAt(i) == '+') {
                if (i != 0 && s.charAt(i - 1) != 'e') {
                    return false;
                }
            } else {
                return false;
            }
            
        }
        return numberSeen && numberAfterE;
    }

    public static void main(String[] args) {
        String ip = "((2[0-4]\\d|25[0-5]|(1\\d{2}|[1-9]?\\d))\\.){3}(2[0-4]\\d|25[0-5]|(1\\d{2}|[1-9]?\\d))";
        String greedy = ".*+0";
        Pattern p = Pattern.compile(greedy);
        Matcher m = p.matcher("000001");
        System.out.println(m.matches());
        
        System.out.println(m.replaceFirst("r"));
        
        _65_ValidNumber test = new _65_ValidNumber();
        System.out.println("\n"+test.isNumber(".1e10"));
    }

}
```
