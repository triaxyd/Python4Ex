#Έστω ένα τετράγωνο 3*3 στο οποίο τοποθετείτε “καπάκια”.
#Έχετε στην κατοχή σας 27 “καπάκια”, 9 για κάθε μέγεθος
#(μικρό, μεσαίο, μεγάλο). Μια τριάδα που τερματίζει το
#παιχίνδι γίνεται οριζόντια, κάθετα ή διαγώνια. Η τριάδα
#αποτελείται από καπάκια είτε του ίδιου μεγέθους είτε από
#το μικρό προς το μεγαλύτερο. Επειδή έχετε καπάκια, ένα
#καπάκι μπορεί να μπει σε οποιοδήποτε τετράγωνο, αρκεί να
#είναι ελεύθερο ή να υπάρχει εκεί μικρότερο καπάκι.
#Γράψτε ένα πρόγραμμα το οποίο παίζει τυχαία το παιχνίδι
#100 φορές και επιστρέφει το μέσο όρο των βημάτων για να λήξει το παιχνίδι.


from random import randrange
import random

sumtries=0
MO=0
for k in range(100):
    triada=0
    kapakia=[]
    for j in range (9):             #27 kapakia small,medium,large
        kapakia.append(1)
    for j in range (9):
        kapakia.append(2)
    for j in range (9):
        kapakia.append(3)
    random.shuffle(kapakia)
    board=[]
    for i in range(3):
        board.append([])
        for j in range (3):
            board[i].append(0)               #dimiourgia board
    while triada==0 and len(kapakia)>0:              #epanalispi topothetisi kapakia
        grammi=randrange(3)               #random grammi (1-3)
        thesikap=randrange(3)            #random thesi grammi (1-3)
        if board[grammi][thesikap]==0 or kapakia[-1]>board[grammi][thesikap]:       #elegxos topothetisis
            board[grammi].remove(board[grammi][thesikap])
            board[grammi].insert(thesikap,kapakia.pop())
            if board[grammi][0]!=0 and board[grammi][1]!=0 and board[grammi][2]!=0:         #elegxos gia triada orizontia
                if sorted(board[grammi])==board[grammi] or sorted(board[grammi],reverse=True)==board[grammi]:
                    triada=1
            if board[0][thesikap]!=0 and board[1][thesikap]!=0 and board[2][thesikap]!=0:            #elegxos gia triada katheta
                temp=[]
                temp.append(board[0][thesikap])
                temp.append(board[1][thesikap])
                temp.append(board[2][thesikap])
                if sorted(temp)==temp or sorted(temp,reverse=True)==temp:
                    triada=1
            if grammi==1 and thesikap==1:                   #elegxos gia triada diagwnia
                if board[0][0]!=0 and board[2][2]!=0:        #elegxos an einai to kentriko keli
                    temp=[]
                    temp.append(board[0][0])
                    temp.append(board[1][1])
                    temp.append(board[2][2])
                    if sorted(temp)==temp or sorted(temp,reverse=True)==temp:
                        triada=1
                if board[0][2]!=0 and board[2][0]!=0:
                    temp=[]
                    temp.append(board[0][2])
                    temp.append(board[1][1])
                    temp.append(board[2][0])
                    if sorted(temp)==temp or sorted(temp,reverse=True)==temp:
                        triada=1
            if grammi==0:                       #elegxos an einai proti grammi kai theseis 0,2
                if thesikap==0:
                    if board[1][1]!=0 and board[2][2]!=0:
                        temp=[]
                        temp.append(board[0][0])
                        temp.append(board[1][1])
                        temp.append(board[2][2])
                        if sorted(temp)==temp or sorted(temp,reverse=True)==temp:
                            triada=1
                if thesikap==2:
                    if board[1][1]!=0 and board[2][0]!=0:
                        temp=[]
                        temp.append(board[0][2])
                        temp.append(board[1][1])
                        temp.append(board[2][0])
                        if sorted(temp)==temp or sorted(temp,reverse=True)==temp:
                            triada=1
            elif grammi==2:                     #elegxos an einai triti grammi kai theseis 0,2
                if thesikap==0:
                    if board[1][1]!=0 and board[0][2]!=0:
                        temp=[]
                        temp.append(board[2][0])
                        temp.append(board[1][1])
                        temp.append(board[0][2])
                        if sorted(temp)==temp or sorted(temp,reverse=True)==temp:
                            triada=1
                if thesikap==2:
                    if board[1][1]!=0 and board[0][0]!=0:
                        temp=[]
                        temp.append(board[2][2])
                        temp.append(board[1][1])
                        temp.append(board[0][0])
                        if sorted(temp)==temp or sorted(temp,reverse=True)==temp:
                            triada=1
        sumtries+=1
MO=sumtries/100
print("**********")
print("\nΜΕΣΟΣ ΟΡΟΣ ΒΗΜΑΤΩΝ ΟΛΩΝ ΤΩΝ ΠΑΙΧΝΙΔΙΩΝ: ",int(MO),"\n")
print("**********")
