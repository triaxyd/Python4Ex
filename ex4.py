#Χρησιμοποιείστε τον κώδικα που έχουμε φτιάξει για “21” (card game) και
#υπολογίστε σε πόσα από τα 100 παιχνίδια κερδίζει ο πρώτος παίκτης, σε πόσα
#ο δεύτερος, και σε πόσα έχουμε ισοπαλία. Στην συνέχεια, πειράξτε το
#μοίρασμα ώστε ο πρώτος παίκτης να ξεκινάει με 10 ή φιγούρα (J,Q, K)
#και ο δεύτερος ποτέ με 10 ή φιγούρα. Υπολογίστε τα νέα στατιστικά
#για 100 τυχαία παιχνίδια, δηλαδή πόσα κερδίζει ο πρώτος παίκτης,
#πόσα ο δεύτερος, και σε πόσα έχουμε ισοπαλία. Κάθε φορά το μοίρασμα
#των χαρτιών γίνεται από την αρχή και ανακατεύεται η τράπουλα.

import random

w1=0
w2=0
wd=0
for l in range (100):
    xartia = []
    figures = ["J", "Q", "K"]
    xarti = [i for i in range(1, 11)] + figures
    color = ["H", "S", "C", "D"]
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    random.shuffle(xartia)
    player1=[]
    sum1=0
    while sum1<16:
        sum1=0
        player1.append(xartia.pop())
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
    if sum1>21:
        w2+=1
    else:
        player2=[]
        sum2=0
        while sum2<16:
            sum2=0
            player2.append(xartia.pop())
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
        if sum2>21:
            sum2=0
        if sum1>sum2:
            w1+=1
        elif sum2>sum1:
            w2+=1
        else:
            wd+=1
print("****************************************")
print("---ΚΑΝΟΝΙΚΟ ΠΑΙΧΝΙΔΙ---")
print ("Ο παίκτης 1 κέρδισε:",w1,"φορές.")
print ("Ο παίκτης 2 κέρδισε:",w2,"φορές.")
print ("Δεν υπήρξε νικητής:",wd,"φορές.\n")



w1=0
w2=0
wd=0
for l in range (100):
    xartia = []
    figures = ["J", "Q", "K"]
    xarti = [i for i in range(1, 11)] + figures
    color = ["H", "S", "C", "D"]
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    random.shuffle(xartia)
    fixed=[]
    for i in xartia:
        for j in figures:
            if i[0]==10 or i[0]==j:
                if i not in fixed:
                    fixed.append(i)   #fixed me 10 kai figoures
    player1=[]
    sum1=0
    player1.append(fixed.pop())      #1o xarti fixed ston player1
    for i in player1:
        xartia.remove(i)         #afairesi apo xartia to fixed xarti
    while sum1<16:
        sum1=0
        player1.append(xartia.pop())
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
    if sum1>21:
        w2+=1
    else:
        player2=[]
        fixed.clear()
        for i in xartia:
            if i[0]!=10 and i[0]!="K" and i[0]!="J" and i[0]!="Q":  #fixed xoris 10 kai figoures
                fixed.append(i)
        for i in player1:
            if i in fixed:
                fixed.remove(i)
        player2.append(fixed.pop())             #1o xarti fixed ston player2
        for i in player2:
            xartia.remove(i)
        sum2=0
        while sum2<16:
            sum2=0
            player2.append(xartia.pop())
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
        if sum2>21:
            sum2=0
        if sum1>sum2:
            w1+=1
        elif sum2>sum1:
            w2+=1
        else:
            wd+=1
print("---FIXED---")
print ("Ο παίκτης 1 κέρδισε:",w1,"φορές.")
print ("Ο παίκτης 2 κέρδισε:",w2,"φορές.")
print ("Δεν υπήρξε νικητής:",wd,"φορές.")
print("****************************************")
