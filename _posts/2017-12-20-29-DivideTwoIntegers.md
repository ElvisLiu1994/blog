---
layout: post
title: Divide Two Integers   	
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
/**
 * Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
 * @author liujing
 *
 */
public class _29_DivideTwoIntegers {
	
	public int divide(int dividend, int divisor){
		if(divisor == 0 || dividend == Integer.MIN_VALUE && divisor == -1)
			return Integer.MAX_VALUE;
		if(divisor == 1)
			return dividend;
		
		long dvd = Math.abs((long)dividend);
		long dvs = Math.abs((long)divisor);
		int sign = ((dividend < 0) ^ (divisor < 0)) ? -1 : 1;
		int res = 0;
		while(dvd >= dvs){
			long temp = dvs, multiple = 1;
			while(dvd >= (temp << 1)){
				temp <<= 1;
				multiple <<= 1;
			}
			dvd -= temp;
			res += 	multiple;
		}
		return sign == 1 ? res : -res;
	}

	public static void main(String[] args) {
		_29_DivideTwoIntegers test = new _29_DivideTwoIntegers();
		System.out.println(test.divide(-2147483648, 2));
		System.out.println(Math.abs(-2147483648));
	}

}
```
