# centos比赛场景的服务器场景还原


### centos 自动联网
```shell
>>>cd /etc/sysconfig/network-scripts
>>>vi ifcfg-eth0 #修改ONBOOT=no 改为 ONBOOT=yes
>>>service network restart
```
### HTTP服务的安装
>下面是基础的使用知识，附赠一个php站点的搭建实例[dvwa搭建](http://blog.csdn.net/isinstance/article/details/54090936)
```shell
>>> yum install httpd 
>>> vim /etc/httpd/conf/httpd.conf #apache2的配置(题外话：apt-get install apache2　是一样的)
>>> echo "hello class" > /var/www/html/index.html #写一个首页

```

### FTP服务的安装


### SSH服务的安装

```shell
>>>yum install openssh*#安装ssh服务，对应的(apt-get install ssh)
```
```shell
vi /etc/ssh/sshd_config #打开配置文件
```
把下面两个配置的＃去掉
```shell
PermitEmptyPasswords no
PasswordAuthentication yes
PermitRootLogin yes　＃确保root可以登录，同理如果做安全加固，这里要注释掉
```
重启
```shell
service sshd.service restart #重启服务
chkconfig sshd on　#设置开机启动
```

### GCC的安装
>gcc是c语言程序的编译程序

```shell
>>> yum install gcc* 
```

### python

