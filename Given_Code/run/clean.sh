#!/bin/bash

rm -f error*
rm -f core

# change 0x610661c3 to your semaphore and shared memory key
ipcrm -S 0x612e8dd4
ipcrm -M 0x612e8dd4

