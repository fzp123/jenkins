#!/usr/bin/env python

##############################################
# NOTE: requires the use of the requests module
# which is open source and available via Pip
################################################

import requests
import datetime
import json

## setup requisite headers and parameters for API calls
headers = { 'Accept' : 'application/json',
            'Content-Type' : 'application/json'
}
# user credentials authorized for this configuration
auth = ( LOGIN , API_TOKEN )

## Get call to local gateway to get configuration hosting this VM
local_url = 'http://gw/skytap'
result = requests.get(local_url, headers=headers, auth=auth)
jsout = json.loads(result.text)
config_url = jsout["configuration_url"]
parse_for_config = config_url.rpartition("/")
my_config_id = str(parse_for_config[2])

## create a delete time one hour ahead of current time
current_time = datetime.datetime.now()
delay_before_delete = datetime.timedelta(hours=1)
delete_time = current_time + delay_before_delete
delete_time = delete_time.strftime("%Y/%m/%d %H:%M")

## create a schedule start time two minutes from now
delay_before_start = datetime.timedelta(minutes=2)
schedule_start_time = current_time + delay_before_start
schedule_start_time = schedule_start_time.strftime("%Y/%m/%d %H:%M")

# define the custom parameters for the POST ##
url = 'https://cloud.skytap.com/schedules'
schedule = [ ('title', ("Swarm Slave Cleanup Config " +
                         str(my_config_id))),
             ('configuration_id', my_config_id),
             ('start_at', schedule_start_time),
             ('end_at', delete_time),
             ('delete_at_end', 'true'),
             ('time_zone', 'Pacific Time (US & Canada)')
]

## POST new schedule ##
result = requests.post(url, headers=headers, auth=auth, params=schedule)

