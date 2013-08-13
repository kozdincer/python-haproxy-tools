from haproxy import HAProxyConfig
my_config = HAProxyConfig('configs/1.conf', 'global')
my_config.getSection()
