---
layout: post
title: Spiral Matrix   
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
 * Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
 *
	For example,
	Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
 * @author liujing
 *
 */
public class _54_SpiralMatrix {
	
	public List<Integer> spiralOrder(int[][] matrix){
		
		List<Integer> res = new ArrayList<Integer>();
		
		if(matrix.length == 0) return res;
		
		int rowBegin = 0, rowEnd = matrix.length-1;
		int colBegin = 0, colEnd = matrix[0].length-1;
		
		while(rowBegin <= rowEnd && colBegin <= colEnd){
			//向右扫描,扫描完一行，rowBegin需要加1
			for(int i = colBegin; i <= colEnd; i++)
				res.add(matrix[rowBegin][i]);
			rowBegin++;
			
			//向下扫描，向下扫描都是最右边的列，所以colEnd需要减1
			for(int i = rowBegin; i <= rowEnd; i++)
				res.add(matrix[i][colEnd]);
			colEnd--;
			
			//向左扫描，由于前面向右扫描过一行了，rowBeign可以大于rowEnd，这样会导致重复扫描了同一行，所以需要判断一下
			if(rowBegin <= rowEnd)
				for(int i = colEnd; i >= colBegin; i--)
					res.add(matrix[rowEnd][i]);
			rowEnd--;
			
			//向上扫描，同理需要判断（如果只有一列的话，这里不判断会导致重复扫描了这一列两次）
			if(colBegin <= colEnd)
				for(int i = rowEnd; i >= rowBegin; i--)
					res.add(matrix[i][colBegin]);
			colBegin++;
		}
		
		return res;
		
	}
	//这里判断得更多，时间开销更大一些
	public List<Integer> spiralOrder1(int[][] matrix){
		
		List<Integer> res = new ArrayList<Integer>();
		
		if(matrix.length == 0) return res;
		
		int rowBegin = 0, rowEnd = matrix.length-1;
		int colBegin = 0, colEnd = matrix[0].length-1;
		while(true){
			
			for(int i = colBegin; i <= colEnd; i++)
				res.add(matrix[rowBegin][i]);
			if(++rowBegin > rowEnd) break;
			
			for(int i = rowBegin; i <= rowEnd; i++)
				res.add(matrix[i][colEnd]);
			if(--colEnd < colBegin) break;
			
			for(int i = colEnd; i >= colBegin; i--)
				res.add(matrix[rowEnd][i]);
			if(--rowEnd < rowBegin) break;
			
			for(int i = rowEnd; i >= rowBegin; i--)
				res.add(matrix[i][colBegin]);
			if(++colBegin > colEnd) break;
		}
		return res;
	}
	
	/**
	 * When traversing the matrix in the spiral order, at any time we follow one out of 
	 * the following four directions: RIGHT DOWN LEFT UP. 
	 * Suppose we are working on a 5 x 3 matrix as such:
		0 1  2  3  4  5
	  	  6  7  8  9  10
	  	  11 12 13 14 15
		Imagine a cursor starts off at (0, -1), i.e. the position at '0', 
		then we can achieve the spiral order by doing the following:
			Go right 5 times
			Go down 2 times
			Go left 4 times
			Go up 1 times.
			Go right 3 times
			Go down 0 times -> quit
		Notice that the directions we choose always follow the order 
		'right->down->left->up', and for horizontal movements, the number of shifts 
		follows:{5, 4, 3}, and vertical movements follows {2, 1, 0}.
	 * @param matrix
	 * @return
	 */
	public List<Integer> spiralOrder2(int[][] matrix){
		List<Integer> res = new ArrayList<Integer>();
		
		int m = matrix.length;
        if(m == 0) return res;
        int n = matrix[0].length;
        if(n == 0) return res;
        
        int[][] direction = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int[] range = {n, m-1};//水平平移量从n开始减，竖直方向平移量从m-1开始
        int dir = 0; // index of dirMatrix, 0: right, 1: down, 2: left, 3: up
        int row = 0, col = -1; // initial position
        
        while(range[dir%2] != 0){
        	for(int i = 0; i < range[dir%2]; i++){
        		row += direction[dir][0];
        		col += direction[dir][1];
        		res.add(matrix[row][col]);
        	}
        	
        	range[dir%2]--;//平移量递减
        	dir = (dir+1) % 4;
        }
        
        return res;
	}

	public static void main(String[] args) {
		_54_SpiralMatrix test = new _54_SpiralMatrix();
		int[][] matrix = {{1,2,3},{4,5,6},{7,8,9}};
		System.out.println(test.spiralOrder2(matrix));
	}

}
```
