from sombrero import *
import os

standings = "standings.csv"
testbatter = {"shortbatter": "Javier Baez"}

fs = open(standings, "r")
fs.close()
def update_standings(batter):
    oncharts = False
    fs = open(standings, "r")
    lines = f.readlines()
    fs.close()
    fs =open(standings,"w")
    for line in lines:
        if line.startswith(batter["shortbatter"]):
            oncharts = True
            s = re.findall(r"\d", line)
            fs.write(batter["shortbatter"] + ", " + str((int(s[0])+1)) + "\n")
        else:
            fs.write(line)

    if oncharts == False:
        fs.write(batter["shortbatter"] + ", 1")
    fs.close()

