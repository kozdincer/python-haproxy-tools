
SECTIONS = ['listen', 'frontend', 'defaults', 'backend']

class HAProxyConfig():
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = self.getConfig(self.config_path)
        self.globalh = self.getGlobal()

    def getSection(self, section):
        f= open(self.config_path)
        lines= f.readlines()

        for line in lines:
            line = line.strip()
	    
	      start =1 
	      if start == 1:
	       
	      if "#" in line:
	          start = 0
	      elif line == section:
	           start = 0
	       elif line in SECTIONS:
                   start =0
	       elif line.startswith("listen"):
		   start =0
	       elif line.startswith("frontend"):
		   start =0
	       elif line.startswith("backend"):
		  start =0
	       else:
	           print line 
		    
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
