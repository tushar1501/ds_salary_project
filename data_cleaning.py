

import pandas as pd
df = pd.read_csv('glassdoor_jobs.csv')

#saalary parsing 
df = df[df['Salary Estimate'] != '-1']
#company name text only
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis =1 )

#age of company
df['age'] = df.Founded.apply(lambda x: x if x <1 else 2020-x)

#parsing of job description(DS,etc)
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.python_yn.value_counts()


df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() else 0)
df.R_yn.value_counts()

df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()

df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws.value_counts()

df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel.value_counts()

df_out = df.drop(['Salary Estimate'], axis = 1)

df_out.to_csv('salary_data_cleaned.csv',index = False)





