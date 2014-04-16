from sombrero import *
from twitter import *
from auth import *

twit = Twitter(auth=my_auth)
fours = y + "-" + m + "-" + d + "_sombreros.txt"
threes = y + "-" + m + "-" + d + "_sombreros_close.txt"
others = y + "-" + m + "-" + d + "_others.txt"
f = open(fours, "a+")
f.close()
f = open(threes, "a+")
f.close()
f = open(others, "a+")
f.close()

while games_in_progress(basegamedayURL) != 0:
    todays_games = get_games(basegamedayURL)
    for x in range(0,len(todays_games)):
        batter_list = batters(todays_games[x])
        for batter in batter_list:
            if batter["batter"] + ", " + batter["so"] in open(fours).read():
                print batter["batter"] + " already tweeted"
                
                pass
            elif int(batter["so"]) > 4:
                twit.statuses.update(status = batter["batter"] + ": " + batter["so"] + " strikeouts in " + batter["ab"] + " at-bats. #PlatinumSombrero #SombreroWatch")
                print batter["batter"]
                if batter["batter"] in open(fours).read():
                    f = open(fours, "r")
                    lines = f.readlines()
                    f.close()
                    f = open(fours, "w")
                    for line in lines:
                        if line!=batter["batter"] + ", 4, " + str(re.compile("\d")) + "\n":
                            f.write(line)
                    f.close()
                open(fours, "a+").write(batter["batter"] + ", " + batter["so"] + ", " + batter["ab"] + "\n")
    #            close(filename)
            elif batter["so"] == "4":
                twit.statuses.update(status = batter["batter"] + ": " + batter["so"] + " strikeouts in " + batter["ab"] + " at-bats. #GoldenSombrero #SombreroWatch")
                print batter["batter"]
                f = open(threes, "r")
                lines = f.readlines()
                f.close()
                f = open(threes, "w")
                for line in lines:
                    if line!=batter["batter"] + ", 3, " + str(re.compile(".")) + "\n":
                        f.write(line)
                f.close()
                open(fours, "a+").write(batter["batter"] + ", " + batter["so"] + ", " + batter["ab"] + "\n")
    #            close(filename)
            elif batter["so"] == "3":
                if batter["batter"] in open(threes).read():
                    print batter["batter"] + " already tweeted"
                    pass
                else:
                    twit.statuses.update(status = batter["batter"] + " is one strikeout away from a #GoldenSombrero! #SombreroWatch")
                    print batter["batter"]
                    open(threes, "a+").write(batter["batter"] + ", " + batter["so"] + ", " + batter["ab"] + "\n")
    #            close(filename)
            elif batter["so"] == "2":
                if batter["final"] != "F":
                    print batter["batter"] + " 2"
                    open(others, "a+").write(batter["batter"] + ", " + batter["so"] + ", " + batter["ab"] + "\n")
    print "waiting ... " + str(time.strftime("%H:%M:%S"))
    time.sleep(300)
    #twit.statuses.update(status="I'm tweeting from Python!")

if games_in_progress(basegamedayURL) == 0:
    f = open(filename, "r")
    f2 = open(filename2, "r")
    sombreros = 0
    close_calls = 0
    for line in f:
        sombreros += 1
    for line in f2:
        close_calls += 1
    f.close()
    f2.close()
    if sombreros == 0 and close_calls == 0:
        twit.statuses.update(status = "Nobody even came close to a sombrero today. :( #GoldenSombrero")
    if sombreros == 0 and close_calls == 1:
        twit.statuses.update(status = str(close_calls) + " close call, but no sombreros today. #sadday #GoldenSombrero")
    if sombreros == 0 and close_calls > 1:
        twit.statuses.update(status = str(close_calls) + " close calls, but no sombreros today. #sadday #GoldenSombrero")
    if sombreros == 1:
        f = open(filename, "r")
        line = f.readline()
        twit.statuses.update(status = "Only one MLB player/hero (" + line.split(",")[0] + ") earned a golden sombrero today. #GoldenSombrero")
        f.close()
    if sombreros > 1:
        twit.statuses.update(status = str(sombreros) + " MLB players earned sombreros today. It was a good day. #GoldenSombrero")
