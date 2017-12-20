---
layout: post
title: 80. Remove Duplicates from Sorted Array II  
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
import java.util.Arrays;

/**
 * Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 
1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
 *
 */
public class _80_RemoveDuplicatesII {
    
    public int removeDuplicates(int[] nums) {
        
        if(nums.length <= 2) return nums.length;
        
        boolean flag = false;
        int index = 1;
        for(int i = 1; i < nums.length; i++){
            if(nums[i] != nums[i-1]){
                nums[index++] = nums[i];
                flag = false;
            }else if(!flag){
                nums[index++] = nums[i];
                flag = true;
            }
        }
        
        return index;
    }
    
    public int removeDuplicates1(int[] nums){
        int i = 0;
        for(int n : nums){
            if(i < 2 || n > nums[i-2])
                nums[i++] = n;
        }
        return i;
    }

    public static void main(String[] args) {
        _80_RemoveDuplicatesII test = new _80_RemoveDuplicatesII();
        int[] nums = new int[]{1,1,1,2,2,3};
        System.out.println(test.removeDuplicates(nums));
        System.out.print(Arrays.toString(nums));
    }

}
```
