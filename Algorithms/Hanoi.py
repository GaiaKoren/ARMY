A = [1, 2]
B = []
C = []

def Hanoi(n, source, dest, mid):
    if n == 1:
        print("Move disk 1 from source:", source, "to destination", dest)
        return
    Hanoi(n-1, "A", "C", "B")
    print("Move disk", n,"from source", source, "to destination", dest)
    Hanoi(n - 1, "C", "B", "A")



def move(list1, list2):
    to_move = list1[len(list1) - 2]
    list2.append(to_move)
    list1.remove(to_move)


Hanoi(10, "A", "B", "C")


