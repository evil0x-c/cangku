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



