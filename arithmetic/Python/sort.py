# coding=utf-8

def bubble_sort(l):
    if l is None:
        return -1

    l_len  =len(l)

    for i in range(l_len):
        flag = False
        for j in range(l_len-1):
            if l[j]>l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
                flag = True

        if flag is False:
            break



if __name__ == '__main__':
    l = [4,5,6,1,3,2]
    bubble_sort(l)
    print(l)