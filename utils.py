"""
Copyright (C) 2013 - Aybuke Ozdemir <aybuke.147@gmail.com>

This file is part of python-haproxy-tools.

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

SECTIONS = ['global','defaults', 'listen', 'frontend', 'backend']
GLOBAL_PARAMS = ['ca-base', 'chroot','crt-base', 'daemon', 'gid',
'group', 'log', 'log-send-hostname', 'nbproc', 'pidfile', 'uid',
'ulimit-n', 'user', 'stats', 'node', 'description', 'unix-bind',
'maxconn', 'maxconnrate', 'maxcomprate', 'maxcompcpuusage', 'maxpipes',
'maxsslconn', 'noepoll', 'nokqueue', 'nopol', 'nosplice', 'spread-checks',
'tune.bufsize', 'tune.chksize', 'tune.comp.maxlevel', 'tune.http.cookielen',
'tune.http.maxhdr', 'tune.maxaccept', 'tune.maxpollevents', 'tune.maxrewrite',
'tune.pipesize', 'tune.rcvbuf.client', 'tune.rcvbuf.server', 'tune.sndbuf.client',
'tune.sndbuf.server', 'tune.ssl.cachesize', 'tune.ssl.lifetime', 'tune.ssl.maxrecord',
'tune.zlib.memlevel', 'tune.zlib.windowsize', 'debug', 'quiet']

import subprocess
def isValid(config, section_name):
    string = ''
    cg = """
global
    daemon
    maxconn 256
    """
    if section_name == 'global':
        string += config
    else:
        string += cg

    cd = """
defaults
    mode http
    timeout connect 5000ms
    timeout client 50000ms
    timeout server 50000ms
"""
    if section_name == 'defaults':
        string += config
    else:
        string += cd

    cf = """
frontend http-in
    bind *:80
    default_backend servers
"""
    if section_name == 'frontend':
        string += config
    else:
        string += cf

    cb = """
backend servers
    server server1 127.0.0.1:8000 maxconn 32
"""
    if section_name == 'backend':
        string += config
    else:
        string += cb

    cl = """
listen http-in2
    bind *:80
    server server1 127.0.0.1:8000 maxconn 32
"""
    if section_name == 'listen':
        string += config
    else:
        string += cl
    f = open('/tmp/deneme.conf', 'w')
    a = f.write(string)
    f.close()

    cmd = 'haproxy -c -f /tmp/deneme.conf'
    ps = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    stdout, stderr = ps.communicate()
    print ps.returncode
    return stdout


