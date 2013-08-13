class HAProxyConfig():
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = self.getConfig(self.config_path)
        self.globalh = self.getGlobal()

    def getSection(self):
        f= open(self.config_path)
        lines= f.readlines()

        for line in lines:
            line = line.strip()
            if  line == 'global':
                print line

            elif line.startswith("\S"):
                print line

            else:
                break
        
        return 1


    def getGlobal(self):
        return 1

    def getConfig(self, config_path):
        config_file = open(config_path)
        config = config_file.read()
        config_file.close()
        return config

class Global():
    def __init__(self): 
	return 1
