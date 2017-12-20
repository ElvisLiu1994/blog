---
layout: post
title: 56. Merge Intervals 
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

/**
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
*/
public class _56_MergeIntervals {
    
    public List<Interval> merge(List<Interval> intervals) {
        
        if(intervals.size() < 2) return intervals;
        
        List<Interval> res = new ArrayList<Interval>();
        
        Collections.sort(intervals, new Comparator<Interval>(){

            @Override
            public int compare(Interval o1, Interval o2) {
                return o1.start - o2.start;
            }
            
        });
        
        int start = intervals.get(0).start;
        int end = intervals.get(0).end;
        
        for(int i = 1; i < intervals.size(); i++){
            Interval tmp = intervals.get(i);
            if(tmp.start <= end){
                end = Math.max(end,tmp.end);//这里不能直接end=tmp.end，因为有可能是[1,4][1,3]这种情况
            } else {
                res.add(new Interval(start,end));
                start = tmp.start;
                end = tmp.end;
            }
        }
        res.add(new Interval(start, end));
        return res;
    }

    public static void main(String[] args) {
        _56_MergeIntervals test = new _56_MergeIntervals();
        List<Interval> in = new ArrayList<Interval>();
        in.add(new Interval(1,3));
        in.add(new Interval(2,6));
        in.add(new Interval(8,10));
        in.add(new Interval(15,18));
        List<Interval> res = test.merge(in);
        for(Interval i : res)
            System.out.println(i.start + ", " + i.end);
    }

}

class Interval {
    int start;
    int end;
    Interval() { start = 0; end = 0; }
    Interval(int s, int e) { start = s; end = e; }
}
```
