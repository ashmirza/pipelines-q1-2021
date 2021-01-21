import requests


#This is where we will extract
def get_launch_date(url):
    launch_data = requests.get(url)
    #print(launch_data.content)
    return launch_data.json()


#this is where we will transform
def transform_data(launch_data):
    
    for launch in launch_data:
        print(launch["mission_name"])


#This is where we will load


#This is where we run the code
result = get_launch_date('https://api.spacexdata.com/v3/launches')
#print(len(result))
transform_data(result)