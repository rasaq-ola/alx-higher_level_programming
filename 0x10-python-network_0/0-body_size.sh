#!/bin/bash
# Display the size of the body of the response from a given URL
curl -s "$1" | wc -c
