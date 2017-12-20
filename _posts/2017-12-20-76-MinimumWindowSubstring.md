---
layout: post
title: 76. Minimum Window Substring    
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
/**
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
 *
 */
public class _76_MinimumWindowSubstring {
    
    public String minWindow(String s, String t) {
        
        int[] map = new int[128]; // ascii码
        
        //初始化map
        for(int i = 0; i < t.length(); i++)
            map[t.charAt(i)]++;
        
        int counter = t.length(); //check whether the substring is valid
        int begin = 0, end = 0; //two pointers, one point head and one tail
        int d = Integer.MAX_VALUE; //the length of substring
        int head = 0; //the selected substring head
        
        while(end < s.length()){
            
            //modify counter hear
            if(map[s.charAt(end++)]-- > 0) //If char does not exist in t, m[s[end]] will be negative
                counter--;
            
            while(counter == 0){ //counter condition
                if(end - begin < d)  //update d if find minimum
                    d = end - (head = begin);
                if(map[s.charAt(begin++)]++ == 0) //increase begin to make it invalid/valid again
                    counter++;
            }
            
        }
        
        return d == Integer.MAX_VALUE ? "" : s.substring(head, head+d);
        
    }
    
    /**
     * One thing needs to be mentioned is that when asked to find maximum substring, 
     * we should update maximum after the inner while loop to guarantee that the substring 
     * is valid. On the other hand, when asked to find minimum substring, 
     * we should update minimum inside the inner while loop.
     */
    
    /**
    int findSubstring(string s){
        vector<int> map(128,0);
        int counter; // check whether the substring is valid
        int begin=0, end=0; //two pointers, one point to tail and one  head
        int d; //the length of substring

        for() { //initialize the hash map here  }

        while(end<s.size()){

            if(map[s[end++]]-- ?){  // modify counter here  }

            while(// counter condition ){ 
                 
                // update d here if finding minimum

                //increase begin to make it invalid/valid again
                
                if(map[s[begin++]]++ ?){ //modify counter here}
            }  

            /* update d here if finding maximum
        }
        return d;
      }*/

    public static void main(String[] args) {
        _76_MinimumWindowSubstring test = new _76_MinimumWindowSubstring();
    }

}
```
