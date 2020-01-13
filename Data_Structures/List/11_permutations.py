'''
created on 13/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python program to generate all permutations of list in Python
'''

def permutations(List):
    if len(List)==1:
        return [List]
    result=[]

    for i in range(len(List)):
        First=List[i]
        remain_List=List[:i]+List[i+1:]

        for perm in permutations(remain_List):
            result.append([First]+perm)
    return result

List=list(map(str,input().split()))

for perm in permutations(List):
    print(perm)
