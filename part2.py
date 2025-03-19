from lxml import etree



def getFirst(attribute, order): #a function to call other functions, takes in only the attribute and the order to sort it in
    attributeAndTeam = createDict(attribute)
    sortedAttrList = sort(attributeAndTeam, attribute, order)
    return(sortedAttrList) #returns the sorted attribute list 

def pointAssignor(statList, pointsDict): #assigns points to teams based on where they are in a statistic's standing

    pointTotalDict = {0:12, 1:11, 2:10, 3:9, 4:8, 5:7, 6:6, 7:5, 8:4, 9:3, 10:2, 11:1} #the dictionary that determines based on index how many points to award

    for i in statList: #iterates through the statlist of dictionaries 
        team = i["name"]  #gets the team name
        index = statList.index(i) #gets the index 
        points = pointTotalDict[index] #gets the points that need to be added be using the pointTotalDict
        for j in pointsDict: #iterates through the points dictionary to find the correct team to add points to 
            if j["name"] == team:
                j["points"] += points
                break

    return(pointsDict)
    

def createDict(attribute): #creates a list of dictionaries (originally created dictionaries, too many calls to change name)

    budgets = etree.parse("WSLStats.xml") #parses the XML file 
    root = budgets.getroot()

    #creates lists to keep track of teams, attribute information, and the list of dictionaries 
    attributeAndTeam = []
    teams = []
    attributeList = []

    attributeResult = root.xpath("//team/name | //team/" + attribute )

    for r in attributeResult: #iterates through results
        if r.tag == "name": #adds teams to team list 
            team = r.text
            teams.append(team)
        elif r.tag == attribute: #adds attribute value to attribute list 
            attributeText = float(r.text)
            attributeList.append(attributeText)

    for i in teams: #creates the dictionary 
        index = teams.index(i) #gets the index of the team 
        teamDict = {}
        teamDict["name"] = teams[index] #adds the team name to the dictionary 
        teamDict[attribute] = attributeList[index] #adds the attribute value to the dictionary 
        attributeAndTeam.append(teamDict) #appends that dictionary to the list of dictionaries 

    return(attributeAndTeam)


def sort(attributeList, attribute, order): #function to sort the lists in order depending on input 
    if order == True: #sorts in descending 
        sortedAttributesList = sorted(attributeList, key=lambda attributeList: (attributeList[attribute]), reverse=True) 
    else: #sorts in ascending 
        sortedAttributesList = sorted(attributeList, key=lambda attributeList: (attributeList[attribute])) 
    return(sortedAttributesList)


def standingsComp(statStandings): #standing comparison function

    #the actual standings in list form, with index 0 being first place 
    standings = ["Chelsea", "Manchester City", "Arsenal", "Liverpool", "Manchester Utd", "Tottenham", "Aston Villa", "Everton", "Brighton", "Leicester City", "West Ham", "Bristol City"]

    #to keep track of stat accuracy
    statAccuracy = 0
    teamAccuracies = []

   
    for i in standings:  #loops through standings 
            teamInd = standings.index(i) #saves the team's index 
            team = standings[teamInd]
            for j in statStandings: #finds the team in the stat standings 
                if j["name"] == team:
                    statInd = statStandings.index(j) #gets its place in the stat standings 
                    break
            teamAccuracy = abs(teamInd - statInd) #get the accuracy of its placement 
            teamAccuracies.append(teamAccuracy) 
            statAccuracy -= teamAccuracy #subtracts that from the stat accuracy 
            

    statAccuracy /= 12 #divides stat accuracy by 12, the number of teams 

    
    statAccuracy = round(statAccuracy, 3)
    return(statAccuracy)


def goalCompCreator(xGStat, rawStat): #creates sorted lists and standing comparison numbers for actual vs expected stats 

    xGStatDict = createDict(xGStat) #creates a dictionary of the expected stat
    rawStatDict = createDict(rawStat) #creates a dictionary of the actual stat 
  

    xGCompList = [] #creates a list of dictionaries where the team's name and the difference between expected and actual stats 

    for i in xGStatDict: #loops through the expected stats 
        xGComp ={}
        for j in rawStatDict: #loops through the raw stats 
            
            if i['name'] == j['name']: 
                xGComp['name'] = i['name'] #sets the name 
                xGComp['goalComp'] = round((float(j[rawStat])- float(i[xGStat])), 1) #creates the stat for the dictionary 

        xGCompList.append(xGComp)

    sortedxGCompList = sort(xGCompList, "goalComp", True)  #sorts the stats both ways to see which is better for that stat
    sortedxGCompList2 = sort(xGCompList, "goalComp", False)
    xGCompeval = standingsComp(sortedxGCompList) #does the standing comparison for both lists 
    xGCompeval2 = standingsComp(sortedxGCompList2)

    return(xGCompeval, xGCompeval2, sortedxGCompList, sortedxGCompList2)


def main():

    points = [] #creates a list for points 

    budgets = etree.parse("WSLStats.xml") #parses the XML
    root = budgets.getroot()
    teamResult = root.xpath("//team/name")

    teams = [] #creates a list of the teams 


    for r in teamResult: #gets all of the team names 
        if r.tag == "name":
            team = r.text
            teams.append(team)

    for i in teams: #creates a dictionary with "name" and "points" to track team points
        index = teams.index(i)
        teamDict = {}
        teamDict["name"] = teams[index]
        teamDict["points"] = 0
        points.append(teamDict)


    #The rest of the code is the same for every stat, so I will only comment out one block


    print("\nACCURACY OF EACH STATISTIC")

    #Goals Against 
    goalsAgainst = getFirst("goals_against", False) #need LOWEST, sends into getFirst to sort with value False
    points = pointAssignor(goalsAgainst, points) #assigns points based on the standings using goals against
    goalsAgainstAccuracy = standingsComp(goalsAgainst) #gets the accuracy of those standings 
    print("Goals Against: " + str(goalsAgainstAccuracy)) #prints results 

    #Goals For
    goalsFor = getFirst("goals_for", True) #need HIGHEST
    points = pointAssignor(goalsFor, points)
    goalsForAccuracy = standingsComp(goalsFor)
    print("Goals For: " + str(goalsForAccuracy))

    #Goal Differential 
    goalDiff = getFirst("goal_differential", True) #need HIGHEST 
    points = pointAssignor(goalDiff, points)
    goalDiffAccuracy = standingsComp(goalDiff)
    print("Goal Differential: " + str(goalDiffAccuracy))
    
    #Expected Goals 
    xG = getFirst("expected_goals", True) #need HIGHEST
    points = pointAssignor(xG, points)
    xGAccuracy = standingsComp(xG)
    print("Expected Goals: " + str(xGAccuracy))

    #Expected Goals Against
    xGA= getFirst("expected_goals_against", False)
    points = pointAssignor(xGA, points)
    xGaAccuracy = standingsComp(xGA)
    print("Expected Goals Against: " + str(xGaAccuracy))

    #Expected Goals Per 90 Minutes 
    xGPer90 = getFirst("expected_goals_per_90_minutes", True)
    points = pointAssignor(xGPer90, points)
    xGper90Accuracy = standingsComp(xGPer90)
    print("Expected Goals Per 90: " + str(xGper90Accuracy))

    #Expected Goal Differential 
    xGD = getFirst("expected_goal_differential", True) 
    points = pointAssignor(xGD, points)
    xGDAccuracy = standingsComp(xGD)
    print("Expected Goal Differential: " + str(xGDAccuracy))


    #The next section creates the expected vs actual stats 

    xGCompeval, xGCompeval2, sortedXGC, sortedXGC2 = goalCompCreator("expected_goals", "goals_for") #sends goals for and expected goals into goalCompCreator
    
    #Evaluates the points here 
    points = sort(points, "points", True)
    accuracySoFar = standingsComp(points)
    print(accuracySoFar)

    print("Expected Goal vs Goal Highest Difference: " + str(xGCompeval))
    print("Expected Goal vs Goal Lowest Difference: " + str(xGCompeval2))

    xGACompeval, xGACompeval2, sortedXGAC, sortedXGAC2 = goalCompCreator("expected_goals_against", "goals_against")
    xGDCompeval, xGDCompeval2, sortedXGDC, sortedXGDC2 = goalCompCreator("expected_goal_differential", "goal_differential")

    points = pointAssignor(sortedXGC, points)
    points = pointAssignor(sortedXGAC2, points)
    points = pointAssignor(sortedXGDC, points)

    print("Expected GA vs GA Highest Difference: " + str(xGACompeval))
    print("Expected GA vs GA Lowest Difference: " + str(xGACompeval2))
    print("Expected GD vs GD Highest Difference: " + str(xGDCompeval))
    print("Expected GD vs GD Lowest Difference: " + str(xGDCompeval2) +"\n")

    
    #Evaluates the points again 
    points = sort(points, "points", True)
    accuracySoFar = standingsComp(points)
    print(accuracySoFar)
    


                

    
main()