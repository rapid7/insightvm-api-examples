import requests
import urllib3
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class IVM_functions:

	# Function used for GET calls
	def get_stuff(console_url, creds, resource):
		url = "https://"+console_url+"/api/3/"+resource+"?size=500"
		payload={}
		headers = {
		  'Accept': 'application/json;charset=UTF-8',
		  'Authorization': 'Basic '+creds
		}
		response = requests.request("GET", url, headers=headers, data=payload, verify=False)
		json_text = response.text
		parsed = json.loads(json_text)
		return parsed

	#Function used for POST calls
	def post_stuff(console_url, creds, resource, in_payload):
		url = "https://"+console_url+"/api/3/"+resource
		payload= in_payload
		headers = {
		  'Content-Type': 'application/json',
		  'Accept': 'application/json;charset=UTF-8',
		  'Authorization': 'Basic '+creds
		}
		response = requests.request("POST", url, headers=headers, data=payload, verify=False)
		json_text = response.text
		parsed = json.loads(json_text)
		if response.status_code == 201:
			id_num = parsed['id']
			return id_num
		else:
			err_msg = response.text
			this_stuff = json.loads(err_msg)
			msg = (f"ERROR {response.status_code} - {this_stuff['message']}")
			return msg

	#Function used for PUT calls
	def put_stuff(console_url, creds, resource, in_payload):
		url = "https://"+console_url+"/api/3/"+resource
		payload= in_payload
		headers = {
		  'Content-Type': 'application/json',
		  'Accept': 'application/json;charset=UTF-8',
		  'Authorization': 'Basic '+creds
		}
		response = requests.request("PUT", url, headers=headers, data=payload, verify=False)
		json_text = response.text
		parsed = json.loads(json_text)
		return parsed