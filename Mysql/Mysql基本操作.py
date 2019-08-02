(1)创建用户（默认是root，）
- create user 'yayan' identified by 'wssyy,yyqx1128'

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
select databases(); #查看当前数据库



(6)查看当前数据库的所有表：
show tables;


（7）查看某个表内容
select * from 表名 #查看全部表内容
select 列名，列名 from 表明 #查看某些列内容

(8)创建/删除/更改表
#create table 表名(列名1 数据类型 null/not null,表名2 字符类型(最多字符数量，超出则忽略))
-create table yayant1(num int,hobbie char(10))
-create table yayant2(id int auto_increment primary key,food char(10));  #如果一列是递增的，必须是一个key
#uto_increment步长：
    # set sesstion auto_increment_increment=2；
    # 基于会话，登录登出后就恢复墨迹人
#primary key 是一个约束，不能为空，也不能重复，加速查找
#一个表里只能有一个自增列，也只能有一个primary key

#引擎：engine=innodb 事务性，出错后会回滚到上一次状态
-create table yayant1(num int not null auto_increment primary key,sport char(15)) engine=innodb default charset=utf8;


#清除表内容
delete from yayant2;  （但是如果重新插入，自增的仍然会从上次记录继续）
truncate table yayant2;  (会清空自增的记录)

#删除表
drop table yayant1;

#修改表名
alter table yayant3 rename yayant3new;

#添加表列
alter table yayant3 add column 列名 列数据类型；

#删除表列
alter table yayant3 drop column 列名；

#修改表列类型
alter table yayant3 change 列名 新列数据类型

#修改表列名
alter table yayant3 change 列名 新列名 列数据类型




(9)数据表增删改查：

增：
- insert into yayant1(num,hobbie) values(1,'sleep')

#字符编码问题：
insert into yayant1(num,hobbie) values(2,'吃吃吃');
#解决方法：创建数据库和表的时候设置默认编码方式
create databases yayandb1 default charset utf8;
create table yayant1(num int,hobbie char(10)) default charset=utf8;



删：
delete from yayant1 where id<6
#问题：删除某行数据后，自增仍然从上次的记录开始
#解决方法：alter table yayant3 auto_increment=6;

改：
update yayant1 set id=2;
update yayant1 set id=2 where id=3;


查看：
    select ...
    查看排序：
        select * from t1 order by id desc;从大到小
        select * from t1 order by id asc;从小到大
    取最后10条数据：
        select * from t1 order by id desc limit 10;


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

#创建两个表，对表1 某一列进行外键约束
-create t1(列名 列数据类型，列名 列数据类型,constraint 约束名 foreign key （要约束的列名） references 表2名（要连接的列名）)


#已经创建好了的两个表，增加外键约束
alter table yayant3 add constraint fk_kindfk_kindtokind foreign key(kind) references kind(id);


（11）
-唯一索引：
create table t1(id int,num int,unique uqq(num))

约束不能重复（可以为空）
主键不能重复（不能为空）

-外键的变种：外键加唯一索引约束(一对一)


(12)分组:将列字段相同的数据进行分组
select count(id),kind from yayant3 group by kind;
可以使用sql函数，对这个分组进行计算
count,max,min,sum,avg


对于聚合函数结果进行二次筛选，必须使用having 代替where
select count(id),kind from yayant3 group by kind having count(id)>1;


(12)连表操作：两个表的数据组合在一起

select * from yayant3,kind where yayant3.kind=kind.id;

select * from yayant3 left join kind on yayant3.kind=kind.id;


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



