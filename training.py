from haproxy import HAProxyConfig
from haproxy import Global

my_config = Global('configs/2.conf')
print my_config.getParams('maxconn')
