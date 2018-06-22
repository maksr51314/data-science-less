braked_dic = {
    '(': ')',
    '{': '}'
}


def braked_balanced(string, i=0, count=0):

    if i == len(string):
        return count == 0
    if count < 0:
        return False

    if string[i] in braked_dic.keys():
        # return braked_balanced(string, i + 1, count + 1, braked_dic[string[i]])
        for endIndex, stringEl in enumerate(string[::-1]):
            if stringEl in braked_dic.values():
                print(stringEl, string[i])
                if stringEl == braked_dic[string[i]]:
                    braked_balanced(string, i + 1, endIndex - 1)
                else:
                    return False


    # elif string[i] in braked_dic.values() and endBrake == string[i]:
    #     return braked_balanced(string, i + 1, count - 1)

    return braked_balanced(string, i + 1, count)


for s in ["({})"]: #, "(()", "(())", "()()", ")("
    print("{}: {}".format(s, braked_balanced(s)))
