# -*-coding:utf-8 -*-
# @Author : Zhigang

from read_data import readLoginData,readStepData
from keyword_func import *

def main():
    """将读取的操作步骤进行拼接映射到关键字函数中，然后读取多个账户进行循环登录"""
    for key,value in readLoginData("loginInfo.txt").items():
        # print (key,value)
        for step in readStepData("step.txt"):
            # print (step)
            if step[0]=="inputWords" and step[2]=="username":
                command="%s('%s','%s')" % (step[0],step[1],key)
            elif step[0]=="inputWords" and step[2]=="password":
                command="%s('%s','%s')" % (step[0],step[1],value)
            elif len(step)==1:
                command = "%s()" % step[0]
            else:
                command="%s('%s')" % (step[0],step[1])
            # print (command)
            eval(command)

if __name__=="__main__":
    main()