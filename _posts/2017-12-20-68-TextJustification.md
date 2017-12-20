---
layout: post
title: Text Justification   			
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
import java.util.ArrayList;
import java.util.List;

/**
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
 *
 */
public class _68_TextJustification {
	
    public List<String> fullJustify(String[] words, int maxWidth) {
    	
    	List<String> res = new ArrayList<String>();
    	
    	for(int i = 0, w; i < words.length; i = w){
    		int len = -1;//最后一个单词后面的空格要减掉
    		for(w = i; w < words.length && len + words[w].length() + 1 <= maxWidth; w++)
    			len += words[w].length() + 1;
    		
    		int space = 1, extra = 0;
    		if(w != i+1 && w != words.length){ // not 1 char, not last line
    			space = (maxWidth - len) / (w - 1 - i) + 1;
    			extra = (maxWidth - len) % (w - 1 - i);
    		}
    		
    		StringBuilder sb = new StringBuilder(words[i]);
    		for(int j = i + 1; j < w; j++){
    			for(int s = 0; s < space; s++) sb.append(' ');
    			if(extra-- > 0) sb.append(' ');
    			sb.append(words[j]);
    		}
    		
    		int strLen = maxWidth - sb.length();
    		while(strLen-- > 0) sb.append(' ');
    		res.add(sb.toString());
    	}
    	
    	return res;
    }

	public static void main(String[] args) {
		_68_TextJustification test = new _68_TextJustification();
		String[] words = new String[]{"This", "is", "an", "example", "of", "text", "justification."};
		String[] words1 = new String[]{""};
		for(String s : test.fullJustify(words, 14)){
			System.out.println(s);
		}
	}

}
```
