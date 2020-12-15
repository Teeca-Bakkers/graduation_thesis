import random
import time
import pandas as pd

NUMBER_OF_HUMANS = 100
TIME_END = 1000000
STEPS = 100

print("NUMBER_OF_HUMANS:",NUMBER_OF_HUMANS)
print("TIME_END:",TIME_END)
print("STEPS",STEPS)

human_list = list()
escalator = [[0] * STEPS for i in range(4)] #[[sl], [wl], [sr], [wr]]

class StandHuman:

    def __init__(self):
        self.active = False
        self.v = 0
        self.x = 0
        self.l_like = 0 #how much a human like to ride on the left
        self.r_like = 0 #----------------------------- on the right
        
class WalkHuman:

    def __init__(self):
        self.active = True
        self.v =1
        self.x = 0
        self.l_like = 0
        self.r_like = 0

def human_random():
    odd_or_even = list(range(NUMBER_OF_HUMANS))
    random.shuffle(odd_or_even)
    for i in range(NUMBER_OF_HUMANS):
        if odd_or_even[i] % 2 == 0:
            human = StandHuman()
        else:
            human = WalkHuman()
        human_list.append(human)

def shift():
    for i in range(STEPS-1):
        escalator[0][STEPS-i-1] = escalator[0][STEPS-i-2]
        escalator[1][STEPS-i-1] = escalator[1][STEPS-i-2]
        escalator[2][STEPS-i-1] = escalator[2][STEPS-i-2]
        escalator[3][STEPS-i-1] = escalator[3][STEPS-i-2]
    escalator[0][0] = 0
    escalator[1][0] = 0
    escalator[2][0] = 0
    escalator[3][0] = 0

def crash(front, front_position, behind):
    x = random.random() * STEPS
    if x <= 1-(front_position + 1)/STEPS: 
        if front.x == 0: #if left
            front.l_like -= x
        else: #if right
            front.r_like -= x
    y = random.random() * STEPS
    if y <= 1-(front_position + 1)/STEPS:
        if front.x == 0: #if left
            behind.l_like -= y
        else: #if right
            behind.r_like -= y
        
def crash_checker():
    for i in range(STEPS): #left
        if escalator[0][i] != 0 and escalator[1][i] != 0:
            crash(escalator[0][i], i, escalator[1][i])
    for i in range(STEPS): #right
        if escalator[2][i] != 0 and escalator[3][i] != 0:
            crash(escalator[2][i], i, escalator[3][i])

def walk():
    for i in range(STEPS):
        l = escalator[1][i]
        r = escalator[3][i]
        if l != 0:
            escalator[1][STEPS-i-1+(l.v)] = escalator[1][STEPS-i-1] 
        if r != 0:
            escalator[3][STEPS-i-1+(r.v)] = escalator[3][STEPS-i-1]

def side_decision(human):
    l = human.l_like
    r = human.r_like
    if l > r:
        human.x = 0
    elif l < r:
        human.x = 1
    else:
        random_x = random.random()
        if random_x <= 0.5:
            human.x = 0
        else:
            human.x = 1

def add_human(human):
    if human.active == False:
        if human.x == 0: #if left
            escalator[0][0] = human
        else: #if right
            escalator[2][0] = human
    else:
        if human.x == 0: #if left
            escalator[1][0] = human
        else: #if right
            escalator[3][0] = human

def write_data():
    for i in range(4):
        for j in range(STEPS):
            if escalator[i][j] != 0: #if human
                if escalator[i][j].active == False:
                    escalator[i][j] = "s"
                elif escalator[i][j].active == True:
                    escalator[i][j] = "w"
    for i in range(STEPS):
        print("|", escalator[0][STEPS-i-1], escalator[1][STEPS-i-1], "|", escalator[2][STEPS-i-1], escalator[3][STEPS-i-1],"|")

def data_output():
    like_table = [[0,0],[0,0]] #[[Stand],[Walk]]
    for i in range(NUMBER_OF_HUMANS):
        human = human_list[i]
        if human.active == False:
            if human.l_like > human.r_like:
                like_table[0][0] += 1
            elif human.l_like < human.r_like:
                like_table[0][1] += 1
        else:
            if human.l_like > human.r_like:
                like_table[1][0] += 1
            elif human.l_like < human.r_like:
                like_table[1][1] += 1

    df = pd.DataFrame(like_table, index=["StandHuman", "WalkHuman"], columns=["Left", "Right"])
    print(df)

def main():
    for i in range(TIME_END):
        shift() 
        crash_checker()
        walk() 
        crash_checker()
        walk() 
        crash_checker()
        #----------------------------------#
        h = human_list[i % NUMBER_OF_HUMANS]
        side_decision(h)
        add_human(h)
        if (i+1)%1000000 == 0:
            print("TIME:",i+1)
            data_output() 

human_random()
main()
write_data()

print("#-------------------------------------------------------------------------#")

s_share_0 = escalator[0].count("s")
w_share_1 = escalator[1].count("w")
s_share_2 = escalator[2].count("s")
w_share_3 = escalator[3].count("w")

s_share_0_dum = s_share_0
s_share_2_dum = s_share_2

if s_share_0_dum == 0:
    s_share_0_dum = 1
if s_share_2_dum == 0:
    s_share_2_dum = 1

print("WalkHuman/StandHuman of left: ", w_share_1/s_share_0_dum, "W:S=", w_share_1, s_share_0)
print("WalkHuman/StandHuman of right: ", w_share_3/s_share_2_dum, "W:S=", w_share_3, s_share_2)

print("#-------------------------------------------------------------------------#")

