#Courtney Sweeney 

import codecs 
import csv
from lxml import etree

#opens an xml file
xmlout = codecs.open("WSLStats.xml", 'w', "utf-8")
xmlout.write("<standings>\n")

#opens a csv file and linereader
csvfile = open('WSLSoccerStats.csv', newline='')
linesreader = csv.reader(csvfile, delimiter=',', quotechar='"')

#iterates through every item in linereader 
for l in linesreader: 
    if l[0] != "Rk" and l[0]!= "": #eliminates the first two lines 
        #writes every element out for each team with the appropriate tags
        xmlout.write("<team>\n")
        xmlout.write("<name>" + l[1] + "</name>\n")
        xmlout.write("<record>\n")
        xmlout.write("\t<wins>" + l[3] + "</wins>\n")
        xmlout.write("\t<draws>" + l[4] + "</draws>\n")
        xmlout.write("\t<losses>" + l[5] + "</losses>\n")
        xmlout.write("</record>\n")
        xmlout.write("<goals_for>" + l[6] + "</goals_for>\n") 
        xmlout.write("<goals_against>" + l[7] + "</goals_against>\n")
        xmlout.write("<goal_differential>" + l[8] + "</goal_differential>\n") 
        xmlout.write("<points>" + l[9] + "</points>\n")
        xmlout.write("<points_per_match>" + l[10] + "</points_per_match>\n")
        xmlout.write("<expected_goals>" + l[11] + "</expected_goals>\n")
        xmlout.write("<expected_goals_against>" + l[12] + "</expected_goals_against>\n")
        xmlout.write("<expected_goals_per_90_minutes>" + l[14] + "</expected_goals_per_90_minutes>\n")
        xmlout.write("<expected_goal_differential>" + l[13] + "</expected_goal_differential>\n")
        xmlout.write("</team>\n")
   
    
csvfile.close()

#closes the XML file
xmlout.write("</standings>")
xmlout.close()




