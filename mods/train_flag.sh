#!/bin/bash

cd $(dirname $(readlink -f $0))

./OpenNERO \
  --log $3 \
  --mod NERO \
  --modpath NERO:share/NERO:common \
  --headless \
  --command "TrainFlag('$1')" &

OPENNERO_PID=$!
echo STARTED OpenNero with PID $OPENNERO_PID

sleep $2

kill -HUP $OPENNERO_PID
echo KILLED OpenNERO PID $OPENNERO_PID