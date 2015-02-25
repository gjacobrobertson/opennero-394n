#!/bin/bash

cd $(dirname $(readlink -f $0))

echo $*
./OpenNERO \
  --log $2 \
  --mod NERO \
  --modpath NERO:share/NERO:common \
  --command "experiments.TrainFlag('$2')" &

OPENNERO_PID=$!
echo STARTED OpenNero with PID $OPENNERO_PID

sleep $1

kill -HUP $OPENNERO_PID
echo KILLED OpenNERO PID $OPENNERO_PID
