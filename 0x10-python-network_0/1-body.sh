#!/bin/bash
# Send a GET request to a URL and display the body of the response if status code is 200
curl -sL -o /dev/null -w "%{http_code}" "$1" | grep -q "200" && curl -s "$1"
