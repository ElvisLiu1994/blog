---
layout: post
title: 34. Search for a Range       
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
/**
 * Given a sorted array of integers, find the starting and ending position of a given target value.
 * Your algorithm's runtime complexity must be in the order of O(log n).
 * If the target is not found in the array, return [-1, -1].
 * For example,
 * Given [5, 7, 7, 8, 8, 10] and target value 8,
 * return [3, 4].
 * @author liujing
 *
 */
public class _34_SearchForRange {
    
    public int[] searchRange(int nums[], int target){
        if(nums == null || nums.length == 0) return new int[]{-1,-1};
        
        int low = 0, high = nums.length-1;
        int mid,val;
        int[] result = new int[2];
        while(low <= high){
            mid = (low+high) >> 1;
            val = nums[mid];
            if(val == target){
                
                int tmp = mid;
                while(--tmp >= 0 && nums[tmp]==target);
                result[0] = tmp+1;
                
                tmp = mid;
                while(++tmp < nums.length && nums[tmp]==target);
                result[1] = tmp-1;
                
                return result;
            }else if(target < val){
                while(--mid >= 0 && nums[mid] == val);
                high = mid;
            }else{
                while(++mid < nums.length && nums[mid] == val);
                low = mid;
            }
        }
        
        return new int[]{-1,-1};
    }
    //two binary search
    public int[] searchRange1(int[] nums, int target){
        if(nums == null || nums.length == 0) return new int[]{-1,-1};
        
        int low = 0, high = nums.length-1;
        int[] result = new int[]{-1,-1};
        
        //最终跳出循环时肯定是low==high或者low-high==1时，而后面对nums[low]有判断，所以这里不用low<=high
        while(low < high){
            int mid = (low+high)>>1;
            if(nums[mid] < target){
                low = mid+1;
            }else{//这里也可以分开写成两个分支，在nums[mid] > target时可以是high=mid-1
                high = mid;
            }
        }
        if(nums[low] != target) return result;
        else result[0] = low;
        
        high = nums.length-1;
        while(low < high){
            int mid = ((low+high)>>1) + 1;
            if(nums[mid] > target){
                high = mid-1;
            }else{
                low = mid;
            }
        }
        result[1] = high;
        return result;
    }

    public static void main(String[] args) {
        _34_SearchForRange test = new _34_SearchForRange();
        int[] d = new int[]{5,7,7,8,8,10};
        int[] res = test.searchRange1(new int[]{2,2}, 2);
        System.out.println(res[0]+", "+res[1]);
    }

}
```
