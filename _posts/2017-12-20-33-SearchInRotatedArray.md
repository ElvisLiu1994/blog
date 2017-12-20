---
layout: post
title: 33. Search in Rotated Sorted Array       
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
/**
 * Suppose a sorted array is rotated at some pivot unknown to you beforehand.
 * (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
 * You are given a target value to search. If found in the array return its index, otherwise return -1.
 * You may assume no duplicate exists in the array.
 * @author liujing
 *
 */
public class _33_SearchInRotatedArray {
    //this is the O(n) method
    public int search1(int[] nums, int target){
        if(nums == null || nums.length == 0) return -1;
        
        int mid = nums.length;
        for(int i = 1; i < nums.length; i++){
            if(nums[i] < nums[i-1])
                mid = i;
        }
        int res = BiSearch(nums, 0, mid,target);
        if(res != -1) return res;
        res = BiSearch(nums, mid, nums.length,target);
        if(res != -1) return res;
        return -1;
    }
    
    private int BiSearch(int[] nums, int s, int e,int target){
        if(s >= e) return -1;
        int mid;
        while(s < e){
            mid = (s+e) >> 1;
            if(nums[mid] == target)
                return mid;
            else if(nums[mid] < target){
                s = mid+1;
                
            }else 
                e = mid;
        }
        return -1;
    }
    //1. 使用二分法时用start和end，end指向最后一个元素与指向最后一个元素的下一个位置有什么区别？
    // 在求mid时有区别，如果总共偶数个数，那么end指向最后一个元素时mid为中间左元素，否则mid为中间右元素
    //2. 使用二分法时while(s<e)和while(s<=e)有什么区别？
    // 在判断分支中，如果e=mid那么只能用s<e，如果e=mid-1那么都可以用
    public int search2(int[] nums, int target){
        if(nums == null || nums.length == 0) return -1;
        
        int s = 0, e = nums.length - 1;
        int mid = 0, minIdx = 0;
        
        //e指向最后一个元素
        while(s < e){
            mid = (s+e) >> 1;
             if(nums[mid] > nums[e]) s = mid+1;
            else e = mid; //如果用while(s<=e)那么会限入死循环,因为这里不是e=mid-1；因为这里mid可能是最小的元素，不能排除掉
        }
        
        minIdx = s;
        if(target == nums[minIdx]) return minIdx;
        s = (target > nums[nums.length-1]) ? 0 : minIdx;
        e = (target > nums[nums.length-1]) ? minIdx-1 : nums.length-1;
        //这里也可以用s<e，只是在循环执行完后，要加上对s==e这一点值的判断就可以了
        while(s <= e){
            mid = (s+e)>>1;
            if(nums[mid] == target) return mid;
            else if(nums[mid] < target) s = mid+1;
            else e = mid-1; //由于mid元素肯定不是需要的，所以e=mid-1，上面必须用s<=e，否最后一个e元素检测不到
        }
        return -1;
    }
    
    public int search3(int[] nums, int target) {
        if(nums == null || nums.length == 0) return -1;
        int lo = 0;
        int hi = nums.length - 1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (nums[mid] == target) return mid;
            
            if (nums[lo] <= nums[mid]) {
                if (target >= nums[lo] && target < nums[mid]) {
                    hi = mid - 1;
                } else {
                    lo = mid + 1;
                }
            } else {
                if (target > nums[mid] && target <= nums[hi]) {
                    lo = mid + 1;
                } else {
                    hi = mid - 1;
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        _33_SearchInRotatedArray test = new _33_SearchInRotatedArray();
        int[] nums = new int[]{};
        System.out.println(test.search3(nums, 5));
    }

}
```
