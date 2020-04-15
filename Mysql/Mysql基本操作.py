///安装与配置
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


///数据类型

(1）数字
int
tinyint
bigint

FLOAT 单精度
DOUBLE 双精度
decimal 十进制小数，永远是精准的



（2）字符串
-char(长度) ：如果没有占满，会自动填上空格；查找速度快
最多255个字符
-varchar(长度)：如果没有占满，不会自动增加空格，节省空间，但是查找速度没有char快
最多255个字符
数据库优化：定长的一定用char,不定长的可以用varchar，并放在后面
-text
最多65535个字符


（3）时间类型
DATE
TIME
DATETIME #常用
TIMESTAMP


（4）枚举enum
create table shirts(name char(10)，size enum('s','xs','l','xl','xxl'));
insert into shirts(name,size) values('dog','s') #插入的values必须是中规定的选项

（5）set
create table shirts(name char(10)，size set('x','s','l'));
insert into shirts(name,size) values('dog','s') #插入的values必须是set中的组合





#如果上传文件，将文件存在某个文件服务器的硬盘中，然后将文件路径存在数据库中








///
数据库基本操作

(1)创建用户（默认是root，）
- create user 'yayan' identified by 'wsxxx,yyqxxxxx'

(2)给用户授权
#grant 权限 on 某个数据库.某文件 to 用户
-grant select,insert,update on yayandb1.* to 'yayan';

#all privileges 是除了grant权限之外的所有操作权限
-grant all privileges on yayandb1.* to 'suisui'

#移除权限
-remoke all privileges from yayandb1.* to 'suisui'



（3）创建,删除数据库
create databases yayandb1;
drop databases yayandb1;

(4)查看数据库
show databases;


(5)进入某个数据库：
use yayandb1;
select database(); #查看当前数据库



(6)查看当前数据库的所有表：
show tables;


（7）查看某个表内容
select * from 表名 #查看全部表内容
select 列名，列名 from 表明 #查看某些列内容

(8)创建/删除/更改表
create table 表名(列名1 数据类型 null/not null,表名2 字符类型(最多字符数量，超出则忽略))
-create table user(id int auto_increment primary key,name char(20),gender char(10),is_admin int default '0');
#如果一列是递增的，必须是一个key
#auto_increment步长：
    # set sesstion auto_increment_increment=2；
    # 基于会话，登录登出后就恢复墨迹人
#primary key 是一个约束，不能为空，也不能重复，加速查找
#一个表里只能有一个自增列，也只能有一个primary key

#引擎：engine=innodb 事务性，出错后会回滚到上一次状态


#清除表内容
delete from yayant2;  （但是如果重新插入，自增的仍然会从上次记录继续）
truncate table yayant2;  (会清空自增的记录)

#删除表
drop table yayant1;

#查看表的结构
desc 表名;

#修改表名
alter table yyblog rename yyblognew;

#添加表列
alter table yyblog add column 列名 列数据类型；

#删除表列
alter table yyblog drop column 列名；

#修改表列类型
alter table yayant
change 列名
列名 列数据类型 (default '默认值')





(9)数据表记录的增删改查：
查看：
    表所有数据：
        -select *  from user;
    表特定字段的数据：
        -select id,gender from user;

    where 查找：
        -select * from user where id >=2 and gender='male';

    like +% 模糊查询：
       -select * from user where name like '%n%';

    limit： 仅取X条数据
        -select * from post limit 10;


    union:将两个表的查询结果从上往下接合（查询column数量要相同）
        -select gender,name from user where id>2 union select body,title from post where id>2;


    排序desc/asc：
        select * from user order by id desc;从大到小
        select * from post order by id asc;从小到大

    分组：group by
        # 就是将数据根据相同的gender值分组，返回里那个Count(gender)就是每个组的出现数量
        -select Count(gender),gender from user group by gender;
        -对于聚合函数结果进行二次筛选，必须使用having 代替where
        select name from table group by name having min(score)>80

(12)分组:将列字段相同的数据进行分组
select count(id),kind from yyblog group by kind;
可以使用sql函数，对这个分组进行计算
count,max,min,sum,avg



insert into post(title,body,author_id) value('post7-title','post7-body',3);
增：
- insert into yayant1(name,gender,is_admin) values('yayan','female','yes')

#字符编码问题：
insert into yayant1(num,hobbie) values(2,'吃吃吃');
#解决方法：创建数据库和表的时候设置默认编码方式
create databases yayandb1 default charset utf8;
create table yayant1(num int,hobbie char(10)) default charset=utf8;



删：
delete from yayant1 where id=6;
#问题：删除某行数据后，自增仍然从上次的记录开始
#解决方法：alter table yyblog auto_increment=6;（后面新添加的数据的id是从6开始计数）

改（update+where）：update 表名
update user set gender='male' where name='xue';



(10) 外键 ：
当一张表1的某一列的数据有重复的，切这些列数据来自另外一张表2的某一列，则在表1内，可以直接用在表2内，数据对应的id
#例子：
t1                       t2
部门：                 id    部门
保安  1                 1   保安
前台  2                 2   前台
行政  3                 3   行政
前台  2
行政  3
保安  1
保安  1


#好处
（1）节省空间
（2）约束：t1部门这一列的数据只能是t2 id 这里一类的数据

#创建表时添加：
-create table t1(列名 列数据类型，外键列名 列数据类型,constraint 外键名(随意起) foreign key(外键列名) references 外表表名(该外键对应的在外表的字段名))

#已经创建好了表，再增加外键约束
alter table user add constraint 外键名(随意起) foreign key(外键字段名) references 外表表名(该外键对应的在外表的字段名);
ex:
1.先创建表post;
create table post(id int auto_increment primary key,title char(30),body text(65535),author_id int) engine=innodb;
2.为post表的author_id 指定为外键，这个外键是由user表的id来约束的
alter table post add constraint fk_skdjf foreign key (author_id) references user(id);




（11）
-唯一索引：
create table t1(id int,num int,unique uqq(num))

约束不能重复（可以为空）
主键不能重复（不能为空）

-外键的变种：外键加唯一索引约束(一对一)






(12)join：
内连接
-select A.stu_name,B.class from student_info as A join class_info as B on A.id = B.id;
-要查询的表中有至少一个匹配，则返回行

左连接
-select A.stu_name,B.class from student_info as A left join class_info as B on A.id = B.id;
-从左表(join左边的表)返回所有的行贴在，如果右表会根据匹配数据来显示没有匹配则以NULL补全

右连接
-select A.stu_name,B.class from student_info as A right join class_info as B on A.id = B.id;
-从右表(join右边的表)返回所有的行，如果左表中没有匹配则以NULL补全


(13)Mysql视图：给某个查询语句设置别名，日后方便使用，成为创建sql视图
（工作中不要使用视图）
create view v1 as sql语句;
select * from v1;

(14)触发器：一旦执行一条sql语句，会自动在这条sql之前之后执行另一条sql语句
#先修改终止符号
delimiter//
create trigger tri_before_delete_t1 before delete on t1 for each row
    begin
    sql
    end


create trigger tri_after_delete_t1 after delete on t1 for each row begin
begin
sql
end


(15)存储过程:保存在mysql上的一个别名》一坨sql语句

delimiter //
create procedure a1()
BEGIN
    select * from account;
    delete from account where id=1;
    #insert into account(name,password) values('')
    alter table account drop id;
    alter table account add column id int not null auto_increment primary key first;
END//
delimiter ;

call a1();



