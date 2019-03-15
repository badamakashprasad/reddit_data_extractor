import praw
import datetime
from store_data import store_data
import codecs
from display_data import display_data


class extract_data(store_data):
    def __init__(self, client_id, client_secret, user_agent):
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_agent = user_agent
        self.reddit = praw.Reddit(client_id=self.client_id, client_secret=self.client_secret, user_agent=self.user_agent)
        self.url = ''
        store_data.__init__(self,name='reddit_test')
        pass

    def extract_reddit_data(self, type, subreddit_name):
        subreddit = self.reddit.subreddit(str(subreddit_name[3:]))
        data = []
        for content in subreddit.hot(limit=None):
            title = content.title
            id = content.id
            author = str(content.author)
            upvote = content.ups
            downvote = content.downs
            date,time = str(datetime.datetime.fromtimestamp(content.created_utc)).split(' ')
            body = content.url
            self.url = content.url
            store_data.content_table(self,subreddit_name,type,id,title,body,upvote,downvote,author,date,time)
            self.extract_comment(id=id)
        pass

    def extract_comment(self,id = None,more_c = None):
        if more_c is None and id is not None:
            submission = self.reddit.submission(id=id)
            submission.comments.replace_more(limit=None)
            for comment in submission.comments:
                id = comment.id
                if isinstance(comment.author,type(None)):
                    continue
                author = comment.author.name
                body = comment.body
                #print(body)
                upvotes = comment.ups
                downvotes = comment.downs
                date,time = str(datetime.datetime.fromtimestamp(comment.created_utc)).split(' ')
                store_data.store_comments(self,id,str(body),self.url,upvotes,downvotes,author,date,time)
                store_data.store_comment_linkage(self,submission.id,id)
                if len(comment.replies) > 0:
                    self.extract_comment(more_c=comment)
        else:
            more_c.replies.replace_more(limit=None)
            for reply in more_c.replies:
                id = reply.id
                if isinstance(reply.author,type(None)):
                    continue
                author = reply.author.name
                body = reply.body
                #print(body)
                upvotes = reply.ups
                downvotes = reply.downs
                date, time = str(datetime.datetime.fromtimestamp(reply.created_utc)).split(' ')
                store_data.store_comments(self, id, str(body), self.url, upvotes, downvotes, author, date, time)
                store_data.store_comment_linkage(self, more_c.id, id)
                if len(reply.replies) > 0:
                    self.extract_comment(more_c=reply)
        pass























#obj_store = store_data()
#obj_collect = display_data()
obj_extract = extract_data(client_id='fvvpnpautWtOjw', client_secret='8kfhlBWC7kfb-oPV7olF9AMsXmw',
                           user_agent='data_testing')
#conn_collect = obj_collect.connect_db("reddit_database.db")
#conn_store = obj_store.connect_db("reddit_content.db")
#all_types = obj_collect.get_subreddit_type(conn_collect)
"""

for type in all_types:
    subbreddit_list = obj_collect.get_subreddit_list(conn_collect,type)
    for subreddit in subbreddit_list:
        data = obj_extract.extract_reddit_data(type,subreddit)
        for subreddit, type, id, title, body, upvote, downvote, author, date, time in data:
            obj_store.content_table(conn_store, subreddit, type, id, title, body, upvote, downvote, author, date, time)


"""

obj_extract.extract_reddit_data('all','/r/all')