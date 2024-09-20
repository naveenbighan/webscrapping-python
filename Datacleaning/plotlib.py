import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('cleaned_indeed_jobs.csv')

profile= ProfileReport(df)
profile.to_file(output_file="jobs.html")