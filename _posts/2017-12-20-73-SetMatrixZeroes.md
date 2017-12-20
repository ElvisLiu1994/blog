---
layout: post
title: Set Matrix Zeroes   	
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
import java.util.HashSet;
import java.util.Set;

/**
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
 *
 */
public class _73_SetMatrixZeroes {
	
	//not constant space
	public void setZeroes(int[][] matrix){
		
		if(matrix == null) return;
		
		Set<Integer> rows = new HashSet<Integer>();
		Set<Integer> cols = new HashSet<Integer>();
		
		for(int i = 0; i < matrix.length; i++){
			for(int j = 0; j < matrix[0].length; j++){
				if(matrix[i][j] == 0){
					rows.add(i);
					cols.add(j);
				}
			}
		}
		
		for(int i : rows) {
			for(int j = 0; j < matrix[0].length; j++) matrix[i][j] = 0;
		}
		for(int j : cols){
			for(int i = 0; i < matrix.length; i++) matrix[i][j] = 0;
		}
	}
	
	//分别用两个变量来指示第一行和第二行是不是需要全设为0
	public void setZeroes1(int[][] matrix){
		boolean fr = false, fc = false;
		int rows = matrix.length;
		int cols = matrix[0].length;
		
		for(int i = 0; i < rows; i++){
			for(int j = 0; j < cols; j++){
				if(matrix[i][j] == 0){
					if(i == 0) fr = true;
					if(j == 0) fc = true;
					matrix[i][0] = matrix[0][j] = 0;
				}
			}
		}
		
		for(int i = 1; i < rows; i++){
			for(int j = 1; j < cols; j++){
				if(matrix[i][0] == 0 || matrix[0][j] == 0)
					matrix[i][j] = 0;
			}
		}
		
		if(fc) for(int i = 0; i < rows; i++) matrix[i][0] = 0;
		if(fr) for(int i = 0; i < cols; i++) matrix[0][i] = 0;
	}
	
	//只需要一个变量即可
	//I think what Chen try to do is to store information at the first element 
	//of each columns and rows. So if a column contains a 0, 
	//it's first element will be 0. Same for rows. However, 
	//both first column and first row use matrix[0][0]. 
	//He creates another variable for first column, col0.
	public void setZeroes2(int[][] matrix){
		boolean fc = false;
		int rows = matrix.length;
		int cols = matrix[0].length;
		
		for(int i = 0; i < rows; i++){
			if(matrix[i][0] == 0) fc = true;
			for(int j = 1; j < cols; j++){
				if (matrix[i][j] == 0)
	                matrix[i][0] = matrix[0][j] = 0;
			}
		}
		
		for (int i = 0; i < rows; i++) {
	        for (int j = 1; j < cols; j++)
	            if (matrix[i][0] == 0 || matrix[0][j] == 0)
	                matrix[i][j] = 0;
	        if (fc) matrix[i][0] = 0;
	    }
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
```
