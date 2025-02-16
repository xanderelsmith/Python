moreUser="yes"
biddingDocuments={}


def getHighestBidder(biddingDocuments):
    for bids in biddingDocuments:
        print(bids)
        winner=''
        currentBid=0
        if currentBid < biddingDocuments[bids]:
            currentBid=biddingDocuments[bids]
            print(winner,"winner")
            winner=bids
        return winner
            
    
    
    
while moreUser=="yes":
    print('Welcome to the scret aunction program')
    name =input('What is your name?:\t')
    bid = input('What\'s your bid?: \t$')
    biddingDocuments[name] = int(bid)
    response= input("Are there any other bidders? Type 'yes' or 'no' ")
    moreUser=response.lower()
    if moreUser=="no":
        winner = getHighestBidder(biddingDocuments)
        print(f"The winner is {winner} with a bid of $ {biddingDocuments[winner]}")
    else:
        print('\n'*100)



    