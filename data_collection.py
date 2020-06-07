# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 09:17:04 2020

@author: asus
"""

import glassdoor_scraper as gs
import pandas as pd
path = "C:/Users/asus/Documents/ds_salary_proj/chromedriver"
df = gs.get_jobs('data scientist', 29, False, path , 15 )
df.to_csv('glassdoor_jobs.csv', index = False)
