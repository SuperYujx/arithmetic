# coding=utf-8

def get_next(p, nexts):
    i = 0
    j = -1
    nexts[0] = -1
    while i < len(p):
        if j == -1 or p[i] == p[j]:
            i = i + 1
            j = j + 1
            nexts[i] = j
        else:
            j = nexts[j]


def my_find(s, t, nexts):
    slen = len(s)
    tlen = len(t)

    if slen == 0 or tlen == 0:
        return -1

    if slen < tlen:
        return -1

    i = 0
    j = 0
    while i < slen and j < tlen:
        if j == -1 or s[i] == t[j]:
            i = i + 1
            j = j + 1
        else:
            j = nexts[j]

    if j >= tlen:
        return i - tlen

    return -1


if __name__ == "__main__":
    s = "abababaabcbab"
    p = "abaabc"
    lens = len(p)
    nexts = [0] * (lens + 1)
    get_next(p, nexts)
    print("next数组为：" + str(nexts[0])),
    i = 1
    while i < lens - 1:
        print("," + str(nexts[i])),
        i = i + 1
    print('\n')
    print("匹配结果为：" + str(my_find(s, p, nexts)))
