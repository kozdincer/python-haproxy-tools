class HAproxyConfig():
    def __init__(self, config_path):
    	self.config_path = config_path
    	self.config = self.getConfig(self.config_path)
        self.globalh = self.getGlobal()
        
        print config_path

    def getSection(self):
    	f= open(self.config_path)
        lines= f.readlines()

        for line in lines:
            if  line.strip() == 'global':
              print line

            elif line.startswith(" "):
               print line

            elif line.strip() == 'defaults':
               break
        return 1


    def getGlobal(self):
        return 1

    def getConfig(self, config_path):
        config = open(config_path).read()
        return config

class Global():
    def __init__(self): 
	return 1
