#!/bin/bash
datum=$(date +'%d/%m/%Y %H:%M:%S:%3N')

git add *
git commit -m '$datum'
git push
