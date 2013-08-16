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
        self.params = [] 
        for param in config_array:
            param_name = self.getOptName(param).strip()
            params = self.getOpts(param).strip()
            pdict = {'name' : param_name, 'params' : params }
            self.params.append(pdict)
			
    def getOptName(self, param):
        return param.split()[0]
	
    def getOpts(self, param):
        return ' '.join(param.split()[1:])

    def getParam(self, name):
        params = []
        name = name.strip()

        for param in self.params:
            if name == param['name']:
                params.append(param['params'])
        return params 
		
    def getParamAll(self, opt):
        params1 = []
        params2 = []
        opt = opt.strip()

        for param in self.params:
            if opt == param['name']:
                params1.append(param['params'])
                params2.append(param['name'])
        return params1 + params2
	
    def addParam(self, param_name, *params):
        add = {'name': param_name, 'params': params}
        self.params.append(add)
        return True
    
    def remParam(self, param_name, *params):
        rem = {'name': param_name, 'params': params}
        self.params.remove(rem)
        return True
    
	def getConfigGlobal(self):
	    param = param.split()
        flag = False

        for param in self.config_array:
            sparam = param.split()[0]
            if param == '':
				continue
            if sparam == 'global':
                flag = True
            if sparam == 'defaults':
                break
            if flag == True:
                print param
        return self.config_array


