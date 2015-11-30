import requests
import gspread
import json
from datetime import datetime
from services.curation import credentials

FIELDS = ['name','country','sitename','latitude','longitude','collector','collectiondate','comment']
SPREADSHEET_ID = "1VTIPXPRNdkAdYJ1ivtQViVzoDN3rhHGqQ3So9bseCis"


def search(arg):
    try:
        gc = gspread.authorize(credentials)
        ss = gc.open_by_key(SPREADSHEET_ID)
        ws = ss.worksheets()[0]
        row,is_modified = _get_row_from_args(arg)
        curator = 'N/A'
        if is_modified: 
            row.append(datetime.now())
            row.append(curator)
            ws.append_row(row)
        return 'application/json',json.dumps({'status':'OK','modified':is_modified})
    except Exception as e:
        return 'application/json',json.dumps({'status':'ERROR','reason':str(e)})

def list(arg):
    gc = gspread.authorize(credentials)
    ss = gc.open_by_key(SPREADSHEET_ID)
    ws = ss.worksheets()[0]
    records = ws.get_all_records()
    data = records
    if 'ID' in arg:
        data = _get_record_from_id(records,arg['ID'][0])                   
    return 'application/json',json.dumps(data)  
         

def _get_record_from_id(records,ID):
     return [x for x in records if x['ID'] == ID]  


def _get_row_from_args(args):
    if 'id' not in args:
        raise Exception('id is not specified')
    row = [args['id']]
    is_modified = False
    for field in FIELDS:
        val = args.get(field,'')
        if val != '':
            is_modified = True
        row.append(val)
    return row,is_modified
