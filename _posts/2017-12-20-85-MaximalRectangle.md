---
layout: post
title: Maximal Rectangle   		
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
import java.util.Arrays;

/**
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle 
containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 6.
 *
 */
public class _85_MaximalRectangle {
	
	/**
	 * 可以考虑利用前一题，条形图的最大矩形，遍历每一行时的最大矩形面积，最终得到最大面积。
	 */
	public static int maximalRectangle(char[][] matrix) {
		
		if(matrix == null || matrix.length == 0)	return 0;
		
		int rows = matrix.length;
		int cols = matrix[0].length;

		int[] heights = new int[cols];
		int max = 0;
		//累加每一行的和
		for(int i = 0; i < rows; i++){
			for(int j = 0; j < cols; j++){
				//为0的列直接要将高度设置为0
				heights[j] = (matrix[i][j] == '0' ? 0 : heights[j]+1);
			}
			max = Math.max(max, largestRectangelInHistogram(heights));
		}
		return max;
	}
	
	public static int largestRectangelInHistogram(int[] heights){
		
		if(heights == null || heights.length == 0) return 0;
		
		int max = 0;
		int top = 0;
		int[] stack = new int[heights.length+1];
		
		for(int i = 0; i <= heights.length; i++){
			
			int curHeight = (i == heights.length ? 0 : heights[i]);
			
			if(top == 0 || curHeight >= heights[stack[top-1]]){
				stack[top++] = i;
			}else{
				int topHeight = heights[stack[--top]];
				max = Math.max(max, topHeight * (top == 0 ? i : i-1-stack[top-1]));
				i--;
			}
		}
		
		return max;
	}
	
	/**
	 * DP方法，依次计算以每一行为底时的最大矩形面积；
	 * 一共需要计算三个数组
	 */
    public static int maximalRectangle1(char[][] matrix) {
    	
		if(matrix == null || matrix.length == 0)	return 0;
		
		int rows = matrix.length;
		int cols = matrix[0].length;
		
		int maxArea = 0;
		//三个数组分别表示，高度为heights[j]时，左右边界分别为left[j]和right[j]
		int[] left = new int[cols];
		int[] right = new int[cols];
		int[] heights = new int[cols];
		
		Arrays.fill(left, 0);
		Arrays.fill(right, cols);//一定要把right数组初始化为cols;
		Arrays.fill(heights, 0);
		
		for(int i = 0; i < rows; i++){
			
			int curLeft = 0, curRight = cols;
			
			for(int j = 0; j < cols; j++){
				//计算高度数组，如果当前位置元素为1，那么高度直接在前一行的heights数组的该元素加上1
				if(matrix[i][j] == '1')
					heights[j]++;
				else //否则的话，该列的高度置为0
					heights[j] = 0;
				
				//计算left数组，从左至右
				if(matrix[i][j] == '1'){
					left[j] = Math.max(left[j], curLeft);
				}else{
					left[j] = 0;
					curLeft = j+1;
				}
				
				//计算right数组，从右至左
				if(matrix[i][cols-j-1] == '1'){
					right[cols-j-1] = Math.min(right[cols-j-1], curRight);
				}else{
					right[cols-j-1] = cols;
					curRight = cols-j-1;
				}
				
			}
			
			for(int j = 0; j < cols; j++){
				maxArea = Math.max(maxArea, (right[j]-left[j])*heights[j]);
			}
			
			System.out.println("h:"+Arrays.toString(heights));
			System.out.println("l:"+Arrays.toString(left));
			System.out.println("r:"+Arrays.toString(right));
			System.out.println();
			
		}
		
		return maxArea;
	}

	public static void main(String[] args) {
		char[][] matrix = new char[][]{ {'0','0','0','1','0','0','0'},
										{'0','0','1','1','1','0','0'},
										{'0','1','1','1','1','1','0'},
										 };
		System.out.println(maximalRectangle1(matrix));
	}

}
```
