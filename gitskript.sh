#!/bin/bash

git add *
git commit -m $(date +'%d/%m/%Y_%H:%M:%S:%3N')
git push
