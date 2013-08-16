from haproxy import HAProxyConfig
from haproxy import Global

my_config = HAProxyConfig('configs/5.conf')
print my_config.globalh.AddParam('deneme1', 'deneme2', 'deneme3', 'deneme4')
print my_config.globalh.RemoveParam('deneme1','deneme2','deneme3','deneme4')
