import random

# pitchs is percentage chance the pitcher throws strike
# swings is percentage chance batter swings at thrown strike
# hits is percentage chance batter hits ball while swinging
# babip is babip

def inplay(babip):
    result = random.random()
    if result < babip:
        return 3 # ball is down
    else:
        return 2 # out

def pitch(pitchs, swings, hits, babip):
    result = random.random()
    if result < pitchs:
        hitresult = random.random()
        if hitresult < swings:
            contactresult = random.random()
            if contactresult < hits:
                return inplay(babip)
            else:
                return 1 # swing and miss
        else:
            return 1 # watched strike
    else:
        return 0 # thrown ball

def ab(pitchs, swings, hits, babip):
    count = [0,0]
    out = 0
    bases = 0
    while count[0] < 4 and count[1] < 3 and out == 0 and bases == 0:
        pitchresult = pitch(pitchs, swings, hits, babip)
        if pitchresult == 0:
            count[0] += 1
        elif pitchresult == 1:
            count[1] += 1
        elif pitchresult == 2:
            out = 1
        elif pitchresult >= 3:
            bases += pitchresult - 2
    if count[0] == 4:
        bases += 1
    elif count[1] == 3:
        out += 1
    return count, bases, out

def inning(pitchs, swings, hits, babip, i):
    outs = 0
    base1 = 0
    base2 = 0
    base3 = 0
    runs = 0
    while outs < 3:
        count = 0
        atbat = ab(pitchs[i], swings[i], hits[i], babip[i])
        count += 1
        if atbat[1] > 0:
            if atbat[1] == 1:
                if base1 == 1:
                    if base2 == 1:
                        if base3 == 1:
                            runs += 1
                            base3 = 1
                        else:
                            base3 = 1
                        base2 = 1
                    else:
                        base2 = 1
                    base1 = 1
                else:
                    base1 = 1
                base1 = 1
        else:
            outs += 1
        i = i + count # fix this up
    print(runs, outs, base1, base2, base3, i)
    return runs, i

def game(pitchs, swings, hits, babip):
    score = [0,0]
    innings = 0
    bottom = 0
    i = 0
    while innings < 10:
        half = inning(pitchs, swings, hits, babip, i)
        score[0] += half[0]
        i = half[1]
        innings += 1
    print(score)

pitchs = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
swings = [0.3, 0.4, 0.5, 0.2, 0.4, 0.6, 0.7, 0.1, 0.9]
hits = [0.4, 0.7, 0.6, 0.8, 0.8, 0.9, 0.4, 0.5, 0.4]
babip = [0.4, 0.5, 0.3, 0.4, 0.5, 0.4, 0.5, 0.3, 0.3]
game(pitchs, swings, hits, babip)