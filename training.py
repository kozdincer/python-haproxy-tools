from haproxy import HAProxyConfig
from haproxy import Global

my_config = HAProxyConfig('configs/5.conf')
print my_config.globalh.getParam('user')

