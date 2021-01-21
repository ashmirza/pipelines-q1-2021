import requests
import csv

#This is where we will extract
def get_launch_date(url):
    launch_data = requests.get(url)
    #print(launch_data.content)
    return launch_data.json()


#this is where we will transform
def transform_data(launch_data):
    mission_names = []
    missions_image = []
    mission_id = []
    # launch_success = []
    # launch_failure = []
    # payload_type = []

    for launch in launch_data:
        mission_names.append(launch["mission_name"])
        missions_image.append(launch["links"]["mission_patch"])
        mission_id.append(launch["flight_number"])
    #    launch_success.append(["launch_success"])
    #    launch_failure.append(["launch_failure"])
    #    payload.append(launch["payload"]["payload_type"])
    #    print(launch["mission_name"])
    with open('flightdata.csv', 'w', newline='') as f:
        for a, b, c in zip(mission_id, mission_names, missions_image):
            writer = csv.writer(f)
            writer.writerow([a, b, c])

    # print (len(mission_names))
    # print (len(missions_image))
    # print (len(mission_id))
#This is where we will load


#This is where we run the code
result = get_launch_date('https://api.spacexdata.com/v3/launches')
#print(len(result))
transform_data(result)