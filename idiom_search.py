from itertools import combinations as cb

with open('d:\\idiom.txt','r') as f:
    idioms=set(map(lambda x: x.strip(), f.readlines()))

keyWordList=input(':')
for keyWord in cb(keyWordList, 4):
    result=idioms
    for kc in keyWord:
        result=set([idiom for idiom in result if kc in idiom])
        if len(result)==0:
            break
    for idiom in result:
        print(idiom)
print('end')
