#!/bin/bash
#sends JSON POST request to URL as first argument, displays body of the response
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
