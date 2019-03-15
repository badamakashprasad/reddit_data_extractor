import praw
import datetime



search = lambda x, ls: [i for i, obj in enumerate(ls) if obj == x]

reddit = praw.Reddit(client_id='public_key', client_secret='private_key', user_agent='data testing')
subreddit = reddit.subreddit('all')


"""

for submission in subreddit.hot(limit=10):
    print(submission.author) 
    print(submission.title)  # Output: the submission's title
    print(submission.score)  # Output: the submission's score
    print(submission.id)     # Output: the submission's ID
    print(submission.url)    # Output: the URL the submission points to
                             # or the submission's URL if it's a self post







all = reddit.subreddit("all")
counter = 1
for post in all.search("trump",sort='comments',limit=None):
    print(counter)
    print("ID:{}\nTitle:{}\nURL:{}\nDate:{}\n".format(post.id,post.title,post.url,datetime.datetime.fromtimestamp(post.created))+20*"-"+"\n")

    counter+=1


"""

submission = reddit.submission(id = 'a7m150')
#print(submission.title)
#print(datetime.datetime.fromtimestamp(submission.created))
#print(submission.selftext)
for comment in submission.comments:
    print(comment.body)
    print(comment.ups)
    print(comment.downs)
    print(comment.author)
    print(len(comment.replies))

    """
        if len(comment.replies) > 0:
        for reply in comment.replies:
            print("REPLY:{}".format(reply.body))

    """
    print('---------------------------------------------')

