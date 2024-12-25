from structure import solution

def move(sol, tabulist, printInterchange=False):
    sel, ofVarSel, unsel, ofVarUnsel = selectInterchange(sol, tabulist)
    solution.removeFromSolution(sol, sel, ofVarSel)
    solution.addToSolution(sol, unsel, ofVarUnsel)
    updateTabulist(tabulist, sel)
    if printInterchange:
        print("\t| Out:\t" + str(sel) + "\t In:\t" + str(unsel))


def selectInterchange(sol, tabulist):
    n = sol['instance']['n']
    sel = -1
    bestSel = 0x3f3f3f
    unsel = -1
    bestUnsel = 0
    bestOfVar = -0x3f3f3f
    for u in sol['sol']:
        ofVarSel = solution.distanceToSol(sol, u, without=u)
        for v in range(n):
            if v in tabulist or solution.contains(sol, v):
                continue
            ofVarUnsel = solution.distanceToSol(sol, v, without=u)
            if bestOfVar < ofVarUnsel - ofVarSel:
                bestOfVar = ofVarUnsel - ofVarSel
                sel = u
                unsel = v
                bestSel = ofVarSel
                bestUnsel = ofVarUnsel
            if ofVarUnsel > ofVarSel:
                return sel, round(bestSel,2), unsel, round(bestUnsel,2)
    return sel, round(bestSel,2), unsel, round(bestUnsel,2)


def updateTabulist(tabulist, sel):
    tabulist.pop()
    tabulist.insert(0, sel)