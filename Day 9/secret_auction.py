
from art import logo

print(logo)

auction_bids = {}


def find_highest_bidder(bidding_record):
    max_bid = 0
    winner = ""
    for bidder in bidding_record:
        if bidding_record[bidder] > max_bid:
            winner = bidder
            max_bid = bidding_record[bidder]

    print(f"The winner is {winner} with a bid of ${max_bid}")

more_bidders = True
while more_bidders:
    bidder_name = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: $"))
    auction_bids[bidder_name] = bid_amount
    selection = input("Are there anyother bidders? Type 'yes' or 'no'. ")
    if selection == 'no':
        more_bidders = False
        find_highest_bidder(auction_bids)
