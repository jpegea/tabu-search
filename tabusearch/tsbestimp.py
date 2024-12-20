from structure import solution

# def improve(sol,tabulist):
#     improve = True
#     while improve:
#         improve = tryImprove(sol,tabulist)


def move(sol,tabulist):
    sel, ofVarSel, unsel, ofVarUnsel, secondUnsel, ofVarSecondUnsel = selectInterchange(sol,tabulist)
    if ofVarSel < ofVarUnsel:
        solution.removeFromSolution(sol, sel, ofVarSel)
        solution.addToSolution(sol, unsel, ofVarUnsel)
        uploadlist(tabulist,sel)
    else:
        solution.removeFromSolution(sol, sel, ofVarSel)
        solution.addToSolution(sol, secondUnsel, ofVarSecondUnsel)
        uploadlist(tabulist,sel)
    return
    


def selectInterchange(sol,tabulist):
    n = sol['instance']['n']
    sel = -1
    bestSel = 0x3f3f3f
    unsel = -1
    bestUnsel = 0
    secondUnsel=-1
    secondBestUnsel=0
    for v in sol['sol']:
        d = solution.distanceToSol(sol, v)
        if d < bestSel:
            bestSel = d
            sel = v

    for v in range(n):
        d = solution.distanceToSol(sol, v, without=sel)
        if not solution.contains(sol, v) and not v in tabulist:
            if d > bestUnsel:
                bestUnsel = d
                unsel = v
            elif d > secondBestUnsel:
                secondUnsel=v 
                secondBestUnsel=d
                
    return sel, round(bestSel,2), unsel, round(bestUnsel,2),  secondUnsel, round(secondBestUnsel,2)

def uploadlist(tabulist,node):
    tabulist.pop()
    tabulist.insert(0,node)
    return