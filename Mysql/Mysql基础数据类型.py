（1）数字
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

