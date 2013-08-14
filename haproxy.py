SECTIONS = ['global','defaults', 'listen', 'frontend', 'backend']

class HAProxyConfig():


	def __init__(self, config_path):
		self.config_path = config_path
		self.config = self.getConfig(self.config_path)
		
		self.globalh = self.getGlobal()
		self.defaults = self.getDefaults()
		self.listen = self.getListen()
		self.frontend = self.getFrontend()
		self.backend = self.getBackend()
	def getSection(self, section):
		config_array = [] 
		section = section.strip()
		start_flag = False

		f = open(self.config_path)
		lines = f.readlines()
		f.close()
        
		for line in lines:
			line = line.strip()
			if line == '':
				continue
            
			sline = line.split()[0]
            
			if sline == section:
				start_flag = True
				continue
            
			if sline in SECTIONS:
				start_flag = False
            
			if start_flag:
				config_array.append(line)
        
		return config_array
	
	def getGlobal(self):
		return getSection('global')

	def getDefaults(self):
		return getSection('defaults')

	def getListen(self):
		return getSection('listen')

	def getFrontend(self):
		return getSection('frontend')

	def getBackend(self):
		return getSection('backend')

	def getConfig(self, config_path):
		config_file = open(config_path)
		config = config_file.read()
		config_file.close()
		return config

class Global():
	def __init__(self): 
		return 1
