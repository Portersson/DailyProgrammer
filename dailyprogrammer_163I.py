########################################
# Challenge 163I: Fallout Hacking Game #
#           Date: July 9, 2014         #
########################################
import random,sys,os

dict = open(os.path.join(os.path.dirname(__file__), 'Resources\enable1.txt'), encoding ='utf-8')
print("Opening",dict.name+"...","\n")
strDict = dict.read()
dict.close()
try:
    difficulty = int(input("Difficulty (1-5)?\n>"))
    if difficulty > 7 or difficulty < 1:
        raise Exception()
except:
    difficulty = 5

print("----------","\n[Difficulty set to",difficulty,"]\n")

class Pw(object):
    """I DONT REALLY KNOW!!"""
    def __init__(self, dict):
        self.randint = random.randint(0, len(dict))
        self.word = ""
        newWord = False
        for c in dict[self.randint:]:
            if c == ' ' or c == '\n':
                newWord = not newWord
                if self.word != "":
                    if len(self.word) == difficulty*2+2:
                        break
                    else:
                        self.word = ""
            if newWord:
                if c != ' ' and c != '\n':
                    self.word += c

pws = []
for i in range(int(difficulty*2.5)+4):
    pws.append(Pw(strDict))
for x in pws:
    print(x.word.upper())
print("----------")

targetPw = pws[random.randint(0,len(pws)-1)].word

for i in range(4):
    guess = input(str(4-i)+" attempt(s) left: ").lower()
   
    count = 0
    matchingChars = 0
    try:
        for c in targetPw:
            if guess[count]==c:
                matchingChars += 1
            count+=1
    except:
        pass
    if matchingChars == len(targetPw):
        print("----------\nACCESS GRANTED\n----------")
        break
    elif 4-i == 1:
        print("----------\n   TERMINAL LOCKED\nCONTACT ADMINISTRATOR\n----------")
    else:
        print("[",matchingChars,"CORRECT ]")