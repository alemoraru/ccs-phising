#!/bin/bash

# Define the input file containing JSON data
JSON_FILE="online-valid.json"

# Loop through each IP address from the JSON file
for ip in $(cat "$JSON_FILE" | jq -r '.[].details | .[].ip_address'); do
  echo "$ip" >> ip_list.txt
  
  # Perform the API call to ipinfo.io to get IP details
  curl "ipinfo.io/$ip" >> ip_details_list.txt
  
  # Adding a brief sleep to avoid sending too many requests in a short time
  # sleep 1
  
done
