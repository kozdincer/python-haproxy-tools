class HAProxyConfig():
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = self.getConfig(self.config_path)
        self.globalh = self.getGlobal()
        print config_path
        print "-----"
        print self.config

    def getSection(self, section_name)
        return 1

    def getGlobal(self):
        return 1

    def getConfig(self, config_path):
        config = open(config_path).read()
        return config
    

class Global():
    def __init__(self):
        pass
