from structure import solution

def move(sol, tabulist):
    sel, ofVarSel, unsel, ofVarUnsel = selectInterchange(sol, tabulist)
    solution.removeFromSolution(sol, sel, ofVarSel)
    solution.addToSolution(sol, unsel, ofVarUnsel)
    updateTabulist(tabulist, sel)


def selectInterchange(sol, tabulist):
    n = sol['instance']['n']
    sel = -1
    bestSel = 0x3f3f3f
    unsel = -1
    bestUnsel = 0
    for v in sol['sol']:
        d = solution.distanceToSol(sol, v)
        if d < bestSel:
            bestSel = d
            sel = v
    for v in range(n):
        if v in tabulist or solution.contains(sol, v):
            continue
        d = solution.distanceToSol(sol, v, without=sel)
        if d > bestUnsel:
            bestUnsel = d
            unsel = v
    return sel, round(bestSel,2), unsel, round(bestUnsel,2)


def updateTabulist(tabulist, sel):
    tabulist.pop()
    tabulist.insert(0, sel)
