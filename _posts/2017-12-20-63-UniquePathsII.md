---
layout: post
title: 63. Unique Paths II               
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
/**
 * Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.
 * @author liujing
 *
 */
public class _63_UniquePathsII {
    
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        
        if(obstacleGrid == null || obstacleGrid.length == 0) return 0;
        
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        int[][] dp = new int[m][n];
        for(int i = 0; i < m && obstacleGrid[i][0] != 1; i++)
            dp[i][0] = 1;
        for(int i = 0; i < n && obstacleGrid[0][i] != 1; i++)
            dp[0][i] = 1;
        
        for(int i = 1; i < m; i++){
            for(int j = 1; j < n; j++){
                if(obstacleGrid[i][j] != 1)
                    //不需要判断上面和左边的元素是不是0
                    dp[i][j] = dp[i-1][j] + dp[i][j-1];
                else
                    dp[i][j] = 0;
            }
        }
        return dp[m-1][n-1];
    }

    public static void main(String[] args) {
        System.out.println(Math.round(1.805*100)/100.0);
        System.out.println(String.format("%.2f", 1.805));
    }

}
```
