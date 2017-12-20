---
layout: post
title: 93. Restore IP Addresses       
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
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
 *
 */
public class _93_RestoreIPAddress {
    
    public static List<String> restoreIpAddresses(String s){
        
        List<String> res = new ArrayList<String>();
        
        if(s.length() < 4 || s.length() > 12) return res;
        
        solve(res, new StringBuilder(s), 0, 0);
        
        return res;
    }
    // dfs算法
    public static void solve(List<String> res, StringBuilder sb, int dotNum, int start){
        if(dotNum == 3) {
            if(isValid(sb.substring(start)))
                res.add(sb.toString());
            return;
        }
        // 最多三位，并且加点后面还需要有数字，所以需要start+i<sb.length()
        for(int i = 1; i <= 3 && start+i < sb.length(); i++){
            if(isValid(sb.substring(start, start+i))){
                solve(res, sb.insert(start+i, '.'), dotNum+1, start+i+1);
                sb.deleteCharAt(start+i);
            }
        }
    }
    
    private  static boolean isValid(String s){
        if(s.length()>3 || s.length()==0 || (s.charAt(0)=='0' && s.length()>1) || Integer.parseInt(s)>255)
            return false;
        return true;
    }
    // 暴力求解算法更快
    public static List<String> restoreIpAddresses1(String s){
        List<String> res = new ArrayList<String>();
        int len = s.length();
        for(int i = 1; i<4 && i<len-2; i++){
            for(int j = i+1; j<i+4 && j<len-1; j++){
                for(int k = j+1; k<j+4 && k<len; k++){
                    String s1 = s.substring(0,i), s2 = s.substring(i,j), s3 = s.substring(j,k), s4 = s.substring(k,len);
                    if(isValid(s1) && isValid(s2) && isValid(s3) && isValid(s4)){
                        res.add(s1+"."+s2+"."+s3+"."+s4);
                    }
                }
            }
        }
        return res;
    }

    public static void main(String[] args) {
        System.out.println(restoreIpAddresses("0000"));
        System.out.println(restoreIpAddresses("25525511135"));
        System.out.println(restoreIpAddresses("010010"));
        System.out.println(restoreIpAddresses("101023"));
    }

}
```
