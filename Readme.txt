echo "# flasktemplate" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/ciaranq/flasktemplate.git
git push -u origin master

git remote add origin https://github.com/ciaranq/flasktemplate.git
git push -u origin master



#!/bin/bash
# My git script

# git init
read -p "Adding - Press enter to add all"
git add ./
read -p "Enter commit message: " commit
git commit -m "$commit"
#git remote add origin https://github.com/ciaranq/flasktemplate.git
read -p "Pushing - Press enter to push"
git push -u origin master

echo "all done "

