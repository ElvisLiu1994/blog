---
layout: post
title: 70. Climbing Stairs 
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
/**
You are climbing a stair case. It takes n steps to reach to the top.
    
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
 * @author liujing
 *
 */
public class _70_ClimbingStairs {
    
    //当n=44时 Time limit exceeded
    public int climbStairs(int n) {
        if(n <= 1) return 1;
        
        return climbStairs(n-1) + climbStairs(n-2);
        
    }
    
    //memorized
    public int climbStairs1(int n ){
        int[] cache = new int[n+1];
        cache[0] = 1;
        cache[1] = 1;
        
        return solve(n, cache);
    }
    
    public int solve(int n, int[] cache){
        if(cache[n] != 0)
            return cache[n];
        int res = solve(n-1, cache) + solve(n-2, cache);
        cache[n] = res;
        return res;
    }
    
    //dynamic programming
    public int climbStairs2(int n){
        if(n < 2) return 1;
        
        //initial
        int[] dp = new int[n+1];
        dp[0] = 1;
        dp[1] = 1;
        
        for(int i = 2; i <= n; i++){
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    }

    public static void main(String[] args) {
        _70_ClimbingStairs test = new _70_ClimbingStairs();
        System.out.println(test.climbStairs2(44));
    }

}
```
