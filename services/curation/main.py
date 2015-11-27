import json
import requests

FUSION_QUERY_URL = "https://www.googleapis.com/fusiontables/v2/query"
FUSION_TABLE_ID = "16I6HWZd8PrvjlzvcKsCWShHii8RaMA_vux8sTQPI"
API_KEY = "AIzaSyDDYAfEQUBkHy6_0ysfwIRe6PucjpVoVFE"
FIELDS = ['id','name','country','sitename','latitude','longitude','collector','collectiondate','CS_number','pilot_projects','Nordborg2005','Nordborg2012','Cao2011','Schmitz2013','Long2013','1001genomes','seq_by']

def search(arg):
    return 'application/json', json.dumps(arg)

def list(arg):
    for key in ('ORDERBY','LIMIT','OFFSET'):
        _flatten_param(arg,key)    
    return search(arg)

def _flatten_param(arg,key):
    if key in arg and len(arg[key]) > 0:
        arg[key] = arg[key][0]


