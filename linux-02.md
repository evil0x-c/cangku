# linux基础二

### 用户和组
>管理本地账户，创建账户，删除账户，更改账户信息

```shell
>>> sudo useradd tester1 #没有使用任何群组相关的参数，默认在创建用户 tester1 的同时会创建一个同名的群组。用户 tester1 的初始群组就是这个新建的群组。
>>> sudo useradd tester2 -g sudo # 创建新账户并指定群组，如果不指定默认是同名组
>>> sudo useradd tester3 -G sudo #创建账户并附加到sudo组，test3的组本身也存在
>>> sudo useradd -m tester4 #创建账户的时候同时创建家目录
>>> sudo useradd -d /home/abcd -m tester5 #创建自己指定的名字的家目录
>>> sudo userdel tester1 #删除tester1账户，但是保留它的家目录，万一有有用的文件呢
>>> sudo userdel -r tester1 #删除tester1账户和它的家目录
>>> sudo userdel -f  tester1 #强制删除某个账户
```
>useradd常见的一些用法

```shell
>>> sudo useradd -m -s /bin/bash tester1 # 创建一个带有家目录并且可以登录 bash 的用户
>>> sudo useradd -m -d /home/xxx tester2 # 指定创建用户家目录的路径
>>> sudo useradd -s /sbin/nologin tester3 #创建一个没有家目录且不能登录的用户,这个多用于安全配置
>>> sudo useradd -m -G sudo tester4 #创建账户并附加到sudo组
```
>usermod的一些用法举例

```
　-c<备注> 　修改用户帐号的备注文字。
　-d登入目录> 　修改用户登入时的目录。
　-g<群组> 　修改用户所属的群组。
　-G<群组> 　修改用户所属的附加群组。
　-l<帐号名称> 　修改用户帐号名称。
　-L 　锁定用户密码，使密码无效。
　-s<shell> 　修改用户登入后所使用的shell。
　-u<uid> 　修改用户ID。
　-U 　解除密码锁定
```
```shell
>>> usermod -G staff newuser2 #将 newuser2 添加到组 staff 中
>>> usermod -l newuser1 newuser #修改 newuser 的用户名为 newuser1
>>> usermod -L newuser1 #锁定账号 newuser1
>>> usermod -U newuser1 #解除对 newuser1 的锁定
>>> usermod -s /bin/ksh -d /home/z –g developer sam #此命令将用户sam的登录Shell修改为ksh，主目录改为/home/z，用户组改为developer
```
>用户口令管理，指定和修改用户口令的Shell命令是passwd。超级用户可以为自己和其他用户指定口令，普通用户只能用它修改自己的口令。命令的格式为：

```shell
>>>passwd #修改当前账户的密码
>>>passwd tester1 #修改tester1的密码
>>>passwd -d sam #sam用户空口令
>>>passwd -l sam #锁定用户
```

>linux 用户组管理,用户组的管理涉及用户组的添加、删除和修改。组的增加、删除和修改实际上就是对/etc/group文件的更新
```shell
>>> groupadd group1 #此命令向系统中增加了一个新组group1
>>> groupadd -g 101 group2 #此命令向系统中增加了一个新组group2，同时指定新组的组标识号是101
>>> groupdel group1
>>> groupmod -g 102 group2 #改变group2的gid
>>> groupmod –g 10000 -n group3 group2 #此命令将组group2的标识号改为10000，组名修改为group3

```
### 文件管理二
>这里主要讲搜索和正则表达式基础用法

### 监控和进程


### service和systemd控制服务

### nmcli 配置网络连接


