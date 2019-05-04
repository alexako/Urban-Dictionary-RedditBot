import praw
import urbanScrape as us
import time
import re
import config
import sys
sys.setrecursionlimit(10000)

reddit = praw.Reddit(client_id=config.CLIENT_ID,
                        client_secret=config.CLIENT_SECRET,
                        user_agent='<console:urban_define_bot:0.0.2 (by /u/',
                        username=config.USERNAME,
                        password=config.PASSWORD)



subreddit = reddit.subreddit('testingground4bots')
bot_url = ""
bot_summon = "!urbandefine"
urban_url = "http://www.urbandictionary.com/define.php?term="
sign_off = "\n\nBrought to you by [Urban Dictionary Bot](%s)" % bot_url 


def run_bot():
    global errors
    for comment in subreddit.stream.comments():
        if bot_summon in comment.body:
            try:
                x = us.read_definition(urban_url + comment.body.split()[1])
                comment.reply(x)
                print("replied to comment")
            except praw.exceptions.APIException as e:
                if e.error_type == "RATELIMIT":
                    delay = re.search("(\d+) minutes?", e.message)
                    print(e.message)

                    if delay:
                        delay_seconds = float(int(delay.group(1)) * 60)
                        time.sleep(delay_seconds)
                        run_bot()
                    else:
                        delay = re.search("(\d+) seconds", e.message)
                        delay_seconds = float(delay.group(1))
                        time.sleep(delay_seconds)
                        run_bot()
            except:
                errors = errors + 1
                if errors > 5:
                    print("crashed ")
                    exit(1)
run_bot()
