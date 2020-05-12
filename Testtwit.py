import GetOldTweets3 as got
totalTweets = 0  # init totalTweets variable
numTweets = 0  # init numTweets variable

keywords = ['arson', 'assault', 'child abuse', 'genocide', 'homicide', 'kidnapping', 'manslaughter', 'mugging',
            'murder', 'crazy af', 'brawl', 'scrap', 'assaulted', 'rape', 'riot', 'kill',
            'savage', 'mug', 'got em', 'abuse', 'battery', 'danger', 'feeling froggy', 'warning',
            'attack', 'caution', 'fight', 'death', 'wildn out', 'killer', 'victim', 'domed',
            'burglary', 'jacked', 'stole', 'bribery', 'burglary', 'blackmail', 'bigamy', 'hijacking',
            'conspiracy', 'forgery', 'break-in', 'fraud', 'shoplifting', 'counterfeit', 'came up today', 'one up',
            'snatched', 'robbery', 'making moves', 'damage', 'baited', 'trespassing', 'drugs', 'heroin',
            'smack', 'dope', 'china white', 'skag', 'junk', 'black tar', 'big h',
            'brown sugar', 'mud', 'mexican brown', 'skunk', 'cocaine', 'blow', 'rock', 'crack',
            'yayo', 'sniff', 'white nose candy', 'bernice', 'toot', 'line', 'dust', 'flake',
            'ecstasy', 'xtc', 'molly', 'rolls', 'hug drug', 'love drug',
            'lovers speed', 'beans', 'moon rocks', 'happy pill', 'scooby snacks', 'uppers', 'methamphetamine',
            'crystal', 'meth', 'cristy', 'tina', 'crank', 'crissy', 'tweak', 'glass', 'ice', 'shards', 'whizz',
            'chalk', 'speed', 'lsd', 'acid', 'lucy in the sky with diamonds', 'cid', 'tabs',
            'doses', 'blotter', 'california sunshine', 'yellow sunshine', 'window pane', 'batter acid', 'dots',
            'looney toons', 'blue heaven', 'cubes', 'marijuana', 'cannabis', 'weed', 'pot', 'hashish', 'hash',
            'green', 'bud', 'grass', 'trees', 'reefer', 'herb', 'mary jane', 'ganja',
            'hemp', 'chronic', 'kush', 'sinsemilla', 'purple haze']  # Tweet keyword dictionary

array_length = len(keywords)  # saves length of keywords to variable array_length


def get_tweets(s):  # get_tweets function
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(s) \
        .setNear("39.768400, -86.158100") \
        .setSince("2019-06-01") \
        .setUntil("2019-06-30") \
        .setMaxTweets(1000)  # concatenated function calls from GetOldTweets3 using available functions
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)  # creates tweet object
    text_tweets = [[tweet.text] for tweet in tweets]  # for each loop dumping tweets to screen
    print("Keyword:", s, ":", "Number of tweets: ", len(text_tweets))  # dumps keyword and number of tweets for each
    print(*text_tweets, sep="\n")  # formats a new line after each tweet
    return len(text_tweets)  # function returns number of tweets for keyword


for i in range(array_length):  # fori loop to iterate length of keywords dictionary
    string = keywords[i]  # stores keyword in dictionary to variable
    numTweets = get_tweets(string)  # calls get_tweets function to scrape and returns count value from function
    totalTweets += numTweets  # sums total tweets returned for each month

print("The total number of tweets in this month is: " + str(totalTweets))  # outputs total tweets returned
