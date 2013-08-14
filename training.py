from haproxy import HAProxyConfig
from haproxy import Global
my_config = Global('configs/1.conf')
print my_config.getParams('maxconn')
