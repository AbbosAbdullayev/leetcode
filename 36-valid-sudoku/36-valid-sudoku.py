import numpy as np
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       ### check for row
        for i in range(len(board)):
            list=[]
            for j in range(len(board)):
                if board[i][j]=='.': continue
                if board[i][j] in list:
                    return False
                list.append(board[i][j])
        ### check for column
        for i in range(len(board)):
            list=[]
            for j in range(len(board)):
                if board[j][i]=='.': continue
                if board[j][i] in list:
                    return False
                list.append(board[j][i])   
        ### check for 3X3 Box     
        for i in range(0,len(board)-2,3):
            for j in range(0,len(board)-2,3):
                        #b_part=board[i-3:i,j-3:j]
                        list=[]
                        for m in range(3):
                            for n in range(3):
                                if board[i+m][j+n]=='.': continue
                                if board[i+m][j+n] in list:
                                    return False
                                list.append(board[i+m][j+n])  
        return True                                                     