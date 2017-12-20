---
layout: post
title: 10. Regular Expression Matching  
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
/**
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
 * @author liujing
 *
 */
public class _10_RegularExpressionMatching {
    
    public boolean isMatch(String s, String p) {
        
        if(!p.isEmpty() && p.charAt(0)=='*')//invalid p
            return false;
        
        int m = s.length(), n = p.length();
        boolean[][] dp = new boolean[m+1][n+1]; 
        //initial
        dp[0][0] = true;//s和p均为空时，匹配结果为true,其他的均默认初始为false了
        //dp[i][0] where i>0 表示p为空串时，s不为空串，这属于不匹配的情况，默认初始化为false
        //dp[0][i] where i>0 表示s为空串时，p不为空串，这里的初始化内容由下面代码实现
        for(int i = 1; i < n; i += 2){//这里可以用i++，但是作用和i+=2是一样的
            //这里s为空串，所以当p的个数为奇数时，肯定匹配结果为false(因为只有X*两个字符才能表示空串，
            //其中X表示任意字符)，所以只需要初始化偶数位置的dp值
            if(p.charAt(i) == '*')
                dp[0][i+1] = dp[0][i-1];
        }
        
        for(int i = 1; i <= m; i++){
            for(int j = 1; j <= n; j++){
                //p.charAt(j-1)表示当前考察的第j个字符，s.charAt(i-1)表示当前考察的第i个字符
                //若当前p中第j个字符不是'*'，那么需要s的前i-1个字符与p的前j-1个字符匹配，
                //同时s的第i个与p的第j个字符要匹配，这里匹配可以是相等，可以是p为'.'；
                if(p.charAt(j-1) != '*')
                    dp[i][j] = dp[i-1][j-1] && (s.charAt(i-1) == p.charAt(j-1) || '.'==p.charAt(j-1));
                //若当前p的第j个字符为'*'，这里有两种情况：
                //*匹配前一个字符零次：则dp[i][j] = dp[i][j-2]
                //*匹配了至少一次：则需要s的前i-1个字符串与p的j个字符串匹配，并且s的第i个字符与p的第j-1个字符匹配，
                //同样，这里的匹配可以是相等，也可以是p为'.'
                else{
                    dp[i][j] = dp[i][j-2] || (s.charAt(i-1) == p.charAt(j-2) || '.' == p.charAt(j-2)) && dp[i-1][j];
                }
            }
        }
        return dp[m][n];
    }

    public static void main(String[] args) {
        _10_RegularExpressionMatching test = new _10_RegularExpressionMatching();
        System.out.println(test.isMatch("", ".***"));
    }

}
```
