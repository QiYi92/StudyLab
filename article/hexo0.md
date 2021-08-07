---
title: hexo奇怪BUG报错总结
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
---

* #### hexo d向github部署博客后 ERROR Deployer not found: git

$ hexo d
```
npm install --save hexo-deployer-git
```

* #### hexo博客页面乱码
例如
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108071729506.png)
解决办法：
找到对应页面的配置文件，例如友链就是friends.json，主副标题就是_config.yml
重新保存为