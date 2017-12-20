---
layout: post
title: 53. Maximum Subarray
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java

public class _53_MaxSubarray {
    
    public int maxSubArray(int[] nums){
        int n = nums.length;
        int[] dp = new int[n];
        dp[0] = nums[0];
        int max = dp[0];
        //dp[i]表示以nums[0-i]中的最大子数组和，只有当dp[i-1]小于0时需要从新从i开始计算和，前面i-1个dp值总会存储一个最大的值
        for(int i = 1; i < n; i++){
            dp[i] = nums[i]+(dp[i-1] > 0 ? dp[i-1] : 0);
            max = Math.max(max, dp[i]);
        }
        return max;
    }
    
    public static void main(String[] args) {
        // TODO Auto-generated method stub

    }

}
```
