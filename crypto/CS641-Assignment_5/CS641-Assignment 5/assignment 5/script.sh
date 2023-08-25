#!/bin/bash

python3 script.py | ssh -i C:\Python\ass5\mykey student@172.27.26.188 -t 2>/dev/null | grep -A1 "Slowly, a new" | grep -v "Slowly" | sed 's/--//g' | grep -E '[a-z]' | sed 's/^[ \t]*//g' | sed '/^$/d' > output.txt
