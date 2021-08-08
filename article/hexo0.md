---
title: hexo matery奇怪BUG报错排雷总结
date: 
author: galileocat
img: 
top: false
cover: false
coverImg: 
password: 
toc: false
mathjax: false
summary: 解决hexo各种奇怪报错
categories: hexo
tags:
  - hexo
  - 教程
  - debug
---

* ## hexo d向github部署博客后 ERROR Deployer not found: git

$ hexo d
```
npm install --save hexo-deployer-git
```

---

* ## hexo博客页面乱码
例如
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108071729506.png)
解决办法：
找到对应页面的配置文件，例如友链就是friends.json，主副标题就是_config.yml
重新保存为UTF-8格式
这里以vscode为例，编码是用的是GB2312，我们以UTF-8格式保存即可，注意，是通过此编码保存，不是通过此编码打开
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108071733248.png)

---

* ## $ hexo d上传博客后不刷新
输入hexo d之前输入
```
hexo clean && hexo g
```
亦或者分开输入
```
hexo clean
hexo g
```
再输入hexo d上传即可

---

* ## hexo编写完文章不显示在列表中
首先检查git bash后台是否有报错
如果有，说明你文章中有书写不规范的地方
例如
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108071750556.jpg)
这里就是文章front-matter里的summary带了不该带的东西(中括号[])，一般非法字符都可以在报错信息里看到，如果没有就控制变量法挨个筛查就好

---

* ## hexo toc目录不显示异常
现在hexo主题都基本上是自带toc
不需要安装`hexo-toc`插件了
如果有安装`hexo-toc`可以输入以下指令卸载
```bash
npm remove hexo-toc --save
```
之后输入`hexo clean`刷新一遍就好了
最后把文章属性栏添加一行
```
toc: true
```
搞定
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108082359927.png)


### 个人技术博客——二进制的伽利略's Blog
[http://galileocat.cn/](http://galileocat.cn/)


