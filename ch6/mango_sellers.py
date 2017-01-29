# bredth first search looking for mango sellers in my network.

from collections import deque

def setupGraph():
    # ## setup the people 
    # ross = {'name': 'ross', 'seller': False}
    # bob = {'name': 'bob', 'seller': False}
    # claire = {'name': 'claire', 'seller': False}
    # alice = {'name': 'alice', 'seller': False}
    # tom = {'name': 'tom', 'seller': False}
    # john = {'name': 'john', 'seller': False}
    # peg = {'name': 'peg', 'seller': True}
    # anuj = {'name': 'anuj', 'seller': False}

    ## build the graph
    graph = {}
    graph["ross"] = ["bob", "claire", "alice"]
    graph["bob"] = ["anuj", "peg"]
    graph['claire'] = ['tom', 'john']
    graph['alice'] = ['peg']
    # only make it two levels
    graph['tom'] = []
    graph['john'] = []
    graph['peg'] = []
    graph['anuj'] = []

    return graph


def personIsSeller(person):
    return person[-1] == 'm'

def bredthSearch(start, graph):
    searchQueue = deque()
    searchQueue += graph[start]
    i = 0
    checked = []
    while searchQueue:
        
        i += 1
        print('iter: ' + str(i))
        print('checked: ' + str(checked))
        print('queue: ' + str(searchQueue) )
        person = searchQueue.popleft()
        print('checking...' + person)
        if person not in checked:
            if personIsSeller(person):
                print(person + ' is a mango seller!')
                return True
            else:
                searchQueue += graph[person]
                checked.append(person)
    print("didn't find a seller :(")
    return False


# initialize the graph
graph = setupGraph()

bredthSearch('ross', graph)
