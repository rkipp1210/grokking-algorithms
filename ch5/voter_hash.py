# Hash table to track if people have voted

voters = {}

def checkVote(name):
    if voters.get(name):
        print("don't let them vote again!")
    else:
        voters[name] = True
        print("let em vote!")

checkVote("Ross")
checkVote("Tom")
checkVote("Ross")