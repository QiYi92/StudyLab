---
title: 【教程】在VMware基于linux ubuntu虚拟机安装ucore
date: 
author: galileocat
img: 
top: false
cover: false
coverImg: 
password: 
toc: false
mathjax: false
summary: 教程随笔
categories: 教程
tags:
  - 教程
  - linux
---
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108072048759.jpeg)
最近在学堂在线上学习操作系统这门课

实验环境一般是使用蓝桥的实验楼

但蓝桥的虚拟机上不方便你在本地记录和保存代码

所以我打算在本地用VMware上完成Ucore操作系统的实验课

实验课的源码在github上很容易就能搜索到，这边放一下链接记录一下
[>>>Github项目地址<<<](https://github.com/kiukotsu/ucore)

---

这门课的实验一共有几种实验方法
一就是[实验楼](https://www.lanqiao.cn/courses/221/learning/)，好处就在方便，不用配置环境，直接用就行
不方便的地方就在保存源码困难

二是Windows环境，环境配置也是比较麻烦
Github里面也提供了链接，需要的朋友可以自己去下载

三是在VirtualBOX和VMWare进行实验
问题就在Github上提供了.vdi格式的安装包，这个格式只支持VirtualBOX，如果要使用VMware进行实验还需要进行转换

所以还是需要下载VirtualBOX   [[下载地址]](https://www.virtualbox.org/)
我使用的是VirtualBOX自带的VBoxManage进行转换
安装完毕后在VirtualBOX会看到**VBoxManage.exe**就说明成功了

把需要转换的vdi安装包放到一个知道路径的位置
然后在命令行进入到VirtualBOX目录下输入指令
```
VBoxManage clonehd f:\mooc-os-2015.vdi e:\mooc-os-2015.vmdk -- foormat vmdk
```
这条指令的意思是把f盘根目录下的xxxx.vdi转换成vmdk存入e盘的根目录，地址根据你的目录自己调整
之后就得到了vmdk格式的安装包了
最后导入VMware就行了

。。。

最后在启动虚拟机时候发生了一个问题
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108072052264.png)
啊。。这

也不难解决

解决这个问题要启动bios，重启进入bios
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108072056914.jpeg)
各个电脑进入bios的方法都不一样，我这边是微星主板，重启时狂按delete就行了
然后依次 OC ————> 其他设置 ——> CPU特征 ——>SVM Mode ——> 允许
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108072059838.jpeg)
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108072059118.jpeg)
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108072100917.jpeg)

记得保存
完美解决！

