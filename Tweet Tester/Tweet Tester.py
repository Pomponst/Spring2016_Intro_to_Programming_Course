##Input
tweet = str(input("Please enter a tweet: "))
tweet = tweet.lower()
length = len(tweet)

##Logic
while length > 140:
    print("Excess characters: ",(length-140))
    tweet = str(input("Please enter a tweet: "))
    tweet = tweet.lower()
    length = len(tweet)

##Calculation
if length <= 140:
    tweet = tweet[:-1]
    print("Length within limit. No. characters: ",length)
    print("Number of Hashtags: ",(tweet.count("#")-(tweet.count("#\t")+tweet.count("# "))))
    print("Number of Attributions: ",(tweet.count("@")-(tweet.count("@\t")+tweet.count("@ "))))
    print("Number of Links: ",tweet.count("http://"))
