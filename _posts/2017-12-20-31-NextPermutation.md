---
layout: post
title: 31. Next Permutation       
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
/**
 * Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
 * @author liujing
 *
 */
public class _31_NextPermutation {

    /**
     * 方案一：找出最后一个升序对，即找到最后一个极值，然后将后面的降序重新排列为升序，将极值与第一个比它
     * 大的数进行交换
     * 改进的地方：1.从数组后面往前遍历；2.先交换，再reverse
     * @param nums
     */
    public void nextPermutation(int[] nums){
        if(nums == null || nums.length == 1) return;
        
        int N = nums.length, idx = N - 2;
        while(idx >= 0 && nums[idx] >= nums[idx+1]) idx--;
        if(idx >= 0){
            int j = N-1;
            while(nums[j] <= nums[idx]) j--;
            swap(nums, idx, j);
        }
        reverse(nums,idx+1,N-1);
    }
    
    public void swap(int[] nums, int i, int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    
    public void reverse(int[] A, int i, int j) {
        while(i < j) swap(A, i++, j--);
    }
    
    public static void main(String[] args) {
        _31_NextPermutation test = new _31_NextPermutation();
        int[] nums = new int[]{1,3,2};
        test.nextPermutation(nums);
        for(int i : nums){
            System.out.print(i+ " ");
        }
    }

}
```
