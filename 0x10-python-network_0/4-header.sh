#!/bin/bash
#takes URL argument, sends a GET request, and displays response
curl -sH "X-School-User-Id: 98" "$1"
