import keep_alive
import json
import requests
import os
from uuid import uuid4
from os import path
import threading
try:
    import colorama
except ModuleNotFoundError:
    os.system("pip install colorama")
    import colorama
try:
    import pyfiglet
except ModuleNotFoundError:
    os.system("pip install pyfiglet")
    import pyfiglet
from colorama import init, Fore, Back, Style
print("\n\n\33[48;5;5m\33[38;5;234m ❮ AMINO COIN GENERATOR ❯ \33[0m\33[48;5;235m\33[38;5;5m \33[0m")
init()
print(Fore.GREEN + Style.BRIGHT)
print(pyfiglet.figlet_format("TECH", font="cybermedium"))
print(pyfiglet.figlet_format("VISION", font="cybermedium"))
THIS_FOLDER = path.dirname(path.abspath(__file__))
emailfile=path.join(THIS_FOLDER,"accounts.json")
dictlist=[]
with open(emailfile) as f:
    dictlist = json.load(f)

tm=len(dictlist)*6
def uidn(device):
	headers={"NDCDEVICEID":"32DEDD3E241E53F09D14F19A2EC0B3E68C59B297A7069F15DA43B9D1ACEC62D46A9E9D77D3E1599E2B"}
	res = requests.get(f"https://service.narvii.com/api/v1/g/s/auid?deviceId={device}", headers=headers)
	if res.status_code != 200:return Exception(res.json())
	else:return (json.loads(res.text)["auid"])
	
headers={
        "cookies":"__cfduid=d0c98f07df2594b5f4aad802942cae1f01619569096",
        "authorization":"Basic NWJiNTM0OWUxYzlkNDQwMDA2NzUwNjgwOmM0ZDJmYmIxLTVlYjItNDM5MC05MDk3LTkxZjlmMjQ5NDI4OA=="
    }
 
def tapcoins(usrd:str):
    data = {
        "reward":{"ad_unit_id":"t00_tapjoy_android_master_checkinwallet_rewardedvideo_322","credentials_type":"publisher","custom_json":{"hashed_user_id":f"{usrd}"},"demand_type":"sdk_bidding","event_id":None,"network":"facebook","placement_tag":"default","reward_name":"Amino Coin","reward_valid":"true","reward_value":2,"shared_id":"dc042f0c-0c80-4dfd-9fde-87a5979d0d2f","version_id":"1569147951493","waterfall_id":"dc042f0c-0c80-4dfd-9fde-87a5979d0d2f"},
        "app":{"bundle_id":"com.narvii.amino.master","current_orientation":"portrait","release_version":"3.4.33567","user_agent":"Dalvik\/2.1.0 (Linux; U; Android 10; G8231 Build\/41.2.A.0.219; com.narvii.amino.master\/3.4.33567)"},"date_created":1620295485,"session_id":"49374c2c-1aa3-4094-b603-1cf2720dca67","device_user":{"country":"US","device":{"architecture":"aarch64","carrier":{"country_code":602,"name":"Vodafone","network_code":0},"is_phone":"true","model":"GT-S5360","model_type":"Samsung","operating_system":"android","operating_system_version":"29","screen_size":{"height":2260,"resolution":2.55,"width":1080}},"do_not_track":"false","idfa":"7495ec00-0490-4d53-8b9a-b5cc31ba885b","ip_address":"","locale":"en","timezone":{"location":"Asia\/Seoul","offset":"GMT+09:00"},"volume_enabled":"true"}
        }
    event=uuid4()
    data["reward"]["event_id"]=f"{event}"
    try:
        requests.post("https://ads.tapdaq.com/v4/analytics/reward",json=data, headers=headers)
    except:
    	pass

def threadit(acc : dict):
	device=acc["device"]
	usrd=uidn(device)
	for _ in range(100):
		try:
			threading.Thread(target=tapcoins,args=(usrd,)).start()
			print("Claiming Coins 💰")
		except:pass
	
	print(f"\nClaimed with {usrd}")
	print(f"\n\33[48;5;5m\33[38;5;234m ------------------------------ \33[0m\33[48;5;234m\33[38;5;5m \33[0m")
def main():
    print(f"\n\33[93;5;5m\33[93;5;234m ❮ Total Accounts : {len(dictlist)} ❯ \33[0m\33[93;5;235m\33[93;5;5m \33[0m")
    print(f"\n\33[93;5;5m\33[93;5;234m ❮ Estimated Time : {tm} seconds ❯ \33[0m\33[93;5;235m\33[93;5;5m \33[0m")
    print("------------------------")
    print(f'\33[0m'+ "Started Claiming Coins")
    for amp in dictlist:
    	threadit(amp)
    print(f'Claimed coins from {len(dictlist)} accounts')
    
if __name__ == '__main__':
		main()
		
