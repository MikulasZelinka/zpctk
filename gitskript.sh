#!/bin/bash

git add -u
git reset --main/gitskript.sh
git commit -m $(date +'%d/%m/%Y_%H:%M:%S:%3N')
git push
