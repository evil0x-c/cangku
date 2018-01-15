#linux基础

###debian与centos的常见区别
>debian和centos的区别还是很大的，但是对于我们使用者来说，记住如下几个区别暂时够用了

|功能|debian命令|centos/redhat命令|
| :--- | :----: | ----: |
|软件包管理器|apt|yum
|包管理器|deb包用dpkg|rpm包用rpm
|服务管理|systemcd|service

###debian apt用法介绍

|命令|说明|备注|
| :--- | :----: | ----: |
|apt-get|apt最常用的工具，用于安装删除等操作|我们绝大多数对系统的软件包的操作都可以使用它来完成
|apt-get install package|安装xxx软件包|安装软件包的同时也会安装这个软件包对应的所有依赖，可能依赖不满足，依赖冲突，或者丢失，这都是常见现象
|apt-get remove package|删除软件包|删除软件包的时候也可能要删除对应的依赖，而依赖配置出现错误页会导致其他软件可能用不了
|apt-get install --reinstall package|重新安装某个软件包|有的时候我们会需要重新安装以达到更新配置或者被改乱了的软件
|apt-get -f install package|修复软件包|自动尝试修复某些软件包的安装问题，比如依赖问题，配置问题
|apt-get remove package - - purge|删除包和配置文件|删除配置文件重装软件往往是一种无奈的问题解决方式，当然有效的很
|apt-get update| 更新源|用于更新软件仓库列表，但是不安装软件，注意和yum的区别
