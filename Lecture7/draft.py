import copy
def main ():
    '''t = ([0,1,2,3], [4,5,6,7], [8,9,10,11])
    t[0].append(4)
    for i in t[0]:
        print(i)
    print (True if (1,2)>(1,1,3) else False)
    List = [x for x in range(1,10)]
    print (List,List[0:11])
    List += [x for x in range (10,20)]
    for i in List:
        print(str(i) * 2, end= " ")

    L1 = [x for x in range(1,6)]
    L2 = copy.deepcopy(L1)
    extraction= L2.pop(0)
    print(extraction)
    L2.reverse()
    L2 = [1,3,5,2,6,8,9,4,5,3,2,3,4,5,6,7]
    L2.sort()
    print(L2)
    print(L2.index(7))
    print(L2.count(7))

    Fruit = ["Banana","Apple","Pear","Orange","Grape"]
    Small_Fruit = [Funnel for Funnel in Fruit if len(Funnel)<=5 ]
    print(Small_Fruit)
 '''
    _str = 'wocao,nima,deshabi'
    _list = _str.split(",")
    print(len(_list))
    _str = '-'.join(_list)
    print(_str)

if __name__ == '__main__':
    main()