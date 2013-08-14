from haproxy import HAProxyConfig
for i in range(1,6):
    my_config = HAProxyConfig('configs/%d.conf' %i)
    print "Config", str(i)
    print "--------"
    print my_config.getSection('backend')
    print ""
    print ""
