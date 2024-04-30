#!/bin/bash
# Display all HTTP methods the server of a given URL will accept.
curl -Is "$1" | grep Allow | cut -c 8-
