res = []
col = []
pos = []
neg = []
def solution(n):
    board  = [['.']*n for i in range(n)]
    def back(r):
        if r==n:
            l = "".join()