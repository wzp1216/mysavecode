 
CURRENT_DIR=$(pwd) 
echo git-pull-add-push:$CURRENT_DIR 
echo;
 
echo 本地主分支拉取远程主分支：git pull 
git pull  
echo;

echo 开始添加变更：git add .
git add . 
echo;
 
set 提交的commit信息为时间；
git add -u;
git commit -m "changed files on `date +'%Y-%m-%d %H:%M:%s'`";
echo;
 
echo 将变更情况提交到远程自己分支：git push 
git push 
echo;
 

echo 执行完毕！
echo;
 
