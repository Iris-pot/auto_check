# auto_check
Automatic Pickling outside the SWUFE campus

[TOC]

## Feature

Implement Southwest University of Finance and Economics - SWUFE Mobile Campus 2.0- Student daily off-campus check-in script.

-Automatic clock-in
-Clock-in can be executed at a specified time
-Logged

To ensure the privacy of the account password of the classmates, please enter the account password and run the program (of course you are willing to host it to me).



## Environment

### Python Environment:

```python
pip install selenium
pip install logging
pip install apscheduler
```

### Chromedriver Driver

Chromedriver's version needs to be consistent with the Chrome version.

Attached download address (choose one from three):

> https://chromedriver.chromium.org/downloads
>
> http://chromedriver.storage.googleapis.com/index.html
>
> https://npm.taobao.org/mirrors/chromedriver/

Note:

My Chrome browser version is: version 85.0.4183.102 (official version) (64-bit), and the version of the download of the download of the download is 85.0.4183.87.

## HOW TO USE

1. In the Auto_check.py file, fill in the data dictionary, and write the user's login account, password, province, city, district, and address information.


2. Daily run auto_check.py

## File Description

| File             | Function     | HOW TO USE                 |
| ------------------ | -------- | ------------------------ |
| auto_check.py      | Automatic clock in | Run once a day (can be turned off)   |
| auto_check_cron.py | Automatic clock in | Only need to run once (cannot shut down)  |

## Timing Task Execution Method

1. Create a regular task on Linux and run auto_check.py. Method: Crontab -e.

2. Run auto_check_cron.py。You need to ensure that your computer is not shut down, you can automatically check in daily.

     
