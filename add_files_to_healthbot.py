import os
import yaml
import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def add_tables_and_views(file_name):
    files = {'up_file': open('tables_and_views/' + file_name,'r')}
    r=requests.post(url + '/files/helper-files/' + file_name, auth=HTTPBasicAuth(authuser, authpwd), headers={ 'Accept' : 'application/json' }, verify=False, files=files)
    print file_name
    return r.status_code

def add_rule(file_name):
    files = {'topics': open('rules/' + file_name,'r')}
    r=requests.post(url + '/topics/', auth=HTTPBasicAuth(authuser, authpwd), headers={ 'Accept' : 'application/json'}, verify=False, files=files)
    print file_name
    return r.status_code

def add_playbook(file_name):
    files = {'playbooks': open('playbooks/' + file_name,'r')}
    r=requests.post(url + '/playbooks/', auth=HTTPBasicAuth(authuser, authpwd), headers={ 'Accept' : 'application/json' }, verify=False, files=files)
    print file_name 
    return r.status_code

def commit():
    r = requests.post(url + '/configuration', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    print 'healthbot configuration commited!'
    return r.status_code


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

server = "10.49.102.129"
authuser = "admin"
authpwd = "Embe1mpls"
url = 'https://'+ server + ':8080/api/v1'
headers = { 'Accept' : 'application/json', 'Content-Type' : 'application/json' }

rules_list=os.listdir('rules')
playbooks_list=os.listdir('playbooks')
tables_and_views_list=os.listdir('tables_and_views')

print '**************** adding tables and views ************************'

for table in tables_and_views_list: 
    add_tables_and_views(table)

print '**************** adding rules ************************'

for rule in rules_list:
    add_rule(rule)

print '**************** adding playbooks ************************'


for playbook in playbooks_list: 
    add_playbook(playbook)




