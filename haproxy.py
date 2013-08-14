
SECTIONS = ['global','listen', 'frontend', 'defaults', 'backend']

class HAProxyConfig():
    def __init__(self, config_path):
	self.config_path = config_path
	self.config = self.getConfig(self.config_path)
	self.globalh = self.getGlobal()
	
    def getSection(self, section):
	f = open(self.config_path)
	lines = f.readlines()
	f.close()
	for line in lines:
	    line = line.strip()
	    
	    if section in SECTIONS:
		if section in line:
                    print line
	        elif line.startswith(" "):
		    print line
		elif line.startswith("#"):
		    continue
	        elif line in section:
		    break 
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
