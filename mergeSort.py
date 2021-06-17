def merge (left ,right):
    res =[]
    while len(left)>0 or len(right):
        if (len(left))>0 and len(right)>0:
            if left[0]<=right[0]:
                res.append(left[0])
                left= left[1:]
            else :
                res.append(right[0])
                right=right[1:]
        elif len(left)==0 :
            res.extend(right)
            break
        else :
            res.extend(left)
            break
        print("result :",res)
    return res


print (merge([1,3,8,9,6,3],[4,9,10,82,96,100]))



#recursion

def merge_sort (xlist):
    if len(xlist)<=1 :
        return xlist
    left =xlist[:len(xlist)//2]
    right =xlist[len(xlist)//2:]
    sorted_left =merge_sort(left)
    sorted_right= merge_sort(right)
    return merge(sorted_left,sorted_right)


print(merge_sort([-9,10,1,0,3,6,9,7,17,75,56,1000,86,32,18,71]))



# time complixity : nlogn
