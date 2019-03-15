import sqlite3
import codecs


class store_data:
    def __init__(self, name):
        self.name = name
        self.conn = sqlite3.connect(name)
        pass

    def __del__(self):
        self.conn.close()
        return True

    def subreddit_table(self, name, subreddit, date):
        """
        Store subreddits (/r/xyz) with the name as Type of subreddit

        :param name: Type of subreddit
        :param subreddit: subreddit (/r/xyz)
        :param date: Date of the subreddit created in UTC (str)
        :return: True after successful execution
        """

        status = "SELECT name FROM sqlite_master WHERE name=" + repr(name) + ";"
        stats = self.conn.execute(status)
        if not stats.fetchall():
            self.conn.execute("CREATE TABLE " + repr(name) + "(ID INTEGER PRIMARY KEY AUTOINCREMENT,SUBREDDIT TEXT NOT "
                                                             "NULL,DATE TEXT NOT NULL);")
        self.conn.execute(
            "INSERT INTO " + repr(name) + "(SUBREDDIT,DATE) VALUES (" + repr(subreddit) + "," + repr(date) + ");")
        self.conn.commit()
        return True

    def content_table(self, subreddit, type, sub_id, title, body, upvote, downvote, author, date, time):
        """
        Stores data the content/post of the subreddit into database

        :param subreddit: subreddit (/r/xyz)
        :param type: Type of subreddit
        :param sub_id: submission id of the post
        :param title: Title of the post
        :param body: url of the post
        :param upvote: upvotes got till date
        :param downvote: downvotes got till date
        :param author: posted by username
        :param date: date of the post
        :param time: time of the post
        :return: True after successful execution
        """

        status = "SELECT name FROM sqlite_master WHERE name=" + repr(subreddit) + " and type = 'table';"
        stats = self.conn.execute(status)
        if not stats.fetchall():
            self.conn.execute("CREATE TABLE " + repr(subreddit) + "(ID INTEGER PRIMARY KEY AUTOINCREMENT"
                                                                  ",TYPE TEXT NOT NULL"
                                                                  ",SUB_ID TEXT NOT NULL"
                                                                  ",TITLE TEXT NOT NULL"
                                                                  ",BODY TEXT NOT NULL"
                                                                  ",UPVOTE INT NOT NULL"
                                                                  ",DOWNVOTE INT NOT NULL"
                                                                  ",AUTHOR TEXT NOT NULL"
                                                                  ",DATE TEXT NOT NULL"
                                                                  ",TIME TEXT NOT NULL"
                                                                  ",INFO TEXT NULL);")

        print("INSERT INTO " + repr(subreddit) + "(TYPE,SUB_ID,TITLE,BODY,UPVOTE,DOWNVOTE,AUTHOR,DATE,TIME) VALUES "
                                                 "({},{},'{}',{},{},{},{},{},{});".format(repr(type), repr(sub_id),
                                                                                          codecs.getdecoder(
                                                                                              'unicode_escape')(title)[
                                                                                              0].replace("'", "''"),
                                                                                          repr(body),
                                                                                          int(upvote),
                                                                                          int(downvote), repr(author),
                                                                                          repr(date),
                                                                                          repr(time)))
        duplicate = self.conn.execute("SELECT * FROM " + repr(subreddit) + " WHERE SUB_ID = " + repr(sub_id))
        if not duplicate.fetchall():
            self.conn.execute(
                "INSERT INTO " + repr(subreddit) + "(TYPE,SUB_ID,TITLE,BODY,UPVOTE,DOWNVOTE,AUTHOR,DATE,TIME) VALUES "
                                                   "({},{},'{}',{},{},{},{},{},{});".format(repr(type), repr(sub_id),
                                                                                            codecs.getdecoder(
                                                                                                'unicode_escape')(
                                                                                                title)[0].replace("'",
                                                                                                                  "''"),
                                                                                            repr(body),
                                                                                            int(upvote),
                                                                                            int(downvote), repr(author),
                                                                                            repr(date),
                                                                                            repr(time)))
        self.conn.commit()
        return True

    def store_comments(self, sub_id, comments, link, upvotes, downvotes, author, date, time):
        """
        Table to store comments and selfbody together

        :param sub_id: submission id
        :param comments: selfbody or comment of the post
        :param link: url of the main post
        :param upvotes: upvotes given
        :param downvotes: downvotes given
        :param author: posted by username
        :param date: posted on date (UTC)
        :param time: posted on time
        :return: True after successful execution
        """
        status = "SELECT name FROM sqlite_master WHERE name = 'comments_reddit' and type = 'table';"
        if not self.conn.execute(status).fetchone():
            self.conn.execute("CREATE TABLE 'comments_reddit' (SR_NO INTEGER PRIMARY KEY AUTOINCREMENT,"
                              "SUB_ID TEXT NOT NULL,"
                              "COMMENT TEXT NOT NULL,"
                              "LINK TEXT NOT NULL,"
                              "UPVOTES INT NOT NULL,"
                              "DOWNVOTES INT NOT NULL,"
                              "AUTHOR TEXT NOT NULL,"
                              "DATE TEXT NOT NULL,"
                              "TIME TEXT NOT NULL,"
                              "RELEVANT_PERCENTAGE INT NULL,"
                              "SENTIMENT_PERCENTAGE TEXT NULL"
                              ");")
        print("INSERT INTO 'comments_reddit' (SUB_ID,COMMENT,LINK,UPVOTES,DOWNVOTES,AUTHOR,DATE,TIME) VALUES"
                          " ({},{},{},{},{},{},{},{});".format(repr(sub_id),"'"+codecs.getdecoder('unicode_escape')(comments)[0].replace("'","''")+"'",repr(link),repr(upvotes),repr(downvotes),repr(author),repr(date),repr(time)))
        self.conn.execute("INSERT INTO 'comments_reddit' (SUB_ID,COMMENT,LINK,UPVOTES,DOWNVOTES,AUTHOR,DATE,TIME) VALUES"
                          " ({},{},{},{},{},{},{},{});".format(repr(sub_id),"'"+codecs.getdecoder('unicode_escape')(comments)[0].replace("'","''")+"'",repr(link),repr(upvotes),repr(downvotes),repr(author),repr(date),repr(time)))
        self.conn.commit()
        return True

    def store_comment_linkage(self, parent_id, sub_id):
        """
        table to link comments(comment id) with post(submission id)
        :param parent_id: main post submission id
        :param sub_id: comment post id (list or str)
        :return: True after successful execution
        """
        status = "SELECT name FROM sqlite_master WHERE name = 'comment_linkage' AND type = 'table';"
        if not self.conn.execute(status).fetchone():
            self.conn.execute("CREATE TABLE comment_linkage (SR INTEGER PRIMARY KEY AUTOINCREMENT"
                              ",PARENT_ID TEXT NOT NULL,"
                              "SUB_ID TEXT NOT NULL);")
        if isinstance(sub_id, list):
            for i in range(len(sub_id)):
                self.conn.execute(
                    "INSERT INTO 'comment_linkage' (PARENT_ID,SUB_ID) VALUES ({},{});".format(repr(parent_id),repr(sub_id[i])))
                self.conn.commit()
        elif isinstance(sub_id, str):
            self.conn.execute(
                "INSERT INTO 'comment_linkage' (PARENT_ID,SUB_ID) VALUES ({},{});".format(repr(parent_id),repr(sub_id)))
            self.conn.commit()
        else:
            print("incorrect arg2")
            return False
        return True
