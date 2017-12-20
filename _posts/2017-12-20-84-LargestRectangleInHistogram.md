---
layout: post
title: 84. Largest Rectangle in Histogram   
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
/**
 * 
 *
 */
public class _84_LargestRectangleInHistogram {
    
    /**
     * 利用DP算法，dp[i]表示前i+1个数所能形成的最大矩形，在每一步中，有一个矩形加入，这个矩形要么能够形成更大的
     * 矩形，要么不会，所以依次向前遍历包含该矩形的最大面积，再与前面的dp值进行比较，判断是否会形成更大的面积，
     * 时间复杂度为O(n^2)，本质上是暴力求解; 95/96个test通过，最后一个全为1的大数组超时
     */
    public int largestRectangleArea(int[] heights) {
        
        if(heights == null || heights.length == 0) return 0;
        
        int[] dp = new int[heights.length];
        dp[0] = heights[0];
        
        for(int i = 1; i < heights.length; i++){
            int tmp = heights[i];
            int min = heights[i];
            for(int j = i-1; j >= 0; j--){
                if(heights[j] < min) min = heights[j];
                tmp = Math.max(tmp, min*(i - j + 1));
            }
            dp[i] = Math.max(dp[i-1], tmp);
        }
        
        return dp[heights.length-1];
    }
    
    /**
     * O(n) 使用栈结构
     * 当高度增高时，将该height的index入栈，直到找到某个height比栈顶的height要小，由于
     * 栈里面的高度，只能与比它们高的条来组成矩形，所以要将栈里面比当前条形高的条形分别计算
     * 面积后出栈，出栈结束的条件是，当前条形高度不再小于栈顶的高度。
     */
    public int largestRectangleArea1(int[] heights){
        int len = heights.length;
        
        int top = 0; //栈顶指针
        int[] stack = new int[len+1]; //栈数组
        int maxArea = 0;
        
        //为了避免当栈不空时结束循环，假设在heights数组里面有一个高度为0的元素，
        //这样可以把栈里面所有的元素都出栈，计算出所有可能的矩形面积。循环条件所以也应该是i<=len。
        for(int i = 0; i <= len; i++){
            //当前条形的高度，如果i==len，设置高度为0
            int curHeight = (i == len) ? 0 : heights[i];
            
            //如果当前栈为空，或者当前条形高度不低于栈顶的高度，则入栈当前条的index
            if(top == 0 || curHeight >= heights[stack[top-1]]){
                stack[top++] = i;
            }else{//否则进行出栈直至栈顶不高于当前条形，出栈的同时计算面积
                int stackTopHeight = heights[stack[--top]];
                //当top==0时说明栈为空，说明栈里面最后的这个元素为前i个(0~i-1)元素中最低的条形
                //因为比它高的都会出栈，所以这里可以将宽度设为i（0~i-1）。
                maxArea = Math.max(maxArea, stackTopHeight * ((top == 0) ? i : (i - 1 - stack[top-1])));
                i--;//此时应该保持当前条形不变，由于for语句中会执行i++,所以这里要先将i减1
            }
        }
        
        return maxArea;
    }

    public static void main(String[] args) {
        _84_LargestRectangleInHistogram test = new _84_LargestRectangleInHistogram();
        System.out.println(test.largestRectangleArea(new int[]{0,9}));
    }

}
```
