from haproxy import HAProxyConfig
from haproxy import Global

my_config = HAProxyConfig('configs/5.conf')
print my_config.globalh.addParam('asdas', 'asdas', 'sdada', 'sadad')
print my_config.globalh.remParam('asdas', 'asdas', 'sdada', 'sadad')
