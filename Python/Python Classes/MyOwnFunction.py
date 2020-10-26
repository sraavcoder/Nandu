Ask = input('Give Me A File Name ')


def CountWords(A):
    Count = 0
    f = open(A, 'r')
    lines = f.readlines()
    for i in lines:
        words = i.split()
        Count = Count+len(words)
    print(Count)


CountWords(Ask)
