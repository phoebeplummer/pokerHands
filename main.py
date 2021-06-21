# PROJECT EULER PROBLEM 54 POKER HANDS
# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

# function to check for royal flush
def royalFlush(hand):
    # seperate hand into values and suits
    value = [hand[0], hand[3], hand[6], hand[9], hand[12]]
    suit = [hand[1], hand[4], hand[7], hand[10], hand[13]]
    # check all values for royal flush are present
    if 'T' in value and 'J' in value and 'Q' in value and 'K' in value and 'A' in value:
        # check suits are all the same
        if suit[0] == suit[1] == suit[2] == suit[3] == suit[4]:
            return True
        else:
            return False
    else:
        return False


# function to check for straight flush
def straightFlush(hand):
    # seperate hand into values and suits
    value = [hand[0], hand[3], hand[6], hand[9], hand[12]]
    suit = [hand[1], hand[4], hand[7], hand[10], hand[13]]
    # create blank array to reorder values
    orderVal = []
    order = ["2", "3", "4", "5", "6", "7", "8", "9", 'T', 'J', 'Q', 'K', 'A']
    # check suits are all the same
    if suit[0] == suit[1] == suit[2] == suit[3] == suit[4]:
        SF = True
        # reorder values so they are in ascending order
        count = 0
        lowestIdx = 100
        while count < 5:
            for x in value:
                idx = order.index(x)
                if idx < lowestIdx:
                    lowestIdx = idx
                    lowestVal = x
            orderVal.append(lowestVal)
            value.remove(lowestVal)
            lowestIdx = 100
            count += 1
        # check that values are consecutive
        count = 0
        while count < 4 and SF == True:
            ordIdx = order.index(orderVal[count])
            if order.index(orderVal[count + 1]) != (ordIdx + 1):
                return False, 0
            count += 1
    else:
        return False, 0
    highest = order.index(orderVal[4]) + 2
    return True,  highest

# function to check for four of a kind
def fourKind(hand):
    # get values of hand
    value = [hand[0], hand[3], hand[6], hand[9], hand[12]]
    order = ["2", "3", "4", "5", "6", "7", "8", "9", 'T', 'J', 'Q', 'K', 'A']
    count = 0
    # check if there are 4 occurrences of same value
    while count < 2:
        if value.count(value[count]) == 4:
            highest = order.index(value[count]) + 2
            return True , highest
        count += 1
    return False, 0

# function to check for full house
def fullHouse(hand):
    # get values of hand
    value = [hand[0], hand[3], hand[6], hand[9], hand[12]]
    order = ["2", "3", "4", "5", "6", "7", "8", "9", 'T', 'J', 'Q', 'K', 'A']
    occur3 = False
    count = 0
    # check if there are 3 occurrences of same vale
    while count < 4 and occur3 == False:
        if value.count(value[count]) == 3:
            occur3 = True
            val = value[count]
        count += 1
    if occur3 == True:
        # remove value that appears 3 times from value list
        for i in range(3):
            value.remove(val)
        # check if two remaining values are equal
        if value[0] == value[1]:
            highest1 = order.index(val) + 2
            highest2 = order.index(value[0]) + 2
            return True, highest1, highest2
        # return false if not a full house
        else:
            return False, 0, 0
    else:
        return False, 0, 0


#function to check for flush
def flush(hand):
    # make array of suits and values
    suit = [hand[1], hand[4], hand[7], hand[10], hand[13]]
    value = [hand[0], hand[3], hand[6], hand[9], hand[12]]
    # initialise array of correct order and set highest idx to low number
    order = ["2", "3", "4", "5", "6", "7", "8", "9", 'T', 'J', 'Q', 'K', 'A']
    highestIdx = -1
    # ensure all cards are same suit
    if suit[0] == suit[1] == suit[2] == suit[3] == suit[4]:
    # find highest card
        for i in value:
            if order.index(i) > highestIdx:
                highestIdx = order.index(i)
        highest = highestIdx + 2
        return True, highest
    else:
        return False, 0

#function to check for stright
def straight(hand):
    #get values of hand
    value = [hand[0], hand[3], hand[6], hand[9], hand[12]]
    # create blank array to reorder values
    orderVal = []
    order = ["2", "3", "4", "5", "6", "7", "8", "9", 'T', 'J', 'Q', 'K', 'A']
    # reorder values so they are in ascending order
    count = 0
    lowestIdx = 100
    while count < 5:
        for x in value:
            idx = order.index(x)
            if idx < lowestIdx:
                lowestIdx = idx
                lowestVal = x
        orderVal.append(lowestVal)
        value.remove(lowestVal)
        lowestIdx = 100
        count += 1
    # check that values are consecutive
    count = 0
    while count < 4:
        ordIdx = order.index(orderVal[count])
        if order.index(orderVal[count + 1]) != (ordIdx + 1):
            return False, 0
        count += 1
    highest = order.index(orderVal[4]) + 2
    return True, highest

# function to check for three of a kind
def threeKind(hand):
    # get values of hand
    value = [hand[0], hand[3], hand[6], hand[9], hand[12]]
    order = ["2", "3", "4", "5", "6", "7", "8", "9", 'T', 'J', 'Q', 'K', 'A']
    count = 0
    # check if there are 3 occurrences of same value
    while count < 3:
        if value.count(value[count]) == 3:
            highest = order.index(value[count]) + 2
            return True, highest
        count += 1
    return False, 0

#function to check for two pairs
def twoPairs(hand):
    # get values of hand
    value = [hand[0], hand[3], hand[6], hand[9], hand[12]]
    order = ["2", "3", "4", "5", "6", "7", "8", "9", 'T', 'J', 'Q', 'K', 'A']
    # initialise variables
    count1 = 0
    count2 = 0
    pair = False
    # check for 1st pair
    while count1 < 4 and pair == False:
        if value.count(value[count1]) == 2:
            val = value[count1]
            pair = True
            # remove pair from list
            for i in range(2):
                value.remove(val)
            # look for 2nd pair
            while count2 < 2:
                if value.count(value[count2]) == 2:
                    idxPair1 = order.index(val) + 2
                    idxPair2 = order.index(value[count2]) + 2
                    if idxPair1 > idxPair2:
                        highest1 = idxPair1
                        highest2 = idxPair2
                    else:
                        highest1 = idxPair2
                        highest2 = idxPair1
                    return True, highest1, highest2
                count2 += 1
        count1 += 1
    return False, 0, 0

# function to check for one pair
def onePair(hand):
    # get values of hand
    value = [hand[0], hand[3], hand[6], hand[9], hand[12]]
    order = ["2", "3", "4", "5", "6", "7", "8", "9", 'T', 'J', 'Q', 'K', 'A']
    count = 0
    while count < 4:
        #check if value has a pair in hand
        if value.count(value[count]) == 2:
            highest = order.index(value[count]) + 2
            return True, highest
        count += 1
    return False, 0

# function to find highest card in hand
def highCard(hand, removeVal):
    # get values of hand
    global value
    value = [hand[0], hand[3], hand[6], hand[9], hand[12]]
    # remove value if two highest cards of players match and next highest must be checked
    if removeVal != 0:
    # use for loop to remove all instances of high card
        for i in range (value.count(removeVal)):
            value.remove(removeVal)
    # initialise highest idx variable
    highestIdx = -1
    order = ["2", "3", "4", "5", "6", "7", "8", "9", 'T', 'J', 'Q', 'K', 'A']
    # find highest value in hand
    for i in value:
        if order.index(i) > highestIdx:
            highestIdx = order.index(i)
    highest = highestIdx + 2
    return highest

# import hand file
hands = open("/Users/phoebeplummer/Desktop/poker.txt", "r")
rounds = []
# create total scores for player one and two
total1 = 0
total2 = 0
# sepearate hands into rounds
for i in hands:
    i = i[0:29]
    rounds.append(i)

for x in rounds:
    score1 = 0
    score2 = 0
    # separate rounds into player 1 and player 2 hands
    player1 = x[0:14]
    player2 = x[15:29]

    # find ranking for player 1's hand
    # highest1 is the value of the card to be examined if rankings are the same highest11 will be checked first
    # then highest 12 in the event that they are also equal
    if royalFlush(player1) == True:
        score1 += 10
    elif straightFlush(player1)[0] == True:
        score1 += 9
        highest1 = straightFlush(player1)[1]
    elif fourKind(player1)[0] == True:
        score1 += 8
        highest1 = fourKind(player1)[1]
    elif fullHouse(player1)[0] == True:
        score1 += 7
        highest11 = fullHouse(player1)[1]
        highest12 = fullHouse(player1)[2]
    elif flush(player1)[0] == True:
        score1 += 6
        highest1 = flush(player1)[1]
    elif straight(player1)[0] == True:
        score1 += 5
        highest1 = straight(player1)[1]
    elif threeKind(player1)[0] == True:
        score1 += 4
        highest1 = threeKind(player1)[1]
    elif twoPairs(player1)[0] == True:
        score1 += 3
        highest11 = twoPairs(player1)[1]
        highest12 = twoPairs(player1)[2]
    elif onePair(player1)[0] == True:
        score1 += 2
        highest1 = onePair(player1)[1]
    else:
        highest1 = highCard(player1, 0)
        score1 = 1

    # find ranking for player 2's hand
    if royalFlush(player2) == True:
        score2 += 10
    elif straightFlush(player2)[0] == True:
        score2 += 9
        highest2 = straightFlush(player2)[1]
    elif fourKind(player2)[0] == True:
        score2 += 8
        highest2 = fourKind(player2)[1]
    elif fullHouse(player2)[0] == True:
        score2 += 7
        highest21 = fullHouse(player2)[1]
        highest22 = fullHouse(player2)[2]
    elif flush(player2)[0] == True:
        score2 += 6
        highest2 = flush(player2)[1]
    elif straight(player2)[0] == True:
        score2 += 5
        highest2 = straight(player2)[1]
    elif threeKind(player2)[0] == True:
        score2 += 4
        highest2 = threeKind(player2)[1]
    elif twoPairs(player2)[0] == True:
        score2 += 3
        highest21 = twoPairs(player2)[1]
        highest22 = twoPairs(player2)[2]
    elif onePair(player2)[0] == True:
        score2 += 2
        highest2 = onePair(player2)[1]
    else:
        highest2 = highCard(player2, 0)
        score2 = 1

    # compare player 1 and player 2 ranking
    # if player 1 has the higher ranking they have won this round
    if score1 > score2:
        total1 += 1
    # if player 2 has the higher ranking then they have won
    elif score2 > score1:
        total2 += 1
    # if rankings are equal then highest card must be examined
    else:
        # for rankings where there is one val to be compared
        if score1 == 9 or score1 == 8 or score1 == 6 or score1 == 5 or score1 == 4 or score1 == 2 or score1 == 1:
            # if highest cards are equal find the next highest card
            while highest1 == highest2:
                highest1 = highCard(player1, highest1)
                highest2 = highCard(player2, highest2)
            # if player 1 has higher card then add to player 1s score
            if highest1 > highest2:
                total1 += 1
            # if player 2 has higher card then add to player 2s score
            elif highest2 > highest1:
                total2 += 1
        # for rankings where there are two vals to be examined
        elif score1 ==7 or score2 == 3:
            # if player 1 has higher card then add to player 1s score
            if highest11 > highest21:
                total1 += 1
            # if player 2 has higher card then add to player 2s score
            elif highest21 > highest11:
                total2 += 1
            else:
                # if high cards are equal find the next highest card
                while highest12 == highest22:
                    highest12 = highCard(player1, highest12)
                    highest22 = highCard(player2, highest22)
                # if player 1 has higher card then add to player 1s score
                if highest21 > highest22:
                    total1 += 1
                # if player 2 has higher card then add to player 2s score
                else:
                    total2 += 1

print("total score for player 1: ", total1)
print("total score for player 2: ", total2)
if total1 > total2:
    print("player 1 wins")
elif total2 > total1:
    print("player 2 wins")
else:
    print("it's a draw")
