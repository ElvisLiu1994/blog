---
layout: post
title: Rotate Image   	
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 * You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
 * @author liujing
 *
 */
public class _48_RotateImage {
	//常规做法，空间复杂度较高O(n*m)
	public void rotate(int[][] matrix){
		if(matrix == null || matrix.length <= 1) return;
		
		int m = matrix.length, n = matrix[0].length;
		int[][] tmp = new int[n][m];
		for(int i = 0; i < m; i++){
			for(int j = 0; j < n; j++){
				tmp[j][m-i-1] = matrix[i][j];
			}
		}
		
		for(int i = 0; i < m; i++){
			matrix[i] = Arrays.copyOf(tmp[i], n);
		}
	}
	
	/*
	 * clockwise rotate
	 * first reverse up to down, then swap the symmetry 
	 * 1 2 3     7 8 9     7 4 1
	 * 4 5 6  => 4 5 6  => 8 5 2
	 * 7 8 9     1 2 3     9 6 3
	*/
	public void rotate_clockwise(int[][] matrix){
		Collections.reverse(Arrays.asList(matrix));
		//下面这段代码相当上面这一句的作用
//		int s = 0, e = matrix.length-1;
//		while(s < e){
//			int[] tmp = matrix[s];
//			matrix[s] = matrix[e];
//			matrix[e] = tmp;
//			s++; e--;
//		}
		
		int m = matrix.length;
		for(int i = 0; i < m; i++){
			for(int j = 0; j < i; j++){
				int tmp = matrix[i][j];
				matrix[i][j] = matrix[j][i];
				matrix[j][i] = tmp;
			}
		}
	}
	/*
	 * anticlockwise rotate
	 * first reverse left to right, then swap the symmetry
	 * 1 2 3     3 2 1     3 6 9
	 * 4 5 6  => 6 5 4  => 2 5 8
	 * 7 8 9     9 8 7     1 4 7
	*/
	public void rotate_anticlockwise(int[][] matrix){
		/*
		 * 下面这种做法不能实现矩阵左右的调换，因为m是一个基本类型的数组，而asList方法使用的是泛型的可变参数
		 * 所以asList方法会将m看成只有一个数组引用的数组，而上面的方法中由于matrix是int[][]，本身是引用的
		 * 数组，所以编译器直接将matrix看成是元素类型为int[]的数组，从而实现调换。
		 */
//		for(int[] m : matrix)
//			Collections.reverse(Arrays.asList(m));
		
		for(int[] m : matrix){
			int s = 0, e = m.length-1;
			while(s < e){
				int tmp = m[s];
				m[s] = m[e];
				m[e] = tmp;
				s++; e--;
			}
		}
		
		int m = matrix.length;
		for(int i = 0; i < m; i++){
			for(int j = 0; j < i; j++){
				int tmp = matrix[i][j];
				matrix[i][j] = matrix[j][i];
				matrix[j][i] = tmp;
			}
		}
	}

	public static void main(String[] args) {
		_48_RotateImage test = new _48_RotateImage();
		int[][] m = {{1,2,3},{4,5,6},{7,8,9}};
		test.rotate_anticlockwise(m);
		
//		int[][] tmp = Arrays.copyOf(m, m.length);
//		System.out.println(m.length);
//		tmp[0][0] = 9;//会改变m中相应位置的值，数组名是引用类型，所以这里的拷贝，是拷贝了所有的行数组引用到了tmp
		for(int[] s : m){
			for(int t : s)
				System.out.print(t+"\t");
			System.out.println();
		}
//		System.out.println("--------------------");
//		
//		for(int[] s:tmp){
//			for(int t: s)
//				System.out.print(t+"\t");
//			System.out.println();
//		}
//		
//		int[] a = {1,2,3};
//		for(int t : a)
//			System.out.print(t+"\t");
//		System.out.println("\n--------------------");
//		List<Integer> l = Arrays.asList(a);//这里a不是引用数组，是基本类型的数组，然后asList方法使用的
//		泛型的可变参数，这就要求传入的必需是引用数组，这里只会将a当作一个元素，即只有一个引用的数组看待。
//		Collections.reverse(Arrays.asList(a));
//		for(int t : a)
//			System.out.print(t+"\t");
		
		
	}

}
```
