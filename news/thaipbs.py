import feedparser

class news(object):
    def __init__(self,url):
        self.url = url
        self.data = feedparser.parse(self.url)
    def get_news(self):
        return self.data.entries
class politics(news):
    """
    ข่าวการเมือง
    """
    def __init__(self):
        super().__init__("https://news.thaipbs.or.th/rss/news/politics")

class social(news):
    """
    ข่าวสังคม
    """
    def __init__(self):
        super().__init__("https://news.thaipbs.or.th/rss/news/social")

class crime(news):
    """
    ข่าวอาชญากรรม
    """
    def __init__(self):
        super().__init__("https://news.thaipbs.or.th/rss/news/crime")

class region(news):
    """
    ข่าวภูมิภาค
    """
    def __init__(self):
        super().__init__("https://news.thaipbs.or.th/rss/news/region")

class environment(news):
    """
    ข่าวสิ่งแวดล้อม
    """
    def __init__(self):
        super().__init__("https://news.thaipbs.or.th/rss/news/environment")

class economy(news):
    """
    ข่าวเศรษฐกิจ
    """
    def __init__(self):
        super().__init__("https://news.thaipbs.or.th/rss/news/economy")

class foreign(news):
    """
    ข่าวต่างประเทศ
    """
    def __init__(self):
        super().__init__("https://news.thaipbs.or.th/rss/news/foreign")

class sport(news):
    """
    ข่าวกีฬา
    """
    def __init__(self):
        super().__init__("https://news.thaipbs.or.th/rss/news/sport")

class breakingnews(news):
    """
    ข่าวเด่น
    """
    def __init__(self):
        super().__init__("https://news.thaipbs.or.th/rss/breakingnews")