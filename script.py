import praw

reddit = praw.Reddit(client_id='',
                        client_secret='',
                        user_agent='<console:urban_define_bot:0.0.2 (by /u/',
                        username='',
                        password='')


#asks user for url and file name
user_Url = input('Input the url: ')

new_file = input("Input name of the file: ')

submission = reddit.submission(url=user_Url)



#Creates new text file with the comments taken

with open(new_file,'w') as cf:

    submission.comments.replace_more(limit=0)
    for top_level_comment in submission.comments:
        cf.write(top_level_comment.body)



