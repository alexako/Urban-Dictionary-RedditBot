import praw
import urbanScrape as us

reddit = praw.Reddit(client_id='',
                        client_secret='',
                        user_agent='<console:urban_define_bot:0.0.2 (by /u/',
                        username='',
                        password='')


subreddit = reddit.subreddit('testingground4bots')

for comment in subreddit.stream.comments():
    if bot_summon in comment.body:
        x = comment.body.split()
        try:
            comment.reply((us.read_definition(us.get_definition_link(str(x[1])))))
        except:
            comment.reply("I can't define a word that does not exist")




