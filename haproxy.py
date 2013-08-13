
SECTIONS = ['global','listen', 'frontend', 'defaults', 'backend']

class HAProxyConfig():
    def __init__(self, config_path, section):
        self.config_path = config_path
        self.config = self.getConfig(self.config_path)
        self.globalh = self.getGlobal()
	
    def getSection(self, section):
	self.section = section
	f= open(self.config_path)
        lines= f.readlines()
	if line.split()[0] in SECTIONS:
           for line in lines:
               line = line.strip()
	       start =0
	       if start == 0:
	       
	         if "#" in line:
	             start =1
	         elif line == section:
	             start =0
                 elif line.startswith(SECTIONS):
		     start =1
	         else:
		     start =0
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
