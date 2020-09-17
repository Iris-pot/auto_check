# auto_check
西财校外自动打卡

[TOC]

## 功能

实现 西南财经大学-swufe移动校园2.0-学生每日校外打卡 脚本。

- 自动打卡
- 可指定时间执行打卡
- 有日志记录

为了保障同学的账号密码隐私，请自行输入账号密码并运行程序（当然你愿意托管给我也ok）。

校友路过求个star呗~ 比心~

欢迎提建议~

## 环境依赖

### python 环境:

```python
pip install selenium
pip install logging
pip install apscheduler
```

### chromedriver驱动

chromedriver的版本需要与Chrome的版本一致。

附下载地址（三选一）：

> https://chromedriver.chromium.org/downloads
>
> http://chromedriver.storage.googleapis.com/index.html
>
> https://npm.taobao.org/mirrors/chromedriver/

注：

我的chrome浏览器版本是：版本 85.0.4183.102（正式版本） （64 位），下载的chromedriver的版本是85.0.4183.87，没有报错。

## 使用方法

1. 在 auto_check.py 文件中，填写data字典，写入用户的登录账号、密码、所在省、市、区、地址信息。

    （请确保用户的账号、密码正确，确保省、市、区的对应关系正确。）

2. 每日运行 auto_check.py 。

## 文件说明

| 文件名             | 作用     | 使用方法                 |
| ------------------ | -------- | ------------------------ |
| auto_check.py      | 自动打卡 | 每日运行一次（可关机）   |
| auto_check_cron.py | 自动打卡 | 只需运行一次（不能关机） |

## 定时任务执行方式

1. 最推荐的一种实现方式是，腾讯云函数！待我调试好了会更新。

2. 在linux上创建定时任务，运行auto_check.py。方式：crontab -e。但是配置环境太麻烦了~

3. 运行auto_check_cron.py。需保证你的电脑一直不关机，即可每日自动打卡。

     



