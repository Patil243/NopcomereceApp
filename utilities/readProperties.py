import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('comon info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        user_name = config.get('comon info', 'username')
        return user_name

    @staticmethod
    def getPassword():
        password = config.get('comon info', 'password')
        return password