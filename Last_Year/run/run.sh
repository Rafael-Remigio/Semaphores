#!/bin/bash

case $# in
    0) n=1;;
    1) n=$1;;
    *) echo "USAGE: $0 «number-of-runs»"; exit;;
esac

if ! [ $n -gt 0 ] 2>/dev/null; then
    echo "Wrong argument value (\"$n\"). Aborting."
    exit 1
fi

for i in $(seq 1 $n)
do
     echo -e "\nRun n.º $i"
     echo -e "stat\ny" | ./probSemSharedMemSoccerGame
done
