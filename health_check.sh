#!/bin/bash

# API URLs array
# Assigning the URLs of two APIs defined in the backend-api python file.
# The localhost address has been assigned to the url.
API_URLS=(
    "http://127.0.0.1:8081/health_check"
    "http://127.0.0.1:8081/download_external_logs"
)

# Log file to store the health check results
LOG_FILE="/var/log/health_check.log"

# Each URL in API_URL is iterated over for loop
for api_url in "${API_URLS[@]}"; do
    status=""
    http_response=""
    timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    
    # Make the HTTP request
    http_response=$(curl -s -o /dev/null -w "%{http_code}" "$api_url")

    # Check the HTTP response code
    if [ "$http_response" == "200" ]; then
        echo "$(date): API at $api_url is reachable - Health check passed" >> "$LOG_FILE"
    else
        echo "$(date): API at $api_url is unreachable - Health check failed (HTTP $http_response)" >> "$LOG_FILE"
    fi
done
