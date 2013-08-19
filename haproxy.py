"""
Copyright (C) 2013 - Aybuke Ozdemir <aybuke.147@gmail.com>

This file is part of python-haproxy-tools

python-haproxy-tools is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

python-haproxy-tools is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>

"""

from utils import *

class HAProxyConfig():

    def __init__(self, config_path):
        self.config_path = config_path
        self.config = self.getConfig(self.config_path)
		
        self.globalh = Global(self.getGlobal())
        self.defaults = Defaults(self.getDefaults())
        self.listen = Listen(self.getListen())
        self.frontend = Frontend(self.getFrontend())
        self.backend = Backend(self.getBackend())
	
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
        self.title = 'global'
        self.config_array = config_array	
        self.params = [] 
        for param in config_array:
            param_name = self.getOptName(param).strip()
            params = self.getOpts(param)
            pdict = {'name' : param_name, 'params' : params }
            self.params.append(pdict)
			
    def getOptName(self, param):
        return param.split()[0]
	
    def getOpts(self, param):
        return tuple(param.split()[1:])

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
                params1.append(param['name'])
                params2.append(param['params'])
        return params1 + params2
	
    def addParam(self, param_name, *params):
        sdict = {'name': param_name, 'params': params}
        self.params.append(sdict)
        return True
    
    def remParam(self, param_name, *params):
        sdict = {'name': param_name, 'params': params}
        self.params.remove(sdict)
        return True

    def getConfigGlobal(self):
        params = self.params
        config_output = ""
        config_output += self.title + '\n'
        for param in self.params:
            config_output += '    ' + str(param).strip() + '\n'
        return config_output

class Defaults():
	def __init__(self, defaults_array):
		self.defaults_array = defaults_array
		self.title = 'defaults'
		self.array = []
		for param in defaults_array:
			defaults_name = self.getDefaultsName(param).strip()
			array = self.getDefaultsParam(param)
			dictd = {'name': defaults_name, 'params': array}
			self.array.append(dictd)

	def getDefaultsName(self, param):
		return param.split()[0]

	def getDefaultsParam(self, param):
		return tuple(param.split()[1:])
    
	def getDefaults(self, name):
		array = []
		name = name.strip()

		for param in self.array:
			if name == param['name']:
			    array.append(param['params'])
		return array
	
	def getDefaultsAll(self, option):
		defaults1 = []
		defaults2 = []

		option = option.strip()

		for param in self.array:
			if option == param['name']:
				defaults1.append(param['name'])
				defaults2.append(param['params'])
		return defaults1 + defaults2

	def addDefaults(self, defaults_name, *defaults_param):
		dictd = {'name': defaults_name, 'params': defaults_param}
		self.array.append(dictd)
		return True

	def remDefaults(self, defaults_name, *defaults_param):
		dictd = {'name': defaults_name, 'params': defaults_param}
		self.array.remove(dictd)
		return True

	def getConfigDefaults(self):
		array = self.array
		config_output = ""
		config_output += self.title + '\n'
		for param in self.array:
			config_output += '    ' + str(param).strip() + '\n'
		return config_output

class Listen():
    def __init__(self, listen_array):
        pass

class Frontend():
	def __init__(self, fronted_array):
		pass

class Backend():
	def __init__(self, backend_array):
		pass
