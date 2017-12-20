---
layout: post
title: 81. Search in Rotated Sorted Array II   
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
/**
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
 *
 */
public class _81_SearchInRotatedArrayII {
    
    public boolean search(int[] nums, int target) {
        
        if(nums == null || nums.length == 0) return false;
        
        int low = 0;
        int high = nums.length - 1;
        
        while(low <= high) {
            int mid = (low + high) >> 1;
        
            if(nums[mid] == target) return true;
            
            if(nums[mid] < nums[high]) {//能找到右边有序的部分
                if(nums[mid] < target && target <= nums[high]) {
                    low = mid + 1;
                }else {
                    high = mid - 1;
                }
            }else if(nums[mid] > nums[high]){//能找到左边的有序部分
                if(nums[low] <= target && target < nums[mid]) {
                    high = mid - 1;
                }else {
                    low = mid + 1;
                }
            }else {//i.e. 11113511,对于这种情况我们只能将high一步一步得试探，有可能mid至high均相等，但也可能中间有大的数
                high--;
            }
        }
        
        return false;
    }

    public static void main(String[] args) {
        _81_SearchInRotatedArrayII test = new _81_SearchInRotatedArrayII();
        int[] nums = new int[] {1,3,1,1,1};
        System.out.println(test.search(nums, 3));
    }

}
```
