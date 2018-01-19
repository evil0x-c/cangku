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
>这里主要讲搜索和正则表达式基础用法，这个相比基本操作稍微高级一点，暂时可以称为中级用法，主要讲创建简单的正则表达式，使用正则表达式搜索文件和文件系统
，结合使用正则表达式和 sed。

```shell
# 匹配０个以上字符的任何字符串
？任何一个字符
～当前家目录
[abc..] 括起来集合中的任何一个字符
[!abc...]不在括号的集合中的任何一个字符

```
### 文件系统权限
>我们使用chmod来修改文件的权限，这里面有符号法和数值法

|权限|对文件的影响|对目录的影响|
| :--- | :----: | ----: |
|r（读取）| 可以读取文件的内容|可以列出目录的内容（文件名）
|w(写入)|可以更改文件的内容|可以创建或删除目录中的任何一文件
|x（执行）|可以作为命令执行文件|可以创建或者删除目录中的任意文件

|权限|对文件的影响|
| :--- | :----: |
|u|代表用户
|g|代表组
|o|代表others
|a|代表全部
|r=4|４代表读权限
|w=2|2代表写权限
|x=1|１代表执行权限

```shell
>>> chmod o+x file1 #给file1　其他用户执行权限
>>> chmod o-w file1 ＃其他用户没有file1的写权限
>>> chmod 755 file  #给file当前用户的读写执行，当前组的读执行，其他用户的读执行
>>> chmod -R g+rwX dir #给我文件夹权限需要使用-R选项，x要大写
```

### 监控和进程


### service和systemd控制服务
>service 和systemd是两个不同的东西，cnetos中7一下的版本是service，这个工具是用来管理服务的，systemd是centos7以后的版本，debian目前普遍使用的服务管理器，当然systemd不仅仅是管理服务，还管理着计算机的启动后的一切的事情和系统日志，和使用service的系统有显著的差别，下面介绍一下这两个的用法

```shell
>>>service <service> status #查看某服务的状态
>>>service <service> start #启动某个服务
>>>service <service> stop #关闭某个服务
>>>service <service> restart #重启某个服务
>>>chkconfig <service> on #设置指定服务<service>开机时自动启动
>>>chkconfig <service> off #设置指定服务<service>开机时不自动启动。
 
```
```shell
>>> systemd-analyze #打印系统启动时间，因为systemd接管了init，所以它也就可以计算启动时间
>>> systemd-analyze blame #以进程初始化所占用时间排序打印出所有正在运行的单元列表
>>> systemctl #打印所有正在运行的单元
>>> systemctl list-unit-files 列出所有可用的单元
>>> systemctl list-unit-files –type=service #列出所有服务，systemd还可以管理服务之外的其他单元
>>> systemctl --failed #查看启动失败的服务
>>> systemctl start httpd.service #启动某个服务
>>> systemctl restart httpd.service #重新启动某个服务
>>> systemctl stop httpd.service #停止某个服务
>>> systemctl reload httpd.service #重载某个服务
>>> systemctl status httpd.service #检查服务的状态及信息
>>> systemctl is-active mysql.service #检查服务是否在运行
>>> systemctl enable mysql.service #设置开机启动
>>> systemctl disable mysql.service #禁止开机启动
>>> systemctl mask ntpdate.service #禁用某个服务
>>> systemctl unmask ntpdate.service #从禁用中恢复服务
>>> systemctl kill crond #杀死某个服务
>>> systemctl reboot #重启
>>> systemctl halt #停止
>>> systemctl suspend #挂起
>>> systemctl hibernate #休眠
>>> systemctl hybrid-sleep #休眠系统或使系统进入混合睡眠 
```

### nmcli 配置网络连接


