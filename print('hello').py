x =  [('a', 'b', 'c'), ('b', 'd'), ('e', 'f'), ('c', 'g'), ('h', 'i', 'j'), ('f', 'k')]
def func(x):
    ans = []
    for s in x:
        sett = []
        for m in ans:
            if set(s) & m:
                sett.append(m)
        new_sett = set(s)
        ans.append(new_sett)
    return ans
print(func(x))

#my_feature分支进行的新开发内容#