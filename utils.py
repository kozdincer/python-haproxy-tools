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
