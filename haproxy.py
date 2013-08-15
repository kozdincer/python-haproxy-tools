from utils import *

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
		return self.getSection('global')

	def getDefaults(self):
		return self.getSection('defaults')

	def getListen(self):
		return self.getSection('listen')

	def getFrontend(self):
		return self.getSection('frontend')

	def getBackend(self):
		return self.getSection('backend')

	def getConfig(self, config_path):
		config_file = open(config_path)
		config = config_file.read()
		config_file.close()
		return config

class Global():


	def __init__(self, config_path):
		self.config_path = config_path
		self.config = self.getConfig(self.config_path)
		self.params = self.getArray()

	def getParams(self, params):
		params_array = []
		flag = False
		f = open(self.config_path)
		lines = f.readlines()
		f.close()
		
		for line in lines:
			if line == '':
				continue
			if params in line:
				flag = True
				continue
			if line in GLOBAL_PARAMS:
				flag = True
			if flag:
				params_array.append(line)
				return params_array

		return params_array

	def getArray(self):
		return self.getParams('maxconn')

	def getConfig(self, config_path):
		config_file = open(config_path)
		config = config_file.read()
		config_file.close()
		return config

