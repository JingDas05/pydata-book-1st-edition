# -*- encoding: utf-8 -*-
import os
import json
from pandas import DataFrame, Series
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path = os.path.abspath('.\ch02\usagov_bitly_data2012-03-16-1331923249.txt')
records = [json.loads(line) for line in open(path)]
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
print time_zones

frame = DataFrame(records)
# print frame['tz'][:10]
tz_counts = frame['tz'].value_counts()
# print tz_counts[:10]

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
# print tz_counts[:10]

results = Series([x.split()[0] for x in frame.a.dropna()])
# print results[:5]
# print results.value_counts()[:8]

cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe['a'].str.contains('Windows'),
                            'Windows', 'Not Windows')
# print operating_system[:5]
# operating_system提供标签
by_tz_os = cframe.groupby(['tz', operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)
# Use to sort in ascending order
# 对于每一行求和
# agg_counts.sum(1),根据sum和排名,是排名
indexer = agg_counts.sum(1).argsort()
# print indexer[:10]
count_subset = agg_counts.take(indexer)[-10:]
# print count_subset

normed_subset = count_subset.div(count_subset.sum(1), axis=0)
# print normed_subset

