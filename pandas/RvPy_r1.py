# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 19:23:45 2014

@author: victor
"""

# This starts the IPython Notebook pylab module, useful for plotting and
# interactive scietific computing
#%pylab inline
from pandas import read_csv

# read the data into a pandas DataFrame
body_count_data = read_csv("http://files.figshare.com/1332945/film_death_counts.csv")

# Divide the body counts by the length of the film
body_count_data["Deaths_Per_Minute"] = (body_count_data["Body_Count"].apply(float).values /
    body_count_data["Length_Minutes"].values)

# Only keep the top 25 highest kills per minute films
body_count_data = body_count_data.sort("Deaths_Per_Minute",ascending=False)[:25]

# Change the order of the data so highest kills per minute films are on top in the plot
body_count_data = body_count_data.sort("Deaths_Per_Minute", ascending=True)
body_count_data

# Generate