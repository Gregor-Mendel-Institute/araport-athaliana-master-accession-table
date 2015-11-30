import requests
import gspread
import json
from datetime import datetime
from services.curation import credentials

FIELDS = ['name','country','sitename','latitude','longitude','collector','collectiondate','comment']
SPREADSHEET_ID = "1VTIPXPRNdkAdYJ1ivtQViVzoDN3rhHGqQ3So9bseCis"


def search(arg):
    gc = gspread.authorize(credentials)
    ss = gc.open_by_key(SPREADSHEET_ID)
    ws = ss.worksheets()[0]
    row,is_modified = _get_row_from_args(arg)
    curator = 'N/A'
    if is_modified: 
        row.append(datetime.now())
        row.append(curator)
        ws.append_row(row)
    return 'application/json',''

def list(arg):
    gc = gspread.authorize(credentials)
    ss = gc.open_by_key(SPREADSHEET_ID)
    ws = ss.worksheets()[0]
    records = ws.get_all_records()
    data = records
    if 'ID' in arg:
        data = _get_record_from_id(records,arg['ID'][0])                   
    return 'application/json',json.dumps(arg)  
         

def _flatten_param(arg,key):
    if key in arg and len(arg[key]) > 0:
        arg[key] = arg[key][0]

def _get_record_from_id(records,ID):
     return [x for x in records if x['ID'] == ID]  


def _get_row_from_args(args):
    if 'ID' not in args:
        raise Exception('ID is not specified')
    row = [args['ID']]
    is_modified = False
    for field in FIELDS:
        val = args.get(field,'')
        if val != '':
            is_modified = True
        row.append(val)
    return row,is_modified
