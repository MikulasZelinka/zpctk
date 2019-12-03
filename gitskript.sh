#!/bin/bash

git add *
git commit -m $(date +'%d/%m/%Y%H:%M:%S:%3N')
git push
