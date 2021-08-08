---
title: 【浅谈】基于github托管，利用hexo+picgo+gitnote构筑一套带图床的完整个人博客生态
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
  - hexo
---
@[toc](目录)
# 前言
先展示一下部署在github上的hexo博客界面
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108072129639.jpg)

这是半年前部署在腾讯云上的wordpresss
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108072129263.jpg)

---

要说谁更好看。。。见仁见智吧
wordpress是动态站点，功能强大，可以整很多好活，其次是可以做到快速部署，技术门槛比hexo低很多，缺点是比较臃肿，访问速度一般
hexo是静态站点，访问速度要优于wordpress，部署还是需要掌握一定的git和Node.js

比较过后我还是将博客从wordpress迁移到hexo

## 成本
从成本上来说wordpress每年100多的腾讯云服务器就个人来说还是有些稍贵，这还是学生优惠，之后续费将会非常肉疼。
而hexo利用Github pages服务搭建hexo博客是免费的。

## 维护性
虚拟主机，可以在设置面板中一键安装，非常方便。云服务器的话要麻烦一些。部署好之后登陆即可发布博客，而且 wordpress 功能强大，易于维护，但是成本较高。而且博客一般会有配图，而且如果后期要迁移图床的话也比较麻烦。

hexo配合github也能做到一键部署、发布。而且利用picgo, gitnote这些git服务管理工具用起来非常方便



下面记录一下我整hexo的思路和遇到的一些问题

# hexo安装
## 安装Node.js
首先下载稳定版

[Node.js传送门](https://link.zhihu.com/?target=https%3A//nodejs.org/dist/v9.11.1/node-v9.11.1-x64.msi)

安装选项全部默认，一路点击Next。

最后安装好之后，按Win+R打开命令提示符，输入node -v和npm -v，如果出现版本号，那么就安装成功了。

安装完成后添加淘宝的镜像进行加速
```
npm config set registry https://registry.npm.taobao.org
```

## 安装git
了把本地的网页文件上传到github上面去，我们需要用到分布式版本控制工具————Git
```
https://link.zhihu.com/?target=https%3A//git-scm.com/download/win
```
安装选项还是全部默认，只不过最后一步添加路径时选择Use Git from the Windows Command Prompt，这样我们就可以直接在命令提示符里打开git了。

安装完成后在命令提示符中输入git --version验证是否安装成功。

## 安装hexo


## 连接github和域名解析

# matery主题安装

# 


