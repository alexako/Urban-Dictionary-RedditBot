import praw
import urbanScrape as us
import time
import re

reddit = praw.Reddit(client_id='',
                        client_secret='',
                        user_agent='<console:urban_define_bot:0.0.2 (by /u/',
                        username='',
                        password='')


def post():

    subreddit = reddit.subreddit('testingground4bots')
# reads through subreddit comments and finds wake word.
    for comment in subreddit.stream.comments():
        try:
            x = comment.body.split() #I might need to move this or make it gloabl
# When the word is found it grabs the deffinition from urban scrape it replies to the comment with the proper deffinition
            if bot_summon in comment.body:
                comment.reply((us.read_definition(us.get_definition_link(str(x[1])))))
                print("replied to comment")
            else:
                comment.reply("word could not be deffined")
                print("word could not be deffined")
#sleep mode if api requests maxxed out
        except praw.exceptions.APIException as e:
            if (e.error_type == "RATELIMIT"):
                delay = re.search("(\d+) minutes?", e.message)
                print(e.message)

                if delay:
                    delay_seconds = float(int(delay.group(1)) * 60)
                    time.sleep(delay_seconds)
                    post()
                else:
                    delay = re.search("(\d+) seconds", e.message)
                    delay_seconds = float(delay.group(1))
                    time.sleep(delay_seconds)
                    post()
# Kills script if it recives over 5 errors
        except:
            errors = errors + 1
            if (errors > 5):
                print("crashed ")
                exit(1)
post()




