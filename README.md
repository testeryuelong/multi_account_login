# multi_account_login
混合驱动框架-多账号登录

思路：
keyword_func.py：关键字函数；

read_data.py:读取文件，获取数据；

run_scripts.py:主程序，将读取的操作步骤进行拼接后映射到关键字函数中，然后遍历多个账户进行登录操作；

loginInfo.txt:账号密码，用/分割；

step.txt:账号登录时的步骤，对应的关键字函数+xpath定位；


登录模块基本都大同小异，利用此框架，只有更改txt文件中的账号信息和xpath定位即可
