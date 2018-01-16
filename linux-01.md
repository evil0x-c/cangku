# linux基础

### debian与centos的常见区别
>debian和centos的区别还是很大的，但是对于我们使用者来说，记住如下几个区别暂时够用了

|功能|debian命令|centos/redhat命令|
| :--- | :----: | ----: |
|软件包管理器|apt|yum
|包管理器|deb包用dpkg|rpm包用rpm
|服务管理|systemcd|service

### apt/yum用法介绍
>apt是debian系统的包管理工具,yum是一个在Fedora和RedHat以及SUSE中的Shell前端软件包管理器

apt配置源的方法
```shell
>>>echo "deb xxxxx.com/xxxx" >>/etc/apt/souces.list
>>>apt-get clean
>>>apt-get update
```
yum配置源的方法
```shell
>>>cd /etc/yum.repos.d/ #进入目录
>>>mv CentOS-Base.repo CentOS-Base.repo.bak #备份之前的源
>>>wget http://mirrors.163.com/.help/CentOS6-Base-163.repo #下载新的源
>>>mv CentOS6-Base-163.repo CentOS-Base.repo #改个名字
```

|apt命令|说明|yum命令|
| :--- | :----: | ----: |
|apt-get|apt最常用的工具，用于安装删除等操作|yum
|apt-get install package|安装或升级xxx软件包|yum install package只负责安装， yum update package负责升级
|apt-get remove package|删除软件包|yum remove package
|apt-get install --reinstall package|重新安装某个软件包|有的时候我们会需要重新安装以达到更新配置或者被改乱了的软件
|apt-get -f install package|修复软件包|自动尝试修复某些软件包的安装问题，比如依赖问题，配置问题
|apt-get remove package - - purge|删除包和配置文件|删除配置文件重装软件往往是一种无奈的问题解决方式，当然有效的很
|apt-get update| 更新源|每次运行yum时自动执行,注意与apt的区别
|apt-get upgrade|更新已经安装的软件包|yum update
|apt-get dist-upgrade| 升级系统|yum upgrade
|apt-cache show package|获取软件包信息|
|apt-cache search package|根据关键字搜索软件包|yum search package
|apt-get source package|下载源码|有时候我们需要手动改动一些东西然后重新编译，这个时候需要源码
|apt-get clean && sudo apt-get autoclean|清理apt缓存和无用的包|yum clean, yum clean all
|apt-get check|检查是否有损坏的依赖|这个对于系统工程师很重要
|apt-cache depends package|了解当前包使用的依赖|yum deplist package
|apt-cache rdepends package|查看该包被哪些程序依赖|rpm -q -whatrequires 
|sudo apt-get build-dep package|安装相关编译环境|没有对应命令
|apt-file search /file/name|搜索所有提供某个文件的软件包|yum provides /file/name
|dpkg -l|显示所有已安装的软件|yum list installed
|没有这个命令|列出所有软件包的信息,如果指定 软件名则列出某个软件的信息|yum info
|没有这个命令|列出所有已安裝的软件包信息|yum info installed
### dpkg/rpm包管理器用法
>dpkg是Debian系统的后台包管理器,类似RPM。也是Debian包管理系统的中流砥柱,负责安全卸载软件包,配置,以及维护已安装的软件包

|dpkg命令|说明|rpm
| :--- | :----: | ----: |
|dpkg –l | 显示所有已安装的软件|rpm -qa
|dpkg -s package| 查看已经安装的指定软件包的详细信息|rpm -qpi pkg.rpm
|dpkg -L package| 列出一个包安装的所有文件清单，很实用的功能|rpm -qpd pkg.rpm
|dpkg -S file |查看系统中的某个文件属于哪个软件包|rpm -qf /file/name
|dpkg -i xxx.deb| 安装指定deb包，后面必须是deb包|rpm -i pkg.rpm
|dpkg -R |后面加上目录名，用于安装该目录下的所有deb安装包，一般不建议这样用
|dpkg -r package |remove，移除某个已安装的软件包|rpm -e package
|dpkg -P package| 彻底的卸载，包括软件的配置文件|没有对应命令
|dpkg -c |查询deb包文件中所包含的文件|rpm -qpl pkg.rpm
|dpkg -L |查看系统中安装包的的详细清单|rpm -qpl pkg.rpm

### 简单的命令演示
>linux 基础命令有上千个，这个命令常用的也很多，并不是所有人都善于记忆所有的命令，下面介绍命令的常用格式和语法

```shell
>>> date #显示时间
>>> date +%F 显示日期
>>> head /etc/passwd #显示文件的开头
>>> tai /etc/passwd #显示文件的结尾
```
#### tab补全
>shell的命令很多，有的比较长，或者忘记了准确的拼写，就算是为了少敲几个键盘也是有意义的，所以大家可以尽可能的使用tab热键，但是tab毕竟本身只是一个小工具，性能也一般，如果对于文件超级多的目录，使用tab会让终端出现短暂的卡死现象。如果linux默认tab没有补全请按照bash-completion这个软件包

#### history 命令
>history命令是一个特别的命令，它可以显示之前我们操作的终端的记录，如果我们有什么命令执行过想查询可以通过这个命令

```shell
>>>history#查看执行命令历史
>>>!1 #执行history中的第1编号的命令
```
#### 编辑命令行
>终端的命令行有的时候会很长，如果我们有敲错的地方肯定不能重新敲所有的地方，因此需要使用一些快捷键来帮助我们编辑，当然不使用也可以。

|快捷键|说明|
| :--- | :----: | 
|ctrl+a|跳到命令行的开头
|ctrl+e|跳到命令行的末尾
|ctrl+u|将光标处到命令行开头的内容清除
|ctrl+k|将光标到末尾的内容清除
|Ctrl+H |删除光标的前一个字符
|Ctrl+W |删除光标前的单词(Word, 不包含空格的字符串)
|ctrl+r|在历史记录中搜索某个曾经使用过的命令
|ctrl+l|清理屏幕
|ctrl+c|中断当前执行的程序
|ctrl+p|上翻历史执行命令，相当于光标上键
|ctrl+n|下翻命令，相当于光标下键
|Ctrl+Z| 把当前进程放到后台（之后可用''fg''命令回到前台）
|Shift Insert|粘贴（相当于Windows的Ctrl V）
|鼠标中间|在命令行窗口选中即复制,在命令行窗口中键即粘贴，可用Shift Insert代替

#### linux文件系统层次结构
```shell
>>>/usr #安装软件和共享库
>>>/etc #特定于此系统的配置文件
>>>/run #自上一次系统启动以来启动的进程的运行时数据
>>>/home #非root账户的家目录，另外有的账户也没有家目录
>>>/root #root的家目录
>>>/tmp  #临时文件目录
>>>/boot #boot启动过程所需文件的目录
>>>/dev #设备目录，里面有真实的硬件设备，也有虚拟的硬件设备
>>>/mnt #挂载硬盘的目录
>>>/media #挂载软盘的目录
>>>/var #日志和其他临时信息存储目录
```
#### 命令行文本管理
>这里我们将学习到文本的创建，移动，修改，复制粘贴删除等操作

```shell
>>>touch testfile #创建一个空文件
>>>echo "this is a test" > testfile #利用重定向方法创建一个文件
>>>vim testfile #通过文本编辑器创建文件
>>>mv file1 file2 #移动文件或者改名字或者移动后改名字
>>>mv -f file1 file2 #强制移动，如果有同名直接覆盖
>>>mv -i file1 file2 #如果遇到 同名提示
>>>rm file #删除文件
>>>rm -f file #强制删除文件
>>>rm -i file #删除前询问
>>>mkdir dir1 #创建目录
>>>mkdir -p /home/xxx/xx/xx/xx #创建多层级目录

```
