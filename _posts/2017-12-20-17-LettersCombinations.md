---
layout: post
title: 17. Letter Combinations of a Phone Number       
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

/**
 * 
 * @author liujing
 *
 */
public class _17_LettersCombinations {
    private static final char[][] map;
    static {
        map = new char[][] { {}, {}, { 'a', 'b', 'c' }, { 'd', 'e', 'f' }, { 'g', 'h', 'i' }, { 'j', 'k', 'l' },
                { 'm', 'n', 'o' }, { 'p', 'q', 'r', 's' }, { 't', 'u', 'v' }, { 'w', 'x', 'y', 'z' } };
    }

    public static List<String> letterCombinations(String digits) {
        if (digits == null || digits.length() == 0) {
            return Arrays.asList();
        }
        List<String> res = new ArrayList<String>();
        res.add("");
        char[] c = digits.toCharArray();
        for (int i = 0; i < c.length; i++) {
            res = combine(map[c[i] - '0'], res);
        }
        return res;
    }

    public static List<String> combine(char[] m, List<String> l) {
        List<String> res = new ArrayList<String>();
        for (int i = 0; i < m.length; i++) {
            for (String x : l) {
                res.add(x + m[i]);
            }
        }
        return res;
    }

    // BFS
    public static List<String> letterCombinations1(String digits) {
        if (digits == null || digits.length() == 0) {
            return Arrays.asList();
        }
        LinkedList<String> res = new LinkedList<String>();
        res.add("");
        for (int i = 0; i < digits.length(); i++) {
            int x = digits.charAt(i) - '0';
            while (res.peek().length() == i) {
                String t = res.remove();
                for (char c : map[x]) {
                    res.add(t + c);
                }
            }
        }
        return res;
    }

    // DFS
    public static List<String> letterCombinations2(String digits) {
        if (digits == null || digits.length() == 0) {
            return Arrays.asList();
        }

        List<String> res = new ArrayList<String>();
        // dfs(digits, 0, "", res);
        LinkedList<String> stack = new LinkedList<String>();
        stack.push("");
        while (stack.size() != 0) {
            if(stack.peek().length() == digits.length()){
                res.add(stack.remove());
                continue;
            }
            for (int i = stack.peek().length(); i < digits.length(); i++) {
                String top = stack.remove();
                for (int j = 0; j < map[digits.charAt(i)-'0'].length; j++) {
                    stack.push(top + map[digits.charAt(i)-'0'][j]);
                }
            }

        }

        return res;
    }

    public static void dfs(String digits, int idx, String path, List<String> res) {
        if (idx == digits.length()) {
            res.add(path);
            return;
        }
        for (char c : map[digits.charAt(idx) - '0']) {
            dfs(digits, idx + 1, path + c, res);
        }
        return;
    }

    public static void main(String[] args) {

        System.out.println(letterCombinations2("23"));
    }

}
```
