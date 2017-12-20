---
layout: post
title: 36. Valid Sudoku       
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java
import java.util.HashSet;
import java.util.Set;

public class _36_ValidSudoku {
    //今次判断每一行每一列以及每一个九宫格
    public boolean isValidSudoku(char[][] board){
        if(board == null) return false;
        
        Set<Integer> row = new HashSet<Integer>();
        Set<Integer> col = new HashSet<Integer>();
        Set<Integer> cube = new HashSet<Integer>();
        
        for(int i = 0; i < 9; i++){
            row.clear();
            col.clear();
            cube.clear();//可以考虑将三个set直接放入这里当作局部变量，可能比clear耗时要短，但空间开销大一些
            for(int j = 0; j < 9; j++){
                if(board[i][j] != '.' && !row.add(board[i][j]-'0'))
                    return false;
                if(board[j][i] != '.' && !col.add(board[j][i]-'0'))
                    return false;
                int rowi = i/3*3;
                int coli = i%3*3;
                if(board[rowi+j/3][coli+j%3] != '.' && !cube.add(board[rowi+j/3][coli+j%3]-'0'))
                    return false;
            }
        }
        
        return true;
    }

    public static void main(String[] args) {
        _36_ValidSudoku test = new _36_ValidSudoku();
        String[] s = new String[]{".........","......3..","...18....","...7.....","....1.97.",".........","...36.1..",".........",".......2."};
        char[][] d = new char[9][9];
        for(int i = 0; i < 9; i++){
            d[i] = s[i].toCharArray();
        }
        System.out.println(test.isValidSudoku(d));
    }

}
```
