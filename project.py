import json
import re
#from nltk.corpus import stopwords
import string

instructionsList = []

instructionsWordList = []

tools = []#["chef's", "knife", "soup", "spoon", "bowl", "spoon"]

toolsMaster = []#["chef's knife", "soup spoon", "bowl", "spoon"]

instruction = "Pour the soup spoon into the bowl and soup Eat with spoon and"

def getTools():

    toolsMasterFile = open('newTools.txt','r')
    
    for line in toolsMasterFile:
        line = re.sub('\n','',line)
        toolsMaster.append(line)
    
    tokenTools = open('tokenizedTools.txt','r')

    for line in tokenTools:
        line = re.sub('\n','',line)
        tools.append(line)
    
#    print(toolsMaster)
##    print("\n")
#    print(tools)




def getInstructions():
    with open('recipes_raw_nosource_epi.json') as f:
        data = json.load(f)
    for recipe in data.values():
        instructionsList.append(recipe["instructions"] + " a")

#    print("here" + instructionsList[0])
    return instructionsList


def cleanInstructions(instructionsList):
    stopWords = ['a','about','an','and','are','as','at','be','but','by','for','from','has','have','he','his','in','is','it','its','more','new','of','on','one','or','said','say','that','the','their','they','this','to','was','which','who','will','with','you']
    for instruction in instructionsList:
        instruction = re.sub('[!@#:;"{}<>,.()\/^\_%$1234567890]', '', instruction)
        instructionWords = instruction.lower().split()
        instructionWords = [x for x in instructionWords if x not in stopWords]
        instructionsWordList.append(instructionWords)
    return instructionsWordList

def findTools(recipeNum, instructionsWordList):
    
#    masterTools = [word in recipeWords for word in tools]
#    print(instructionsWordList[recipeNum])
    masterTools = []
    buffer = ""
    for word in instructionsWordList[recipeNum]:
        if word in tools:
            buffer += word + " "
        else:
            if(len(buffer) > 0):
                buffer = buffer[0:len(buffer)-1]
                masterTools.append(buffer)
            buffer = ""


    for i in range(0, len(masterTools)):
        if masterTools[i] not in toolsMaster:
            masterTools[i] = ''
    masterTools = list(filter(None, masterTools)) # fastest

    masterTools = list(set(masterTools))

    print(len(masterTools))


    return masterTools






getTools()
getInstructions()
cleanInstructions(instructionsList)


recipeNumber = input("What recipe do you want the tools for?")

print("These are the tools you need:")
print(findTools(int(recipeNumber),instructionsWordList))
#findTools(instruction, instructionsList)




