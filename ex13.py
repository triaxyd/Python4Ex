#H υπηρεσία https://www.cloudflare.com/en-gb/leagueofentropy/ προσφέρει τυχαίους αριθμούς.
#Χρησιμοποιείστε αρχικά την διεύθυνση https://drand.cloudflare.com/public/latest για να πάρετε το
#τελευταίο randomness το οποίο θα το χωρίσετε σε δυάδες δεκαεξαδικών χαρακτήρων, και κάθε μια θα την μετρέψετε
#σε ακέραιο και θα την κάνετε modulo 80. Κρατείστε αυτούς τους 32 αριθμούς μοναδική φορά το καθένα και υπολογίστε
#πόσοι από αυτούς τους αριθμούς θα κληρονόντουσαν στην τελευταία κλήρωση του ΚΙΝΟ
#που θα βρείτε εδώ https://api.opap.gr/draws/v3.0/1100/last-result-and-active


import requests

r = requests.get('https://drand.cloudflare.com/public/latest', headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = r.json()
ran=data.get("randomness")
diad=[]
for i in range(0,len(ran),2):
    diad.append(ran[i : i + 2])
r = requests.get('https://api.opap.gr/draws/v3.0/1100/last-result-and-active')
kino = r.json()
w=kino.get('last')
wi=w.get('winningNumbers')
win=wi.get('list')
telar=[]
for i in diad:
    x=int(i,16)%80
    if x not in telar:
        telar.append(x)
sum=0
for i in telar:
    for j in win:
        if i==j:
            print("Κληρώθηκε ο αριθμός:", i)
            sum+=1
            break
print("*****\n")
print("Συνολικά κληρώθηκαν:", sum)
print("\n*****")
