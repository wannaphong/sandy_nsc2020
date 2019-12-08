import feedparser

class news(object):
    def __init__(self,url):
        self.url = url
        self.data = feedparser.parse(self.url)
    def get_news(self):
        return self.data.entries
class politics(news):
    def __init__(self):
        super().__init__("https://news.thaipbs.or.th/rss/news/politics")

class social(news):
    def __init__(self):
        super().__init__("https://news.thaipbs.or.th/rss/news/social")

class crime(news):
    def __init__(self):
        super().__init__("https://news.thaipbs.or.th/rss/news/crime")

class region(news):
    def __init__(self):
        super().__init__("https://news.thaipbs.or.th/rss/news/region")

class environment(news):
    def __init__(self):
        super().__init__("https://news.thaipbs.or.th/rss/news/environment")

class economy(news):
    def __init__(self):
        super().__init__("https://news.thaipbs.or.th/rss/news/economy")

class foreign(news):
    def __init__(self):
        super().__init__("https://news.thaipbs.or.th/rss/news/foreign")

class sport(news):
    def __init__(self):
        super().__init__("https://news.thaipbs.or.th/rss/news/sport")

class breakingnews(news):
    def __init__(self):
        super().__init__("https://news.thaipbs.or.th/rss/breakingnews")