#linux基础

###debian与centos的常见区别
>debian和centos的区别还是很大的，但是对于我们使用者来说，记住如下几个区别暂时够用了

|功能|debian命令|centos/redhat命令|
| :--- | :----: | ----: |
|软件包管理器|apt|yum
|包管理器|deb包用dpkg|rpm包用rpm
|服务管理|systemcd|service

###debian apt用法介绍
>apt在正常使用之前需要配置软件源，配置文件为/etc/apt/souces.list

```shell
>>>echo "deb xxxxx.com/xxxx" >>/etc/apt/souces.list
>>>apt-get clean
>>>apt-get update
```

|命令|说明|备注|
| :--- | :----: | ----: |
|apt-get|apt最常用的工具，用于安装删除等操作|我们绝大多数对系统的软件包的操作都可以使用它来完成
|apt-get install package|安装xxx软件包|安装软件包的同时也会安装这个软件包对应的所有依赖，可能依赖不满足，依赖冲突，或者丢失，这都是常见现象
|apt-get remove package|删除软件包|删除软件包的时候也可能要删除对应的依赖，而依赖配置出现错误页会导致其他软件可能用不了
|apt-get install --reinstall package|重新安装某个软件包|有的时候我们会需要重新安装以达到更新配置或者被改乱了的软件
|apt-get -f install package|修复软件包|自动尝试修复某些软件包的安装问题，比如依赖问题，配置问题
|apt-get remove package - - purge|删除包和配置文件|删除配置文件重装软件往往是一种无奈的问题解决方式，当然有效的很
|apt-get update| 更新源|用于更新软件仓库列表，但是不安装软件，注意和yum的区别
|apt-get upgrade|更新已经安装的软件包|这句话可以理解为更新系统
|apt-get dist-upgrade| 升级系统|顾名思义，系统升级，同时也会更新所有软件包
|apt-cache show package|获取软件包信息|
|apt-cache search package|根据关键字搜索软件包|搜索结果一般很多，我们还要进行详细过滤或者配合show命令来找我们想要的
|apt-get source package|下载源码|有时候我们需要手动改动一些东西然后重新编译，这个时候需要源码
|apt-get clean && sudo apt-get autoclean|清理apt缓存和无用的包|更多时候是为了释放硬盘空间
|apt-get check|检查是否有损坏的依赖|这个对于系统工程师很重要
|apt-cache depends package|了解当前包使用的依赖|这对系统工程师很重要
|apt-cache rdepends package|查看该包被哪些程序依赖|这对系统工程师很重要
|sudo apt-get build-dep package|安装相关编译环境
