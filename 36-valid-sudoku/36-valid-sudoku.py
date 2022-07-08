import numpy as np
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
            ninematrix=rowcol=0
            b=np.array(board)
            for i in range(b.shape[0]):
                for j in range(b.shape[1]):
                    if b[i][j]!='.':
                        if np.count_nonzero(b[i][:]==b[i][j])==1 and                                 np.count_nonzero(b[:,j]==b[i][j])==1:            
                           rowcol+=1
                          # print(rowcol)             
                    else:
                           rowcol+=1
            print(rowcol)               
            if rowcol==b.size:
                #list=[]=1
                for i in range(3,b.shape[0]+1,3):
                    for j in range(3,b.shape[1]+1,3):
                        b_part=b[i-3:i,j-3:j]
                        for m in range(3):
                            for n in range(3):
                                if (b_part[m][n]=='.' or                                                  np.count_nonzero(b_part[::]==b_part[m][n])==1):
                                    ninematrix+=1
                                    if ninematrix==b.size:
                                        return True