MySQL:是用于管理文件的一个软件
-服务端软件
    1：socket服务端
    2：本地文件操作
    3：解析指令[SQL语句]
-客户端软件（各种各样）
    1:socket客户端
    2：发送指令
    3：解析指令[SQL语句]
-DBMS:数据库管理系统


技能：
-安装服务端和客户端
-连接
-学习sql与规则：指示服务端做任意操作


-安装服务端和客户端
（1）安装
双击安装dmg文件>
默认安装地址：/usr/local/mysql
（2）配置
启动完成后,打开终端，open ~/.bash_profile,添加下面三条

export PATH=${PATH}:/usr/local/mysql/bin

alias mysql=/usr/local/mysql/bin/mysql

alias mysqladmin=/usr/local/mysql/bin/mysqladmin

source ~/.bash_profile 使得配置文件生效



（3）修改密码：
mysqladmin -u root -p password 新密码



（4）进入数据库
mysql -u root -p

(5)mysql文件夹权限问题：
当时情况：无法进入，打开/usr/local/mysql/data/ ：permission denied

解决方法
sudo chown -R _mysql:admin /usr/local/mysql/data/

sudo chmod -R u+rwX,g+rwX,o-rwx /usr/local/mysql/data/


(6)查看、杀死进程
ps -ef | grep mysql
sudo kill 26625


-连接
alias mysqlstart='sudo /usr/local/mysql/support-files/mysql.server start'
alias mysqlstop='sudo /usr/local/mysql/support-files/mysql.server stop'


-数据库结构

   文件夹【数据库】
        文件【表】
            数据行【行】
            数据行【行】
            数据行【行】







