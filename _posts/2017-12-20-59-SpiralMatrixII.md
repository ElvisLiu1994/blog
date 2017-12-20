---
layout: post
title: 59. Spiral Matrix II               
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
import java.util.Arrays;

/**
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,
You should return the following matrix:

[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

 * @author elvisliu
 *
 */
public class _59_SpiralMatrixII {
    
    public int[][] generateMatrix(int n){
        
        if(n <= 0) return new int[0][];
        
        int c = 1;
        int[][] res = new int[n][n];
        int rowBegin = 0, rowEnd = n-1;
        int colBegin = 0, colEnd = n-1;
        while(rowBegin <= rowEnd && colBegin <= colEnd){
            
            for(int i = colBegin; i <= colEnd; i++)
                res[rowBegin][i] = c++;
            rowBegin++;
            
            for(int i = rowBegin; i <= rowEnd; i++)
                res[i][colEnd] = c++;
            colEnd--;
            
            if(rowBegin <= rowEnd){
                for(int i = colEnd; i >= colBegin; i--)
                    res[rowEnd][i] = c++;
                rowEnd--;
            }
            
            if(colBegin <= colEnd){
                for(int i = rowEnd; i >= rowBegin; i--)
                    res[i][colBegin] = c++;
                colBegin++;
            }
        }
        
        return res;
    }

    public static void main(String[] args) {
        _59_SpiralMatrixII test = new _59_SpiralMatrixII();
        
        for(int[] arr : test.generateMatrix(3))
            System.out.println(Arrays.toString(arr));
                
    }

}
```
