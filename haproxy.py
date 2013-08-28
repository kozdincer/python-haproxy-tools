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

        #Set Listen.
        self.listens = []
        for name in self.getListenNames():
            l = Listen(self.getListen(name), name)
            self.listens.append(l)

        # Set Frontends.
        self.frontends = []
        for name in self.getFrontendNames():
            f = Frontend(self.getFrontend(name), name)
            self.frontends.append(f)

        #Set Backend.
        self.backends = []
        for name in self.getBackendNames():
            b = Backend(self.getBackend(name), name)
            self.backends.append(b)

    def getSection(self, section, name=None):
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
                if name == None:
                    start_flag = True
                    continue

                else:
                    if name in line:
                        start_flag = True
                        continue

                    else:
                        start_flag = False

            if sline in SECTIONS:
                start_flag = False

            if start_flag:
                config_array.append(line)
        return config_array
    def getGlobal(self):
        return self.getSection('global')

    def getDefaults(self):
        return self.getSection('defaults')

    def getListen(self, name):
        return self.getSection('listen', name=name)

    def getFrontend(self, name):
        return self.getSection('frontend', name=name)

    def getBackend(self, name):
        return self.getSection('backend', name=name)

    def getConfig(self, config_path):
        config_file = open(config_path)
        config = config_file.read()
        config_file.close()
        return config

    def getListenNames(self):
        l_names = []
        rows = self.config.split('\n')
        for row in rows:
            row = row.strip()
            if row.startswith('listen'):
                name = row.split()[1]
                l_names.append(name)
        return l_names

    def getFrontendNames(self):
            f_names = []
            rows = self.config.split('\n')
            for row in rows:
                row = row.strip()
                if row.startswith('frontend'):
                    name = row.split()[1]
                    f_names.append(name)
            return f_names

    def getBackendNames(self):
        b_names = []
        rows = self.config.split('\n')
        for row in rows:
            row = row.strip()
            if row.startswith('backend'):
                name = row.split()[1]
                b_names.append(name)
        return b_names

class Option():
    def __init__(self, param_name, params):
        self.name = param_name
        self.params = params

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return str(self.name + " " + " ".join(self.params))

    def getRow(self):
        return self.__repr__()

    def getParamName(self):
        return self.name

    def getParams(self):
        return self.params

class Section():
    def __init__(self, config_array):
        self.config_array = config_array
        self.options = []
        self.title = ''
        for row in config_array:
            param_name = self.getParamName(row).strip()
            params = self.getParams(row)
            option = Option(param_name, params)
            self.options.append(option)

    def getParamName(self, row):
        return row.split()[0]

    def getParams(self, row):
        return tuple(row.split()[1:])

    def getConfig(self):
        options = self.options
        config_output = "%s" %self.title + " " +"%s\n" %self.name
        for param in self.options:
            config_output += '    ' + str(param).strip() + '\n'
        return config_output

    def addOption(self, option):
        self.options.append(option)
        return True

    def delOption(self, option):
        for opt in self.options:
            if opt == option.name:
                self.options.remove(opt)
        return True
    def setOption(self, option):
        for opt in self.options:
            if opt.name == option.name:
                opt.params = option.params
        return self.options

class Global(Section):
    def __init__(self, config_array):
        Section.__init__(self, config_array)
        self.title = 'global'

class Defaults(Section):
    def __init__(self, config_array):
        Section.__init__(self, config_array)
        self.title = 'defaults'

class Listen(Section):
    def __init__(self, config_array, name):
        Section.__init__(self, config_array)
        self.title = 'listen'
        self.name = name

class Frontend(Section):
    def __init__(self, config_array, name):
        Section.__init__(self, config_array)
        self.title = 'frontend'
        self.name = name

class Backend(Section):
    def __init__(self, config_array, name):
        Section.__init__(self, config_array)
        self.title = 'backend'
        self.name = name
