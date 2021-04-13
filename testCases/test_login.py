import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage

class Test_001_Login:
    baseurl = "https://admin-demo.nopcommerce.com"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homePageTitile(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        if act_title == "Your store. Login123":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_homePageTitile.png")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration123":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_login.png")
            self.driver.close()
            assert False
