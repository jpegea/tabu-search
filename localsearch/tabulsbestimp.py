from structure import solution

def move(sol, tabulist):
    sel, ofVarSel, unsel, ofVarUnsel = selectInterchange(sol, tabulist)
    solution.removeFromSolution(sol, sel, ofVarSel)
    solution.addToSolution(sol, unsel, ofVarUnsel)
    updateTabulist(tabulist, sel)


def selectInterchange(sol, tabulist):
    n = sol['instance']['n']
    sel = None
    bestSel = None
    unsel = None
    bestUnsel = None
    for v in sol['sol']:
        d = solution.distanceToSol(sol, v)
        if bestSel is None or d < bestSel:
            bestSel = d
            sel = v
    for v in range(n):
        if v in tabulist or solution.contains(sol, v):
            continue
        d = solution.distanceToSol(sol, v, without=sel)
        if bestUnsel is None or d > bestUnsel:
            bestUnsel = d
            unsel = v
    return sel, round(bestSel,2), unsel, round(bestUnsel)


def updateTabulist(tabulist, sel):
    tabulist.pop()
    tabulist.insert(0, sel)