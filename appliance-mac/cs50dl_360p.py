from os import system

# Videos

for i in range(12):
    system("curl -o \"cs50_week%s_monday\" \"http://cdn.cs50.net/2014/fall/lectures/%s/m/week%sm-360p.mp4\"" % (i, i, i))
    system("curl -o \"cs50_week%s_wednesday\" \"http://cdn.cs50.net/2014/fall/lectures/%s/w/week%sw-360p.mp4\"" % (i, i, i))

    
# Problem Sets

for i in range(9):
    system("curl -o \"pset%s_normal.html\" \"http://cdn.cs50.net/2015/x/psets/%s/pset%s/pset%s.html\"" % (i, i, i, i))
    system("curl -o \"pset%s_hacker.html\" \"http://cdn.cs50.net/2015/x/psets/%s/hacker%s/hacker%s.html\"" % (i, i, i, i))
