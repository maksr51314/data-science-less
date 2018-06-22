# import multiprocessing as mp
# import random
# import heapq
#
# PROCESS_COUNT = 4
#
# pipes = [mp.Pipe for i in range(PROCESS_COUNT)]
# IN, OUT = 0, 1
# barrier = mp.Barrier(PROCESS_COUNT)
#
#
# def parallel_sort(i):
#     l = [random.randint(1, 30) for i in range(4)]
#     l.sort()
#
#     for j in range(PROCESS_COUNT):
#         if j % 2:
#             if i == 1:
#                 r = pipes[1][IN].recv()
#                 res = list(heapq.merge(l, r))
#                 l = res[:4]
#                 pipes[2][OUT].send(res[4:])
#                 print(i, l)
#             if i == 2:
#                 pipes[1][OUT].send(l)
#                 l = pipes[2][IN].recv()
#                 print(i, l)
#         else:
#             if i%2:
#                 pipes[i - 1][OUT].send(l)
#                 l = pipes[i][IN].recv()
#                 print(i, l)
#             else:
#                 r = pipes[i][IN].recv()
#                 res = list(heapq.merge(l, r))
#                 l = res[:4]
#                 pipes[i + 1][OUT].send(res[4:])
#                 print(i, l)
#         barrier.wait()
#
#
#
# for i in range(PROCESS_COUNT):
#     p = mp.Process(target=parallel_sort, args=(i,))
#
#     p.start()


import multiprocessing as mp
import random
import heapq

N = 4

pipes = [mp.Pipe() for i in range(N)]
IN, OUT = 0, 1
barrier = mp.Barrier(N)


def p_sort(i):
    l = [random.randint(1, 30) for i in range(4)]
    l.sort()
    #    print(i, l)
    for j in range(N):
        if j % 2:
            if i == 1:
                r = pipes[1][IN].recv()
                res = list(heapq.merge(l, r))
                l = res[:4]
                pipes[2][OUT].send(res[4:])
                print(i, l)
            if i == 2:
                pipes[1][OUT].send(l)
                l = pipes[2][IN].recv()
                print(i, l)
        else:
            if i % 2:
                pipes[i - 1][OUT].send(l)
                l = pipes[i][IN].recv()
                print(i, l)
            else:
                r = pipes[i][IN].recv()
                res = list(heapq.merge(l, r))
                l = res[:4]
                pipes[i + 1][OUT].send(res[4:])
                print(i, l)
        barrier.wait()


for i in range(N):
    p = mp.Process(target=p_sort, args=(i,))
    p.start()