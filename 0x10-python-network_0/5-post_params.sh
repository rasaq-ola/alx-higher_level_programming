#!/bin/bash
# Send a POST request with specific parameters and display the response body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
