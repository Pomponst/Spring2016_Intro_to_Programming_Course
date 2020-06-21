suits = ["hearts","diamonds","spades","clubs"]
ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
for rank in ranks:
    for suit in suits:
        print(rank, "of", suit,end="\t")
    print()
