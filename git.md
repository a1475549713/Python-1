Github 导图 -Windows		首先你的有github账号！！！
1 ：下载git 
2： pycharm-setting-version control-github 填github户名密码
3： pycharm-setting-version control- git 填git.exe安装路径
4:  pycharm-setting-tool -  Terminnal  填 git-bash.exe 路径 （此步关联pycharm与bash 既可以在pycharm上操作git命令）
----至此，基本配置已完毕，下面git配置
5：配置git个人信息

-- $ git config --global user.name "runoob"    用户名
--$ git config --global user.email test@runoob.com  邮箱地址
-- git config 配置文件命令 
 		-- glabal 参数作用为全局  Windows下路径 c:/user /administrator /.gitconfig
--也可以 --system   读取配置为git安装目录下 /etc/gitconfig
Git config --list可以查看当前所有配置  
--默认使用最后一个 
--如：
--user.name = ‘xxx’  user.emai  = ‘xxxx’
--remote.xxx.url = ‘xxxxx’  remote.xxx.fetch = ‘xxxx’
-- 如遇WARNING: terminal is not fully functional  系统环境变量新建 			TERM --cygwin
6：创建ssh关联github
--$ ssh-keygen -t rsa -C "youremail@example.com"  此命令会在主目录下生成id_rsa.pub		文件，打开复制所有内容到github右上角 --setting -SSH and gpg keys  张贴
--也可以生成多个！
验证： $ ssh -T git@github.com
如果他跟你说HI 就是成功了
*--至此git与pycharm github已关联完成，接下来可以愉快的在本地与远程操作代码了

7：上传项目到Github 	  比较类似数据库的操作

--首先你得有个仓库！！！
--pycahrm --VCS -- import into version control --share project on github 				-shareanyway -填仓库名称 
--当然也可以在github上直接新建一个
-- $ git remote add [shortname][url]  填项目名称 URL
--至此，github仓库与本地git已关联完成
-- 上传代码到github
1：Pycharm -vcs -commit （默认全部）选好你要的代码 commit message 输入描述，		右下角commit
 //或者 pycharm  git-add  步骤同
2：Pycharm -vcs -git-push 这里会看到你commit的代码 -push
或者：
$ git add xxxx 你要添加的文件
$ git commit -m ‘xxxx’ 对此操作的注释
$ git push -u origin master
注意！！此处 默认是origin  如果github上有多个仓库，此处改成仓库名
或者

8：获取远程代码：
 $ git pull xxxx master  
 		---xxxx为你的仓库名  master为分支，默认为主分支
删除远程代码
$ git rm -r --cached xxxx 文件名
..... 
可删除多个
$git commit -m ‘操作注释’
$git push xxxx master 

对远程代码修改
Git pull 会自动同步当前代码。
--如果报错	fatal: refusing to merge unrelated histories
-- git pull --rebase
如果当前代码有修改
--git status / git commit，先提交




9：其他  常用操作
Config文件修改
git config --global --list 查看当前工作配置文件
git config  --global --add user.name 增加一个用户
git config  --global --unset user.name 修改
git remote add  name url 增加一个远端库
git reset --hard FETCH_HEAD  版本回退！！好用，慎用
git reflog 查看版本纪录
git reset --hard HEAD@{1}  回到本地代码1的位置
git remote -v 查看当前远端库及地址
git init 初始化

清空所有commit
1.Checkout git checkout --orphan latest_branch 新建一个分支
2.添加所有文件 git add -A
3.提交更改 git commit -m "commit message"
4.删除分支 git branch -D master11
5.将当前分支重命名为 master git branch -m master
6.最后，强制更新您的存储库 git push -f “仓库名” maste




这真的是极好用的东西！！！！
！！！！千万注意工作目录
 ---- 至此基础git已基本掌握

