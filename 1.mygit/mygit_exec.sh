#!/bin/bash

CURRENT_DIR=$(cd $(dirname $0); pwd)
CMD=$CURRENT_DIR/'mygit.py '$@

var=$(python3 $CMD)
eval $var
