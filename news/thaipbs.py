# -*- coding: utf-8 -*-
import feedparser
from dateutil import parser
import datetime
import re

def stripHTMLTags(html):
  """
    Strip HTML tags from any string and transfrom special entities
    from http://www.codigomanso.com/en/2010/09/truco-manso-eliminar-tags-html-en-python/
  """
  text = html
 
  # apply rules in given order!
  rules = [
    { r'>\s+' : u'>'},                  # remove spaces after a tag opens or closes
    { r'\s+' : u' '},                   # replace consecutive spaces
    { r'\s*<br\s*/?>\s*' : u'\n'},      # newline after a <br>
    { r'</(div)\s*>\s*' : u'\n'},       # newline after </p> and </div> and <h1/>...
    { r'</(p|h\d)\s*>\s*' : u'\n\n'},   # newline after </p> and </div> and <h1/>...
    { r'<head>.*<\s*(/head|body)[^>]*>' : u'' },     # remove <head> to </head>
    { r'<a\s+href="([^"]+)"[^>]*>.*</a>' : r'\1' },  # show links instead of texts
    { r'[ \t]*<[^<]*?/?>' : u'' },            # remove remaining tags
    { r'^\s+' : u'' }                   # remove spaces at the beginning
  ]
 
  for rule in rules:
    for (k,v) in rule.items():
      regex = re.compile (k)
      text  = regex.sub (v, text)
 
  # replace special strings
  special = {
    '&nbsp;' : ' ', '&amp;' : '&', '&quot;' : '"',
    '&lt;'   : '<', '&gt;'  : '>', '\u200b' : '',
    '&ldquo;' : '"', '&rdquo;' : '"'
  }
 
  for (k,v) in special.items():
    text = text.replace (k, v)
 
  return text

class news(object):
    def __init__(self,url:str):
        self.url = url
        self.data = feedparser.parse(self.url)
        self.news = []
        for i in self.data.entries:
          self.news.append((parser.parse(i.published),i.summary))
    def get_news(self):
        return self.news
    def clean(self,t:str):
        return stripHTMLTags(re.sub('<[^<]+?>', '',t).strip())
    def yesterday(self):
        self.today = []
        offset = datetime.timezone(datetime.timedelta(hours=7))
        for i in self.news:
          #print(datetime.datetime.now(offset).date())
          #print(i[0].date())
          if (datetime.datetime.now(offset)- datetime.timedelta(days=1)).date() == i[0].date():
            self.today.append(self.clean(i[1]))
        return self.today
    def get_today(self):
        self.today = []
        offset = datetime.timezone(datetime.timedelta(hours=7))
        for i in self.news:
          #print(datetime.datetime.now(offset).date())
          #print(i[0].date())
          if (datetime.datetime.now(offset)- datetime.timedelta(days=0)).date() == i[0].date():
            self.today.append(self.clean(i[1]))
        return self.today

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