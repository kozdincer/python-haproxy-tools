from utils import *

class HAProxyConfig():


	def __init__(self, config_path):
		self.config_path = config_path
		self.config = self.getConfig(self.config_path)
		
		self.globalh = Global(self.getGlobal())
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

	def __init__(self, config_array):
		self.config_array = config_array	
		self.param_name = self.getParamname(self.config_array)
		self.params = self.getParams(self.config_array)
		param_array = []
		arrayfor_name = []
		arrayfor_params = []

		for param in config_array:
			param_dict = {'param_name' : arrayfor_name, 'params' : arrayfor_params }
			param_array.append(param_dict)
			
			if self.param_name in config_array:
				arrayfor_name.append(param_name)
			if self.params in config_array:
				arrayfor_params.append(params)

		print param_array

	def getParamname(self, param_name):
		pass
	def getParams(self, params):
		pass

	







