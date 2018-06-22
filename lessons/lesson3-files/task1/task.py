
firstIndex = 0
secondIndex = 0


with open('res.txt', 'wt') as res:
    with open('num1.txt', 'rt') as f:
        with open('num2.txt', 'rt') as f2:
            for line in f:
                val = int(line)
                val2 = int(f2.readline())
                if val < val2:
                    res.write(str(val))
                    # print(val, val2)
                else:
                    res.write(str(val2))
                    # print(val2, val)

            #     for line2 in f2:
            #         val2 = int(line2)


                #
                # num1.append(int(line))
                # print(num1)



# num2 = []
# with open('num2.txt', 'rt') as f:
