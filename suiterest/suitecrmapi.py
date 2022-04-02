import os
import urllib.request
import json
import hashlib
import requests

class SuitCrmApi():
	def __init__(self):
		self.Url	=	"https://suitecrmdemo.dtbc.eu/service/v4_1/rest.php"

	def login(self):
		encodedPassword = hashlib.md5('Demo'.encode('utf-8')).hexdigest()
		data = json.dumps({'user_auth': {'user_name': 'Demo','password': encodedPassword}})
		args = {'method': 'login', 'input_type': 'json',
				'response_type' : 'json', 'rest_data' : data}
		params = urllib.parse.urlencode(args).encode('utf-8')
		response = requests.get(self.Url, params).json()
		# data = json.loads(response.decode('utf-8'))
		session_id = response['id']
		return session_id

	def getData(self):
		session_id = self.login()
		data = json.dumps({'session': session_id, 'module_name': 'Leads', 'query': '', 'order_by': '', 'offset' : '', 'select_fields': ['phone_work', 'first_name', 'last_name'], 'link_name_to_fields_array': '', 'max_results': '', 'deleted': False})
		args = {'method': 'get_entry_list', 'input_type': 'json',
				'response_type' : 'json', 'rest_data' : data}
		params = urllib.parse.urlencode(args).encode('utf-8')
		response = requests.get(self.Url, params)
		return response.json()

# suitecrm = SuitCrmApi()
# x = suitecrm.getData()
