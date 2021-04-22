# from selenium import webdriver
import unittest

from ft_home import NewVisitorTest


class FtMain:

    def __init__(self):
        self.ft_home = NewVisitorTest()
        self.test = unittest.main(warnings='ignore')

    def functional_tests(self):
        print("Tests Fonctionnels pour la HP :")
        self.ft_home(self.test)


if __name__ == "__main__":
    main = FtMain()
    main.functional_tests()
