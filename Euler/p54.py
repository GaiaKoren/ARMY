def get_rank(hand):
    if is_royal_flush(hand):
        return 1
    elif is_consecutive(hand) and is_same_suit(hand):
        return 2
    elif 4 in get_reps(turn_to_nums(hand)).values():
        return 3
    elif 3 in get_reps(turn_to_nums(hand)).values() and 2 in get_reps(turn_to_nums(hand)).values():
        return 4
    elif is_same_suit(hand):
        return 5
    elif is_consecutive(hand):
        return 6
    elif 3 in get_reps(turn_to_nums(hand)).values():
        return 7
    elif is_two_pairs(hand):
        return 8
    elif 2 in get_reps(turn_to_nums(hand)).values():
        return 9
    else:
        return 10


def declare_winner(hand1, hand2):
    rank1 = get_rank(hand1)
    rank2 = get_rank(hand2)
    if rank1 < rank2:
        return 1
    elif rank2 < rank1:
        return 0
    else:
        return comp_with_mults(turn_to_nums(hand1), turn_to_nums(hand2))
        
    




def turn_to_nums(hand):
    res = []
    order = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    for card in hand:
        res.append(order.index(card[0]))
    return res



def get_max(hand):
    nums_hand = turn_to_nums(hand)
    m = 0
    for card in nums_hand:
        m = max(card, m)
    return m + 2

def get_max(hand):
    nums_hand = turn_to_nums(hand)
    m = 0
    for card in nums_hand:
        m = max(card, m)
    return m

def comp_max(hand1, hand2):
    max1 = get_max(hand1)
    max2 = get_max(hand2)
    if max1 > max2:
        return 1
    elif max1 == max2:
        hand1.remove(max1)
        hand2.remove(max1)
        return comp_max(hand1, hand2)
    return 0

def is_two_pairs(hand):
    dic = get_reps(turn_to_nums(hand))
    c = 0
    for val in dic.values():
        if val == 2:
            c += 1
    return c == 2

def is_same_suit(hand):
    suit = hand[0][1]
    for card in hand:
        if card[1] != suit:
            return False
    return True

def is_consecutive(hand):
    nums_hand = turn_to_nums(hand)
    mergeSort(nums_hand)
    prev = nums_hand[0]
    i = 1
    while i < 5:
        curr = nums_hand[i]
        if curr - prev != 1:
            return False
        prev = curr
        i += 1
    return True



def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]
        mergeSort(left)
        mergeSort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                myList[k] = left[i]
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1


def get_reps(hand):
    res_dic = {}
    for card in hand:
        num = card
        if res_dic.get(num) is None:
            res_dic[num] = 1
        else:
            res_dic[num] += 1
    return res_dic

def is_royal_flush(hand):
    if is_same_suit(hand) and get_max(hand) == 14 and is_consecutive(hand):
        return True
    return False


def comp_with_mults(hand1_nums, hand2_nums):
    dic1 = get_reps(hand1_nums)
    dic1_val = 0
    m1 = 0
    for key in dic1.keys():
        if dic1[key] > dic1_val:
            dic1_val = dic1[key]
            m1 = key
        elif dic1[key] == dic1_val:
            if key > m1:
                m1 = key
    dic2 = get_reps(hand2_nums)
    dic2_val = 0
    m2 = 0
    for key in dic2.keys():
        if dic2[key] > dic2_val:
            dic2_val = dic2[key]
            m2 = key
        elif dic2[key] == dic2_val:
            if key > m2:
                m2 = key
    if m1 > m2:
        return 1
    elif m1 < m2:
        return 0
    else:
        hand1_nums = remove_all(hand1_nums, m1, dic1_val)
        hand2_nums = remove_all(hand2_nums, m2, dic2_val)
        return comp_with_mults(hand1_nums, hand2_nums)

def remove_all(hand, num, c):
    for i in range(0, c):
        hand.remove(num)
    return hand



def parse(file):
    file_op = open(file, "r")
    file_str = file_op.read()
    lines = file_str.split("\n")
    return lines[0:-1]

def poker_hands(file):
    c = 0
    matches = parse(file)
    for match in matches:
        cards = match.split(" ")
        hand1 = cards[:5]
        hand2 = cards[5:]
        print(hand1, hand2, declare_winner(hand1, hand2))
        c += declare_winner(hand1, hand2)
    return c

print(declare_winner(['5S', '5D', 'JC', 'QH', '2D'], ['KS', '8H', 'QS', '2H', 'TS']))

print(get_rank(['5S', '5D', 'JC', 'QH', '2D']))
print(get_rank(['KS', '8H', 'QS', '2H', 'TS']))

FILE = r"C:\Users\princess\Downloads\p054_poker.txt"






print(poker_hands(FILE))







