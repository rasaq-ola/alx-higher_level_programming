#!/bin/bash
# Send GET rqst. to URL & display d body of d resp. if stat code is 200
curl -sL "$1" -o /dev/null -w "%{http_code}" | grep -q "200" && curl -sL "$1"
