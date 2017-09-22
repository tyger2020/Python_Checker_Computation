def can_capture(your_checker, i):
    if (abs(your_checker[0] -i[0]) == 1 and abs(your_checker[1] -i[1]) == 1):
        position = (your_checker[0] + 2*(i[0]-your_checker[0]), your_checker[1] + 2*(i[1]-your_checker[1]))
        if (position[0] >= 1 and position[0] <= 8 and position[1] >= 1 and position[1] <= 8):
            return position
    return (0,0)
###############################################################################
def get_jumps(your_checker, ocheckerlist):
    checkerlist = ocheckerlist
    for i in ocheckerlist:
        position = can_capture(your_checker, i)
        if (position != (0,0)):
            checkerlist.remove(i)
            return 1 + get_jumps(position, checkerlist)
        
    return 0
###############################################################################



checkers = raw_input('Enter checkers, separated by commas: ').split(',')
#print checkers[0]


checkerx = (int)(checkers[0])
checkery = (int)(checkers[1])

your_checker = (checkerx, checkery)

num_checkers = (int)(checkers[2])

opponent_checkers = checkers[3:]
#print opponent_checkers
for line in opponent_checkers:
    ocheckerlist = [((int)(opponent_checkers[i]),(int)(opponent_checkers[i+1])) for i in range(0,len(opponent_checkers)-1,2)]
print "checkerlist", ocheckerlist

jumps = get_jumps(your_checker, ocheckerlist)
print "jumps",jumps
