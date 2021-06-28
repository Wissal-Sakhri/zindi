import requests
import json

url = 'http://localhost:5000/GENDER BASED VIOLENCE'

r = requests.post(url,json=
{'age':20 ,
'race':0,
'dwelling':2,
'dwelling_type':0,
'province_code':6,
'metro_code':14,
'nationality':1,
'RTH':8,
'marital_st':4,
'Lang_inside':14,
'Lang_outside':9,
'Education':9,
'lw_work':1,
'lw_business':1,
'help_on_household':1,
'job_or_business':1,
'nature_of_work':3},)

print(r.json())