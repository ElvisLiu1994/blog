---
layout: post
title: 72. Edit Distance       
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
/**
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
 *
 */
public class _72_EditDistance {
    
    public int minDistance(String word1, String word2){
        
        int n = word1.length();
        int m = word2.length();
        
        int[][] dp = new int[n+1][m+1];
        
        //initial
        for(int i = 0; i <= n; i++) dp[i][0] = i;
        for(int j = 0; j <= m; j++) dp[0][j] = j;
        
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                char ch1 = word1.charAt(i);
                char ch2 = word2.charAt(j);
                if(ch1 == ch2){
                    dp[i+1][j+1] = dp[i][j];
                }else{
                    dp[i+1][j+1] = Math.min(dp[i+1][j]+1, Math.min(dp[i][j+1]+1, dp[i][j]+1));
                }
            }
        }
        
        return dp[n][m];
        
    }

    public static void main(String[] args) {
        _72_EditDistance test = new _72_EditDistance();
        System.out.println(test.minDistance("", ""));
    }

}
```
