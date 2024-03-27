#!/bin/bash
# send request to URL with curl, displays body size
curl -s "$1" | wc -c
