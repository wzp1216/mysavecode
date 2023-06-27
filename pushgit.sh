@echo off
 
title GIT一键提交
color 3
echo 当前目录是：%cd%
echo;
 
echo 本地主分支拉取远程主分支：git pull origin master
git pull 
echo;

echo 开始添加变更：git add .
git add .
echo;
 
set /p declation=输入提交的commit信息:
git commit -m "%declation%"
echo;
 
echo 将变更情况提交到远程自己分支：git push 
git push 
echo;
 

echo 执行完毕！
echo;
 
pause
