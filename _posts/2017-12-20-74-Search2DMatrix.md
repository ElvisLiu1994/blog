---
layout: post
title: Search a 2D Matrix  
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
/**
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
 *
 */
public class _74_Search2DMatrix {
	
	public boolean searchMatrix(int[][] matrix, int target){
		if(matrix == null || matrix.length == 0 || matrix[0].length == 0) return false;
		
		int rows = matrix.length;
		int cols = matrix[0].length;
		
		int high = rows*cols-1;
		int low = 0;
		int mid, midr, midc;
		
		while(low <= high){
			
			mid = (high + low) >> 1;
			midr = mid / cols;
			midc = mid % cols;
			
			if(target == matrix[midr][midc]){
				return true;
			}else if(target > matrix[midr][midc]){
				low = mid+1;
			}else{
				high = mid-1;
			}
		}
		return false;
	}

	public static void main(String[] args) {
		_74_Search2DMatrix test = new _74_Search2DMatrix();
		int[][] m = new int[][]{{1,3,5,7},{10,11,16,20},{23, 30, 34, 50}};
		int[][] m1 = new int[][]{{1}};
		System.out.println(test.searchMatrix(m, 3));
	}

}
```
