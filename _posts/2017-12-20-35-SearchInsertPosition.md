---
layout: post
title: Search Insert Position  
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java

public class _35_SearchInsertPosition {
	
	public int searchInsert(int[] nums, int target){
		if(nums.length == 0) return 0;
		
		int low = 0, high = nums.length-1;
		int mid,val;
		while(low < high){
			
			mid = (low+high)>>1;
			val = nums[mid];
			
			if(val == target){
				return mid;
			}else if(val < target){
				low = mid+1; //可能导致low==high跳出循环
			}else{
				high = mid;//high=mid-1可能导致low==high+1也跳出循环,而写成high=mid，退出时只有low=high
			}
		}
		if(nums[low] >= target) return low;//由于没有使用while(low<=high)，需要对第一种情况进行补充判断
		else return low+1;
	}
	
    public int searchInsert1(int[] A, int target) {
        int low = 0, high = A.length-1;
        while(low<=high){//这里退出循环的条件一定是low==high+1，所以返回时统一返回low就可以了
            int mid = (low+high)/2;
            if(A[mid] == target) return mid;
            else if(A[mid] > target) high = mid-1;
            else low = mid+1;
        }//循环条件带等号，所以只能low=mid+1和high=mid-1,否则有可能死循环。
        return low;
    }

	public static void main(String[] args) {
		_35_SearchInsertPosition test = new _35_SearchInsertPosition();
		int[] nums = new int[]{1,3,5,6};
		System.out.println(test.searchInsert(nums, 0));
	}

}
```
