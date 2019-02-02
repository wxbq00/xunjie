from selenium import  webdriver
from threading import Thread
from log.log import Log
log=Log()
CONFIG_FILE = r'/Users/Tiernan/Desktop/projects/wcn_selenium/case/config/config.yml'

DATA_PATH = r'C:\Users\Administrator\PycharmProjects\xunjie\data'
DRIVER_PATH=r'C:\Users\Administrator\PycharmProjects\xunjie\drivers\chromedriver.exe'
LOG_PATH = r'C:\Users\Administrator\PycharmProjects\xunjie\log'
REPORT_PATH = r'C:\Users\Administrator\PycharmProjects\xunjie\report'

def startBrowser(name,url):#浏览器兼容性
    driver=None
    try:
        if name=='chrome' or name=='Chrome':
            driver=webdriver.Chrome(DRIVER_PATH)
            return driver
        elif name == "firefox" or name == "Firefox" or name == "ff":
            driver=webdriver.Chrome(DRIVER_PATH)
            return driver
        else:
            log.info('没有此浏览器')
    except Exception as e:
        log.info('异常:%s'%str(e))

    driver.get(url)
    driver.implicitly_wait(30)
    driver.maximize_window()

if __name__ == '__main__':
    data={
        'chrome':'http://app.xunjiepdf.com/pdf2word',
        'firefox':'http://app.xunjiepdf.com/pdf2word'

    }

    threads=[]
    for a,url in data.items():
        t=Thread(target=startBrowser,args=(a,url))
        threads.append(t)

    for t in threads:
        t.start()








