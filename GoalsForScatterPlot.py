#Courtney Sweeney

import numpy as np
import matplotlib.pyplot as plt
from lxml import etree

#some scatter plots comparing where a team is in a stat vs their actual ranking 
#I have commented these exact functions in my part 2 file. The code to this is almost exactly the same to part3b and part3c, so I will only comment this one. 


def getFirst(attribute, order):
    attributeAndTeam = createDict(attribute)
    sortedAttrList = sort(attributeAndTeam, attribute, order)
    return(sortedAttrList)


def createDict(attribute):

    budgets = etree.parse("WSLStats.xml")
    root = budgets.getroot()

    attributeAndTeam = []
    teams = []
    attributeList = []

    attributeResult = root.xpath("//team/name | //team/" + attribute )

    for r in attributeResult:
        if r.tag == "name":
            team = r.text
            teams.append(team)
        elif r.tag == attribute:
            attributeText = float(r.text)
            attributeList.append(attributeText)

    for i in teams:
        index = teams.index(i)
        teamDict = {}
        teamDict["name"] = teams[index]
        teamDict[attribute] = attributeList[index]
        attributeAndTeam.append(teamDict)

    return(attributeAndTeam)


def sort(attributeList, attribute, order):
    if order == True:
        sortedAttributesList = sorted(attributeList, key=lambda attributeList: (attributeList[attribute]), reverse=True) 
    else:
        sortedAttributesList = sorted(attributeList, key=lambda attributeList: (attributeList[attribute])) 
    return(sortedAttributesList)

def standingListCreator(stList): #This is a new function, used to create a list of the team names in the order they were sorted into by statistic 
    statStandings = []
    for i in stList: 
        statStandings.append(i["name"])

    return(statStandings)


def main():

    goalsFor = getFirst("goals_for", True)
    standings = ["Chelsea", "Manchester City", "Arsenal", "Liverpool", "Manchester Utd", "Tottenham", "Aston Villa", "Everton", "Brighton", "Leicester City", "West Ham", "Bristol City"]

    gFList = standingListCreator(goalsFor) #creates the list with just team names in the correct order 
    print(gFList)
    

    for i in standings: #for every team, it creates a separate scatter point where the group is labeled by team
        x = [standings.index(i)]
        y = [gFList.index(i)]
        label = i
        plt.scatter(x, y, label=label)


    plt.legend() #creates the legend
    plt.xlabel("Standings") #x label
    plt.ylabel("Goals For Standings") #y label
    plt.title("Standings vs Goals For Standings") #title 

    plt.show()



main()
