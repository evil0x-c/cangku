# linux基础二

### 用户和组
>管理本地账户，创建账户，删除账户，更改账户信息

```shell
>>> sudo useradd tester1 #没有使用任何群组相关的参数，默认在创建用户 tester1 的同时会创建一个同名的群组。用户 tester1 的初始群组就是这个新建的群组。
>>> sudo useradd tester2 -g sudo # 创建新账户并指定群组，如果不指定默认是同名组
>>> sudo useradd tester3 -G sudo #创建账户并附加到sudo组，test3的组本身也存在
>>> sudo useradd -m tester4 #创建账户的时候同时创建家目录
>>> sudo useradd -d /home/abcd -m tester5 #创建自己指定的名字的家目录

```

### 文件管理二
>这里主要讲搜索和正则表达式基础用法

### 监控和进程


### service和systemd控制服务

### nmcli 配置网络连接


