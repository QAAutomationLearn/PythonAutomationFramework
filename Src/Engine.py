#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from Utils.Paths import CHROME_DRIVER_PATH, IE_DRIVER_PATH
from Utils.ParseConfig import parseConfig
from Utils.Logger import logger

WAIT_IMPLICITY_TIMEOUT = parseConfig.time_config('ImplicityWaitTime')
LOCAL_BROWSER_NAME = parseConfig.browser_name()
WINDOW_SIZE = parseConfig.browser_window_size()


class BrowserEngine:
    def __init__(self):
        self.driver = None

    def launch_local_browser(self, local_browser_name=LOCAL_BROWSER_NAME, window_size=WINDOW_SIZE,
                             implicity_wait_timeout=WAIT_IMPLICITY_TIMEOUT):
        """启动本地浏览器"""
        try:
            # 初始化浏览器
            if LOCAL_BROWSER_NAME in ["Chrome", "chrome", "CHORME"]:
                logger.info("Launch {0} browser".format(local_browser_name))
                self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
            elif LOCAL_BROWSER_NAME in ["Firefox", "firefox", "FIREFOX", "FireFox"]:
                logger.info("Launch {0} browser".format(local_browser_name))
                self.driver = webdriver.Firefox()
            elif LOCAL_BROWSER_NAME in ["Ie", "ie", "IE"]:
                logger.info("Launch {0} browser".format(local_browser_name))
                self.driver = webdriver.Ie(IE_DRIVER_PATH)
            else:
                raise NameError
            # 设定浏览器尺寸
            if window_size in ["Max", "max", "MAX"]:
                logger.info("Maximize browser")
                self.driver.maximize_window()
            elif window_size in ["Min", "min", "MIN"]:
                logger.info("Minimize browser")
                self.driver.minimize_window()
            # 设定隐式等待时间
            logger.info("Set implicity wait time to {0}".format(str(implicity_wait_timeout)))
            self.driver.implicitly_wait(implicity_wait_timeout)
            return self.driver
        except NameError:
            logger.error("Fail to launch browser due to incorrect browser name: {0}".format(LOCAL_BROWSER_NAME))
            raise
        except WebDriverException as e:
            logger.error("Fail to launch browser: {0}".format(e))
            raise e
        except Exception:
            logger.exception("Fail to launch browser", exc_info=True)
            raise

    def get_driver(self):
        logger.info("Get current driver, ID: {0}, Driver: {1}".format(id(self.driver), self.driver))
        return self.driver

    def quit_browser(self):
        logger.info("Quit browser and release current driver")
        self.driver.quit()


ENGINE = BrowserEngine()


if __name__ == '__main__':
    browser_engine = BrowserEngine()
    driver = browser_engine.launch_local_browser()
    import time
    time.sleep(5)
    print("{0}=========={1}".format(id(driver), driver))
    browser_engine.quit_browser()
