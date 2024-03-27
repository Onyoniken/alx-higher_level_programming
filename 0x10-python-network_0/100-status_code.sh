#!/bin/bash
#sends a request to a URL, and displays status code of response.
curl -s -o /dev/null -w "%{http_code}" "$1"
