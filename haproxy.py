class HAProxyConfig():
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = self.getConfig(self.config_path)
        self.globalh = self.getGlobal()
<<<<<<< HEAD
        
=======
>>>>>>> 7b75b0429daa7aa9c57a679e578feb79239b5792
        print config_path
        print "-----"
        print self.config

    def getSection(self, section_name)
        return 1

    def getGlobal(self):
        return 1
    
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


    def getConfig(self, config_path):
        config = open(config_path).read()
        return config
    

class Global():
    def __init__(self):
<<<<<<< HEAD
	return 1
=======
        pass
>>>>>>> 7b75b0429daa7aa9c57a679e578feb79239b5792
