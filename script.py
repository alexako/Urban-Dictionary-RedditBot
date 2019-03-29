import praw

reddit = praw.Reddit(client_id='',
                        client_secret='',
                        user_agent='<console:urban_define_bot:0.0.2 (by /u/',
                        username='',
                        password='')


bot_summon = "!urbandefine"

subreddit = reddit.subreddit('testingground4bots')

for comment in subreddit.stream.comments():
    if bot_summon in comment.body:
        comment.reply("Thankyou for summoning me! I am currently under construction and will one day be able to provide you with deffinitions from the urban dictionary.")
        print("responding to comment")




