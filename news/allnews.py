# -*- coding: utf-8 -*-
from .thaipbs import *

all_news=[]

def get_all():
    global all_news,breakingnews,politics,social,crime,region,environment,economy,foreign,sport
    n = [breakingnews(),politics(),social(),crime(),region(),environment(),economy(),foreign(),sport()]