n = 90

import random
import time
import sys
l = list(range(1,91))
g = []
random.shuffle(l)
dict = {1:"Jiwan ek sangarsh. Take off the G the number is 1",2:"Birthday of Lal Bahudar Shastri",3:" Buy 2 get 1 free",4:"Hum doh humare doh",5:" Hum Panch",6:"Super Sixer",7:"Captain cool he is called. Behind the wicket is his heaven. The next number is 7",8:"Abhinav Bindra won India's First Individual Gold in 2008",9:"The Number of Planets Including Pluto",10:"Dus numbari",11:"Two Beautiful Legs",12:"One Dozen",13:"Unlucky for many lucky for few",14:"Start of the World War 1 ",15:"Independence Day",16:"Sweet sixteen",17:"Dance Queen Number 17",18:"Be Responsible to start voting at 18",19:"Last of the teens  1 9 Nineteen",20:"Age of Blind Dates 2 and 0 20",21:"Marriagable age 2 and 1 21",22:"The length of a Cricket Pitch",23:"The Date when the revolutionary Bhagat singh was hanged to death",24:"The Current Strength of our Team",25:"Silver Jubliee",26:"Republic Day",27:"Gateway to Heaven",28:"Dhoni finishes off in Style. India wins the world cup after 28 years.",29:"Time to Rise & shine",30:"On the rocks is the best with a small and ice in plenty. The number is 30",31:"Get up and Run",32:"A big broad Smile  32",33:"All of 3s 3 and 3 33",34:"Savan ka Mahina Ram Bhai kare Shor. Next Number is 34",35:"Jump and Jive at 35",36:"Three Dozens",37:"The total number of states and UT in India",38:"OverSize",39:"Watch your Wasteline",40:"Naughty at 40",41:"Time for some Fun @ 41",42:"Quit India Movement",43:"Pain in the Knee at 43",44:"Gokul ki galiyon main aaya maakhan chor. The next number is 44",45:"The End of World War II",46:"Chouke and Cheke 4 and 6 46",47:"Year of Independence",48:"Mahatma Gandhi Assassinated.",49:"4 and 9 49",50:"Half a century ",51:"5 and 1 51",52:"Pack of Cards",53:"Stuck in the Tree ",54:"Murghi Chor",55:"All of 5s 55",56:"Pick up the sticks",57:"5 and 7 57",58:"Make them Wait",59:"5 and 9 59",60:"One Large please. The number is 60.",61:"Bakers Bun",62:"Turn on the screw",63:"6 and 3 63",64:"Dil Maange More 6 and 4 64",65:"Its Time for Old age pension",66:"All the sixes 6 and 6 66",67:"Made in Heaven",68:"Check your Weight",69:"Ulta Palta 6 and 9 69",70:"7 and 0 70",71:"The setting sun 7 and 1 71",72:"Six Dozen",73:"Under the Tree, Lucky 3 73",74:"Still want more 7 and 4 74",75:"Platinum Jubliee",76:"Seven N Six 76",77:"Hum Saath Saath Hain 7 and 7 77",78:"Heaven's Gate 78",79:"One More time",80:"Gandhi's Breakfast",81:"All set and Done at 81",82:"Be careful. Don’t go down with Flu 8 and 2 82",83:"India Wins the first World Cup",84:"The Lion's Roar 8 and 4 84",85:"Staying Alive ",86:"Carl Benz patented his three-wheeled, petrol-powered Motorwagen in 1886",87:"8 and 7 87",88:"Bartha Benz took the first long distance ride in August 88",89:"Nearly there. All but One",90:"Start with a Small, then a Large then 90"}

def get_num():
    global n
    random.shuffle(l)
    num = l.pop(random.randint(1,n)-1)
    g.append(num)
    n -= 1
    return num

def display_timer():
    for i in range(8,0,-1):
        sys.stdout.write(str(i) +' ')
        sys.stdout.flush()
        time.sleep(1)

print("--------------------")
print("Lets Play Tombola")
print("--------------------\n")
flag = 1
while (flag == 1):
    print(f"Numbers remaining: {len(l)}")
    print(f"Numbers Generated: {g}")
    num = get_num()
    print(f"num={num}")
    print(f"{num}: {dict[num]}")
    print("\n")
    display_timer()
    chk = input("\nGenerate next number?? (y/n) :" )
    print("\n")
    if chk.lower() == "y":
        continue
    else:
        flag = 0