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

在你希望存放自己博客文件的地方新建一个文件夹，我自己直接存放在E盘的**blog**文件夹内
之后在此文件夹右键打开`Git Bash Here`
！！！注意储存路径不能有中文！！！
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108081612202.png)
以后对博客的所有操作都在这个git控制台执行
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108081613162.png)
输入`npm i hexo-cli -g`安装Hexo
安装完成后输入`hexo -v`如果出现版本号说明安装成功
接着输入`hexo init`初始化文件夹
`hexo g`生成静态网页
`hexo s`打开本地服务器
之后在浏览器输入**localhost:4000**查看，可以发现博客已经部署在我们本地服务器上了
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108081715997.png)
这算是一个预览状态，以后做的所有操作例如更新文章，修改主题，都要在本地预览，无误后再上传github服务器
确认无误后`ctrl+c`关闭本地服务器


## 连接github和域名解析
github就不多说了，没注册去注册
注册完后新建一个项目仓库
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108081724541.png)
注意这里仓库名称一定是这个格式
`你的github名.github,io`
不能起其他名字，这一点很重要
例如我id是QiYi92，那么我博客仓库起名就是`QiYi92.github.io`
以后如果你不设置自己的域名，那直接在浏览器里输入这个仓库名就可以连接到你自己的博客

## git秘钥配置
1. 本地安装好git；

2. 桌面右键 Git Bash Here 打开git命令行；

3. `ssh-keygen -t rsa -C "nideyouxiang@xxx.com"`   （全部按enter）；

4. `cd ~/.ssh`   （如果没有执行第三步，则不会有这个文件夹）；

5. `cat id_rsa.pub`     在命令行打开这个文件，会直接输出密钥；

6. 复制即可，打开github   ，点自己头像 >> settings >> SSH and GPG keys >>New SSH key 

7. title写blog key里把秘钥粘贴上去就完事

测试
输入`ssh -T git@github.com`如果出现你的用户名就说明成功了

打开博客根目录下的_config.yml这是博客的配置文件，可以在这里修改各种信息

修改最后一行的配置
```
deploy:
  type: git
  repo: git@github.com:QiYi92/QiYi92.github.io.git
  branch: main
```
这里repo填的就是你博客仓库的地址
branch是你博客储存的主要分支，因为我们新建仓库时主要分支是main，那这里就填main。

如果两边分支不一样`hexo d`上传时候就会出错或发现更新无效，例如一些教程是master，而你仓库是main，这就导致很多人在这里踩坑



## 绑定域名
这里我用腾讯云的域名为例，阿里云也差不多
如何购买域名+实名一系列问题就不慢慢写了
这里只写如何添加域名
解析
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108081739741.jpg)
添加@和www两条解析记录,记录类型选CNAME，记录值是你的默认网址也就是仓库名
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108081744039.png)
然后打开你的github博客项目，点击settings，拉到下面Custom domain处，填上你自己的域名

# matery主题安装
**这里有个坑需要说一下**
你的博客文件一共有两个最重要配置文件`_config,yml`
一个是根目录的_config，另一个是 themes\hexo-theme-matery 里面的主题`_config.yml`
你的基本设置是跟着前者走，而主题图片特效这些是跟着后者，看教程的时候一定要注意是在哪个`_config.yml`进行操作

如何配置matery主题还是matery作者自己写的官网文档靠谱，网上很多教你如何配置主题的帖子要不就是没写完全或者已经过时了。
## 官方文档传送门

[matery中文说明文档](https://github.com/blinkfox/hexo-theme-matery/blob/develop/README_CN.md)

按着文档走完一遍的时候你的博客已经基本上成型了

# Gitnote文章编写发布及储存方案
我们写博客的时候最宝贵的是文章数据，很多博客系统在数据的保管和迁移的方面做的实在是一言难尽，这里我提供一个非常方便编写和储存的方案

## Gitnote下载
首先我们先下载Gitnote
[Gitnote下载传送门](https://www.gitnoteapp.com/)
[Gitnote使用视频教程](https://player.bilibili.com/player.html?aid=43903167&cid=76908079&page=1)

GitNote 是一款基于 Git 来管理内容的免费跨平台笔记软件，它支持 Windows、macOS 以及 Linux 三大平台 (未来还会支持移动端)。软件直接内置了 Git 支持，你无须在本地安装或配置 Git，你的笔记即能拥有 Git 的特性，比如可以任意的恢复笔记的版本记录等

## Gitnote使用
gitnote安装好后是这样
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108081819792.png)


在github上创建一个 **私有** 笔记仓库用来做笔记托管，这个仓库一定要与博客仓库**保持独立**
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108081811441.png)

接着我们把笔记仓库的SSH复制到gitnote上克隆仓库
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108081823150.png) 
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108081824005.png)
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108081826995.png)
克隆完成后就可以在Gitnote里完成你自己的文章编辑
支持markdown语法
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108081829291.png)

如果你是编写hexo文章还需要在头部添加hexo的`front-matter`
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108081833053.png)

都知道hexo博客储存在根目录的`\source\_posts`文件夹内，等你写完一篇文章后直接将`文章.md`从你电脑上的笔记库粘贴到_post库里
再在git bash里输入
```
hexo clean && hexo g
hexo d
```
即可完成发布

---

而且你会发现你的文章已经自动同步到github笔记仓库里面了

如果需要迁移直接整个文件打包带走~非常方便

![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108081811357.png)

# Picgo图床
PicGo是一款比较优秀的图床工具。它是一款用 Electron-vue 开发的软件，可以支持微博，七牛云，腾讯云COS，又拍云，GitHub，阿里云OSS，SM.MS，imgur 等8种常用图床，功能强大，简单易用

一般如果不使用图床，你的图片会存放在_post的文章文件夹内，这对于博客迁移来说是非常不方便的，所以依旧是借助github的托管来做一个图床

## Picgo下载

[Picgo传送门](https://github.com/Molunerfinn/PicGo/releases)

## Picgo使用
我们先创建一个图床仓库
**！注意仓库属性一定要设置为公共，如果是私有库的图片是无法被访问的**
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108081847123.png)
创建好后，需要在 GitHub 上生成一个 token 以便 PicGo 来操作我们的仓库，来到个人中心，选择 Developer settings 就能看到 Personal access tokens，我们在这里创建需要的 token
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108081850474.webp)
点击 Generate new token 创建一个新 token，选择 repo，同时它会把包含其中的都会勾选上，我们勾选这些就可以了。然后拉到最下方点击绿色按钮，Generate token 即可。之后就会生成一个 token ，记得复制保存到其他地方，这个 token 只显示一次！！


这里我使用的是picgo 2.3.0的beta版
![](https://cdn.jsdelivr.net/gh/QiYi92/ImageHost/img/202108081845263.png)