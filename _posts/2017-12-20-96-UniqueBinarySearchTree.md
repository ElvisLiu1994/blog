---
layout: post
title: 96. Unique Binary Search Trees       
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
/**
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
 *
 */
public class _96_UniqueBinarySearchTree {
    
    // 纯递归的做法
    // 今次以1...n中的每个数做为根结构，判断左子树和右子树分别有多少种形式，然后相乘得到总的形式数目，再累加起来
    // 对于某棵子树结点数为0的结构，表示该棵子树为空，返回1
    // 当n=19时，leetcode测试超时
    public static int numTrees(int n) {
        
        if(n < 1) return 1;
        
        int res = 0;
        for(int i = 0; i < n; i++) {
            res += numTrees(i) * numTrees(n-1-i);
        }
        return res;
    }
    
    // 使用自顶向下的备忘法， 同样超时
    static int[] numTrees = new int[100];
    
    public static int numTrees1(int n) {
        
        if(n < 1) {
            numTrees[0] = 1;
            return 1;
        }
        
        if(numTrees[n] != 0) return numTrees[n];
        
        int res = 0;
        for(int i = 0; i < n; i++) {
            res += numTrees1(i) * numTrees1(n-1-i);
        }
        return res;
    }
    
    public static int numTreesDP(int n) {
        
        int[] dp = new int[n+1];
        dp[0] = 1;
        dp[1] = 1;
        // dp[i] 表示长度为i时的numTrees
        for(int i = 2; i <= n; i++) {
            // 当长度为i时，今次取0~i作为根结点，左子树的数目乘以右子树的数目，再累加起来
            for(int j = 0; j < i; j++) {
                dp[i] += dp[j] * dp[i-1-j];
            }
            
        }
        
        return dp[n];
    }

    public static void main(String[] args) {
        System.out.println(numTreesDP(19));
    }

}
```
