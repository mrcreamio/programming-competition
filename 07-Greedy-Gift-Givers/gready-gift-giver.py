"""
ID: mrcream1
LANG: PYTHON3
TASK: gift1
"""


def greedyGift(dict_of_people,giver, m_given_to, money):
    money = int(money)
    num = len(m_given_to)
    if num != 0:
        money_should_be_given = int(money/num)
        giver_account_plus = money-(money_should_be_given*num)
        dict_of_people[giver] += giver_account_plus
        dict_of_people[giver] -= money
        for i in m_given_to:
            dict_of_people[i] += money_should_be_given
    else: 
        return 0

fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')

num = fin.readline()
dict_of_people = {}
for i in range(int(num)):
     name = fin.readline().strip()
     dict_of_people[name] = 0
while True:
    giver = fin.readline().strip()
    if giver == "":
        break
    money, no_of_pp = fin.readline().split(' ')
    m_given_to = []
    for j in range(int(no_of_pp)):
        pp = fin.readline().strip()
        if not pp:
            break
        m_given_to.append(pp) 
    greedyGift(dict_of_people,giver,m_given_to,money)
print(dict_of_people)
for key,value in dict_of_people.items():
    fout.write(key+" "+str(value)+"\n")
fout.close()


