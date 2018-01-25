# linux 系统加固


### ssh 加固
>加固之前升级你的ssh
如果权限不对，更改权限
```shell
>>>chmod 644 /etc/ssh/sshd_config
```
打开/etc/ssh/sshd_conf文件
```shell
PermitRootLogin no #这里面root能不用ssh就不用，尽量别改yes,或者改成prohibit password,比赛可能改了配置这是个考点
PermitEmptPasswords no ＃这个设置是否允许口令为空，很显然要选择no
PassworAuthentication yes ＃设置是否允许口令登录，根据实际情况来改
```
打开/etc/ssh/ssh_config
```shell
CheckHostIP yes #设置ssh是否查看连接到服务器的主机的ip防止ＤＮＳ欺骗，可有可无，某些版本应该无效了
```
### http加固
>加固之前升级你的http
打开/etc/httpd/conf/http.conf
```shell
ServerSignature off #回显没有版本号（可能无效，因为centos是需要改源码，而且这个设置比赛是没用的）
ServerTokens Prod #回显没有版本号
Options Indexes FollowSymLinks #删掉Indexes,禁止显示目录结构

```
对目录进行加固
```shell
>>>chown -R apach2.apache2 /var/www/html
>>>chmod -R 2570 /www/html/
```
### php安全设置
>这个设置有别与apache2是在php.ini中
```shell
safe_mode=on 
safe_mode_gid = off
open_basedir = /var/www/html/ 限制只能访问自己的web目录
disable_functions = system,passthru,exec,shell_exec,popen,phpinfo #限制危险的函数
disable_functions = chdir,chroot,dir,getcwd,opendir,readdir,scandir,fopen,unlink,delete,copy,mkdir限制特殊操作
expose_php = Off #限制查看版本信息
magic_quotes_gpc = on #打开魔术引号，防止sql注入
display_errors = Off 禁止打印错误信息防止被黑客利用

```
### ftp加固
```shell
anonymous_enable=NO　＃设置不能匿名访问,防止匿名读取
userlist_deny=NO　设置为no并在vsftpd.userlist指定可登录用户
vim /etc/vsftpd/vsftpd.userlist #去掉root防止爆破
```
### sql加固
>比赛的环境应该是mysql，centos的mysql的初始密码是空的(和debian不同)，sql加固虽然有很多选项，但是实际上考点应该就是设置root密码，并且让web使用普通数据库进行链接。扩展[mysql常见操作](http://linux.it.net.cn/e/data/mysql/2014/1206/9723.html)
```shell
>>> yum install mysql #升级到最新
>>> mysqladmin -u root password "password" #修改root密码，默认密码可能是空，debian这么修改可能不成功
mysql> set password for root@localhost=password('password);#进入mysql修改
mysql> select load_file('d://debug.txt') ;#尝试读取文本内容,查看是否安全，不安全加local-infile = 0
mysql> select 'test' into outfile 'd:/test.txt'; #尝试写入文本内容，查看是否安全
>>>vim /etc/my.cnf ＃查看启动账户是否是root如果是，改成ｍysql
>>>vim /etc/my.cnf ##skip-networking，如果有这个设置打开它，或者添加bind_address=127.0.0.1
>>>vim /etc/my.cnf #skip-show-database 限制普通用户浏览其它数据库

```
或者进入Mysql里面进行修改,这种方式最保险。
```shell
mysql>use mysql;
mysql>select host from user where user='root'; #这里查询下是不是有'%'权限，如果没有就安全
mysql>update user set host = 'localhost' where user = 'root';
```
举个例子，我们要创建一个新的账户，然后给新的账户某个固定数据库的权限，比赛可能不需要做时间来不及
```shell
create database dvwa; #创建一个新的数据库
CREATE USER 'dvwauser'@'localhost' IDENDIFIED BY '123456'; #保证只能本地登录
GRANT ALL ON dvwa.* TO 'dvwauser'@'%localhost';#指定dvwauser只能链接dvwa的数据库
```
[mysql 账户操作参考](http://www.jb51.net/article/31850.htm)

### 常规加固

1删除不必要的用户组
```shell
>>>vim /etc/passwd #修改之前先备份
>>>vim /etc/sudoers#修改之前先备份
>>>vim /etc/group#修改之前先备份
```
２服务用户要保证没有bin/bash的权限
```shell
>>>vim /etc/passwd
```
３删除不必要的软件
```shell
>>>rpm -e python
>>>rpm -e gcc
4关闭不必要的服务
```shell
>>>chkconfig|grep on
```
>>>rpm -e netcat
>>>rpm -e wget
>>>rpm -e curl
>>>rpm -e perl
```
### iptables
>iptables 一般情况不要动，如果配置错误可能导致犯规，根据实际情况，使用iptables的好处是比如mysql远程连接，不用安全配置，在防火墙这里不放行就可以了。
```shell
 iptables -F   #清楚防火墙规则
iptables -L   #查看防火墙规则
iptables -A INPUT -p tcp --dport 80 -j ACCEPT  
iptables -A INPUT -p tcp --dport 22 -j ACCEPT  
iptables -A INPUT -p tcp --dport 21 -j ACCEPT  
iptables -A INPUT -p udp --dport 443 -j ACCEPT  
iptables -A INPUT -p icmp -j ACCEPT  
iptables -P INPUT DROP  
/etc/init.d/iptables save
```
[相关内容](http://blog.csdn.net/knight_zhen/article/details/46444451)

### python如何调试别人的代码
[pdb调试](http://blog.csdn.net/eric_sunah/article/details/56484912)
