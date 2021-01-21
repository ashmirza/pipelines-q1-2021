import requests


#This is where we will extract
def get_launch_date(url):
    launch_data = requests.get(url)
    print(launch_data.content)



#this is where we will transform




#This is where we will load


#This is where we run the code
get_launch_date('https://api.spacexdata.com/v3/launches')