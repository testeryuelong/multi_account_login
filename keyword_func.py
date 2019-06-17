import time
from selenium import webdriver

"定义全局变量driver"
driver=""

def startBrowser(*args):
    "启动浏览器"
    global driver
    if len(args)==0:
        driver=webdriver.Chrome(executable_path="D:\\chromedriver.exe")
    elif len(args)==1:
        if args[0]=="chrome":
            driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
        elif args[0]=="firefox":
            driver = webdriver.Firefox(executable_path="D:\\geckodriver.exe")
        elif args[0]=="ie":
            driver = webdriver.Ie(executable_path="D:\\IEDriverServer.exe")
        else:
            print ("无法启动不知名的浏览器")
    else:
        print ("无法识别浏览器")

def accessWebsite(url):
    "访问网页"
    global driver
    driver.get(url)

def forcedWait(duration):
    "强制等待时长"
    time.sleep(int(duration))

def switchIframes(xpathExpression):
    "切换进入指定的iframe"
    global driver
    iframe=driver.find_element_by_xpath(xpathExpression)
    driver.switch_to.frame(iframe)

def inputWords(xpathExpression,words):
    "清空输入框并输入内容"
    global driver
    inputBox=driver.find_element_by_xpath(xpathExpression)
    inputBox.clear()
    inputBox.send_keys(words)

def buttonClick(xpathExpression):
    "点击按钮操作"
    button=driver.find_element_by_xpath(xpathExpression)
    button.click()

def assertString(s):
    "断言字符串"
    global driver
    assert s in driver.page_source

def closeBrowser():
    "关闭浏览器"
    global driver
    driver.close()