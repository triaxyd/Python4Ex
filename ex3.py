#Σας δίνεται ένα αρχείο κειμένου το οποίο έχει μόνο ASCII χαρακτήρες.
#Αρχικά, κάντε την κατάλληλη επεξεργασία ώστε να σας μείνει κείμενο με
#μόνο γράμματα και τον κενό χαρακτήρα (space). Χωρείστε αυτό το κείμενο
#σε λέξεις σύμφωνα με το κενό και ξεκινείστε να αφαιρείτε ζευγάρια λέξεων
#αν το άθροισμα των γραμμάτων τους είναι 20. Βγάλτε τα στατιστικά για το μήκος
#των λέξεων που έμειναν, πχ. 10 λέξεις του ενός γράμματος, 12 λέξεις των 2 γραμμάτων, 3 λέξεις των 3 γραμμάτων κτλ.
#Τα ζεύγη δεν χρειάζεται να είναι από συνεχόμενες λέξεις.


with open('tc.txt','r') as f:
    keim=f.read()
    kef=keim.upper()
    output = ''.join([i if ord(i) > 64 and ord(i) < 91 or ord(i)==32 else '' for i in kef])
    lekseis=output.split()
    for lek in lekseis:
        zeug=False
        i=0
        while zeug==False and i<len(lekseis):
            if len(lek)+len(lekseis[i])==20:
                zeug=True
                lekseis.remove(lek)
                lekseis.remove(lekseis[i])
            i+=1
    for i in range(1,30):
        sum=0
        for lek in lekseis:
            if len(lek)==i:
                sum+=1
        if sum>0:
            print("Γράμματα:",i,"---Λέξεις:",sum)
