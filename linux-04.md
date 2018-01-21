# linux 系统加固


### ssh 加固
>加固之前升级你的ssh
如果权限不对，更改权限
```shell
>>>chmod 644 /etc/ssh/sshd_config
```
打开/etc/ssh/sshd_conf文件
```shell
PermitRootLogin no #这里面root能不用ssh就不用，尽量别改yes
PermitEmptPasswords no ＃这个设置是否允许口令为空，很显然要选择no
PassworAuthentication yes ＃设置是否允许口令登录，根据实际情况来改
```
打开/etc/ssh/ssh_config
```shell
CheckHostIP yes #设置ssh是否查看连接到服务器的主机的ip防止ＤＮＳ欺骗
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
### ftp加固
```shell
anonymous_enable=NO　＃设置不能匿名访问
userlist_deny=NO　设置为no并在vsftpd.userlist指定可登录用户
vim /etc/vsftpd/vsftpd.userlist #去掉root防止爆破
```
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

[相关内容](http://blog.csdn.net/knight_zhen/article/details/46444451)
