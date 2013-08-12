class HAproxyConfig():
    def __init__(config_path):
        self.config_path = config_path
        self.config = self.getConfig(self.config_path)
        self.global = self.getGlobal()
        
        print config_path

    def getGlobal(self):
        return 1

    def getConfig(self, config_path):
        config = open(config_path).read()
        return config()
    

class Global():
    def __init__(self):
