import requests
import json
import getpass
from datetime import date

Username=input('Username:-') #if runing on Python 2 so raw_input should be use as input function
Password=getpass.getpass()

f = open ('APIC.txt')

x=str(date.today())

saveoutput =  open('Capacity_Report_'+x+'.txt', "w")

for IP in f:
	APIC_IP=IP
		
	r = requests.post('https://'+APIC_IP+'/api/aaaLogin.json', json={'aaaUser':{"attributes":{'name':Username,'pwd':Password}}}, verify=False)
	r_json = r.json()
	token = r_json["imdata"][0]["aaaLogin"]["attributes"]["token"]
	cookie = {'APIC-cookie':token}

	BD = requests.get('https://'+APIC_IP+'/api/class/fvBD.json?rsp-subtree-include=count&_dc=1478828916248', cookies=cookie, verify=False)
	BD_json = BD.json()
	non=json.dumps(BD_json, indent=4, sort_keys=True)
	BD1=("Total BD count is " + non[154:158])
	
	TN = requests.get('https://'+APIC_IP+'/api/class/fvTenant.json?rsp-subtree-include=count&_dc=1478828916249', cookies=cookie, verify=False)
	TN_json = TN.json()
	non=json.dumps(TN_json, indent=4, sort_keys=True)
	TN1=("Total Tenant count is " + non[154:158])
	
	L3 = requests.get('https://'+APIC_IP+'/api/class/fvCtx.json?rsp-subtree-include=count&_dc=1478828916248', cookies=cookie, verify=False)
	L3_json = L3.json()
	non=json.dumps(L3_json, indent=4, sort_keys=True)
	L31=("Total L3 count is " + non[154:158])
	
	EP = requests.get('https://'+APIC_IP+'/api/class/fvAEPg.json?rsp-subtree-include=count&_dc=1478828916248', cookies=cookie, verify=False)
	EP_json = EP.json()
	non=json.dumps(EP_json, indent=4, sort_keys=True)
	EP1=("Total EP count is " + non[154:158])
		
	VRF = requests.get('https://'+APIC_IP+'/api/class/fvRsCtx.json?rsp-subtree-include=count&_dc=1478828916248', cookies=cookie, verify=False)
	VRF_json = VRF.json()
	non=json.dumps(VRF_json, indent=4, sort_keys=True)
	VRF1=("Total VRF count is " + non[154:158])
	
	saveoutput.write('***Report for '+IP+' APIC***'+'\n')
	saveoutput.write(BD1+'\n')
	saveoutput.write(TN1+'\n')
	saveoutput.write(L31+'\n')
	saveoutput.write(VRF1+'\n')
	saveoutput.write(EP1+'\n'+'\n')
	
saveoutput.close()