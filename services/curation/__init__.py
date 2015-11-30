import json,os
from oauth2client.client import SignedJwtAssertionCredentials
package_directory = os.path.dirname(os.path.abspath(__file__))

json_key = json.load(open(os.path.join(package_directory,"keys/athaliana_master_list.json")))
scope = ['https://spreadsheets.google.com/feeds']
credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)

