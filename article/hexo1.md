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
先展示一下部署在github上的hexo博客界面
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108072129639.jpg)

这是半年前部署在腾讯云上的wordpresss
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108072129263.jpg)

---

要说谁更好看。。。见仁见智吧
wordpress是动态站点，功能强大，可以整很多好活，其次是可以做到快速部署，技术门槛比hexo低很多，缺点是比较臃肿，访问速度一般
hexo是静态站点，访问速度要优于wordpress，部署还是需要掌握一定的git和Node.js

### 成本
从成本上来说wordpress每年100多的腾讯云服务器就个人来说还是有些稍贵，这还是学生优惠，之后续费将会非常肉疼。
而hexo利用Github pages服务搭建hexo博客是免费的。

### 维护性
虚拟主机，可以在设置面板中一键安装，非常方便。云服务器的话要麻烦一些。部署好之后登陆即可发布博客，而且 wordpress 功能强大，易于维护，但是成本较高。而且博客一般会有配图，而且如果后期要迁移图床的话也比较麻烦。

hexo配合github也能做到一键部署、发布。而且利用picgo, gitnote这些git服务管理工具用起来非常方便

[toc]
# hexo安装

下面记录一下我整hexo的思路和遇到的一些问题

# hexo安装
### 安装Node.js


