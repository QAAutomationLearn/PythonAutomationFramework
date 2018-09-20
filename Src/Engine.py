#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from Utils.Paths import CHROME_DRIVER_PATH, IE_DRIVER_PATH
from Utils.ParseConfig import IMPLICITY_WAIT_TIME,  BROWSER_NAME, BROWSER_WINDOW_SIZE
from Utils.Logger import logger


# class BrowserEngine(object):
#
#     logger = Logger().get_logger()
#
#     # 之前考虑过单例模式，但是如果中途调用driver.quit()退出浏览器后，浏览器进程被杀掉，无法再次打开新的浏览器，这应该是和webdriver
#     # 的机制有关。如果真要用单例模式，建议始终保持一个浏览器对象，而调用 driver.close()关闭当前测试的window比较合适
#     def __init__(self, browser_name="Chrome"):
#         self.logger.info("Start to init BrowserEngine")
#         try:
#             if browser_name == "Chrome" or "chrome":
#                 self.logger.info("Instantiate object {0} driver, launch {0} browser".format(browser_name))
#                 self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
#             elif browser_name == "Firefox" or "firefox":
#                 self.logger.info("Instantiate object {0} driver, launch {0} browser".format(browser_name))
#                 self.driver = webdriver.Firefox()
#             elif browser_name == "IE" or "ie":
#                 self.logger.info("Instantiate object {0} driver, launch {0} browser".format(browser_name))
#                 self.driver = webdriver.Ie(IE_DRIVER_PATH)
#             self.logger.info("Maximize browser")
#             self.driver.maximize_window()
#             self.logger.info("Set driver implicity wait time to default 30s")
#             self.driver.implicitly_wait(30)
#         except WebDriverException as e:
#             self.logger.error("Fail to launch browser: {0}".format(str(e)))
#             raise e
#         except Exception:
#             self.logger.exception("Fail to launch browser", exc_info=True)
#             raise
#
#     def Driver(self):
#         self.logger.info("Get current driver, ID: {0}, Driver: {1}".format(id(self.driver), self.driver))
#         return self.driver
#
#     def Quit(self):
#         self.logger.info("Quit browser and release current driver")
#         self.driver.quit()


class BrowserEngine:
    def __init__(self):
        self.driver = None

    def launch_local_browser(self, local_browser_name=BROWSER_NAME, window_size=BROWSER_WINDOW_SIZE,
                             implicity_wait_timeout=IMPLICITY_WAIT_TIME):
        """启动本地浏览器"""
        try:
            # 初始化浏览器
            if BROWSER_NAME in ["Chrome", "chrome", "CHORME"]:
                logger.info("Launch {0} browser".format(local_browser_name))
                self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
            elif BROWSER_NAME in ["Firefox", "firefox", "FIREFOX", "FireFox"]:
                logger.info("Launch {0} browser".format(local_browser_name))
                self.driver = webdriver.Firefox()
            elif BROWSER_NAME in ["Ie", "ie", "IE"]:
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
            logger.error("Fail to launch browser due to incorrect browser name: {0}".format(BROWSER_NAME))
            raise
        except WebDriverException as e:
            logger.error("Fail to launch browser: {0}".format(e))
            raise e
        except Exception:
            logger.exception("Fail to launch browser", exc_info=True)
            raise

    # def launch_remote_browser(self, _command_executor, _desired_capabilities,
    #                           implicity_wait_timeout=WAIT_IMPLICITY_TIMEOUT):
    #     """
    #     启动远程浏览器
    #     :param _command_executor: 远程server地址，如 "http://192.168.98.106:5555/wd/hub"
    #     :param _desired_capabilities: 调用webdriver的DesiredCapabilities的模板
    #     :param implicity_wait_timeout: 隐式等待时间
    #     :return: self.driver
    #     """
    #     logger.info("Launch remote browser")
    #     try:
    #         self.driver = webdriver.Remote(command_executor=_command_executor,
    #                                        desired_capabilities=_desired_capabilities)
    #         logger.info("Maximize browser")
    #         self.driver.maximize_window()
    #         logger.info("Set implicity wait time to {0}".format(str(implicity_wait_timeout)))
    #         self.driver.implicitly_wait(implicity_wait_timeout)
    #         return self.driver
    #     except WebDriverException as e:
    #         logger.error("Fail to launch browser: {0}".format(str(e)))
    #         raise e
    #     except Exception:
    #         logger.exception("Fail to launch browser", exc_info=True)
    #         raise

    def get_driver(self):
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
