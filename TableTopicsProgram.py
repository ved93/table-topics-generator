
import sys
import random
from pathlib import Path




def welcomeMessage():
    response = "N"
    print("This program with give a topic a table topics speech. A clock will start for 2:00 minutes. Keeps practicing!")
    while(response.upper() != "Y"):
        response = input("Are you ready? Y/N or (Q)uit: ")
        if response.upper() == "Q":
            exit


def readInParseFile():

    topicList = [None] * 500
    with open(str(Path(__file__).parent)+'/TM-365-sample-table-topics-questions.txt', 'r',encoding='utf-8') as fp:
        lines = (line.rstrip() for line in fp) # All lines including the blank ones
        lines = (line for line in lines if line) # Non-blank lines
        cnt = 0
        for line in lines:
            # print("""___""", line)
            (number, topic) = line.strip().split(". ")
            topicList[int(number)-1] = topic
            cnt+=1

    return topicList,cnt

def chooseQuestionNumber(topicList,cnt):
    qNumber = input("Which topic do you want? Pick number 1-{}: ".format(cnt))
    print("\n\n\n\n\n%s\n\n\n\n\n" % topicList[int(qNumber)-1])




# https://www.northrise-toastmasters.org/members/resourcenotes/50_Ideas_TT.htm
# https://toastmasters.fandom.com/wiki/Table_Topics_Ideas


# print(Path.cwd())
import os

# print('getcwd:      ', os.getcwd())
# print('__file__:    ', __file__)

print(str(Path(__file__).parent))

# welcomeMessage()
topicList,cnt = readInParseFile()
chooseQuestionNumber(topicList,cnt)





