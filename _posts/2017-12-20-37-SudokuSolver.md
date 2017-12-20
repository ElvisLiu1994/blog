---
layout: post
title: 37. Sudoku Solver  
date: 2017-12-20
category: LeetCode
tag: algorithm
---

* content
{:toc}


```java

public class _37_SudokuSolver {
    
    public void solveSudoku(char[][] board){
        if(board == null || board.length == 0)
            return;
        solve(board);
    }
    //关键在于回溯法的实现，使用递归来进行实现；时间复杂度为指数复杂度O(9^m),m为所有的空格数
    public boolean solve(char[][] board){
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[0].length; j++){
                if(board[i][j] == '.'){
                    for(char c = '1'; c <= '9'; c++){//分别尝试1到9
                        if(isValid(board,i,j,c)){
                            board[i][j] = c;
                            
                            if(solve(board))//递归调用该函数来填写剩下的空格
                                return true;//已经得到答案
                            else
                                board[i][j] = '.';//否则进行回溯
                        }
                    }
                    
                    return false;//尝试9个数都不可以则返回false
                }
            }
        }
        return true;//如果没有空格了，则返回true
    }
    
    private boolean isValid(char[][] board, int row, int col, char c){
        for(int i = 0; i < 9; i++){
            if(board[i][col] != '.' && board[i][col] == c) return false;
            if(board[row][i] != '.' && board[row][i] == c) return false;
            if(board[row/3*3+i/3][col/3*3+i%3] != '.' && board[row/3*3+i/3][col/3*3+i%3] == c)
                return false;
        }
        return true;
    }

    public static void main(String[] args) {
        _37_SudokuSolver test = new _37_SudokuSolver();
    }

}
```
