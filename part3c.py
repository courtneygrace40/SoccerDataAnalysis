import numpy as np
import matplotlib.pyplot as plt
from lxml import etree

#some scatter plots comparing where a team is in a stat vs their actual ranking 


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

def standingListCreator(stList):
    statStandings = []
    for i in stList: 
        statStandings.append(i["name"])

    return(statStandings)


def main():


    xGD = getFirst("expected_goal_differential", True)
    standings = ["Chelsea", "Manchester City", "Arsenal", "Liverpool", "Manchester Utd", "Tottenham", "Aston Villa", "Everton", "Brighton", "Leicester City", "West Ham", "Bristol City"]

    
    xGDList = standingListCreator(xGD)
    print(xGDList)

    

    for i in standings:
        x = [standings.index(i)]
        y = [xGDList.index(i)]
        label = i
        plt.scatter(x, y, label=label)


    plt.legend()
    plt.xlabel("Standings")
    plt.ylabel("Expected Goal Differential Standings")
    plt.title("Standings vs Expected Goal Differential Standings")

    plt.show()



main()