########################################
# Challenge 166bI: Prime Factor Trees  #
#           Date: July 21, 2014        #
########################################
def factor(num):
    #i = int(num/2)+1
    i=0
    while i<num: 
        i+=1
        for x in range(i,-1,-1):
            if x*i==num:
                return(x,i)
                break
def tree(num):
    fnum = factor(num)
    resolvedFactors = [num,]
    unresolvedFactors = [fnum[0],fnum[1]]
    while 1:
        print(resolvedFactors[-1],end='') 
        fnum = factor(unresolvedFactors[-1])
  
        unresolvedFactors.extend((fnum[0],fnum[1]))
        
        resolvedFactors.append(  unresolvedFactors[0])#
        unresolvedFactors.remove(unresolvedFactors[0])#move first unresolved item to resolved
        
        print('\n+--',end='')
        if(len(resolvedFactors)>10): break
    
    return resolvedFactors
    
    
print(factor(1767150))
print(tree(1767150))







""""
60
+--30
|  |
|  +--15
|  |  |
|  |  +--5
|  |  |
|  |  |--3
|  |
|  +--2
|
+--2
"""