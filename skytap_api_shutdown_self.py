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
# user with authorization to change runstate of swarm slave configs
auth = ( LOGIN, API_TOKEN )

#REST call to local gateway to get configuration hosting this VM
local_url = 'http://gw/skytap'
result = requests.get(local_url, headers=headers, auth=auth)
jsout = json.loads(result.text)
config_url = jsout["configuration_url"]
shutdown_url = config_url + "?runstate=stopped"

#call to the Skytap API to shutdown this config
result = requests.put(shutdown_url, headers=headers, auth=auth)


