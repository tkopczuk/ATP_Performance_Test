#!/bin/sh

# Copyright (C) 2011 by Blade Polska s.c.
# Full rights belong to Tomek Kopczuk (@tkopczuk).
# www.askthepony.com
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

apt-get install libevent-dev
cd /tmp
wget http://pgfoundry.org/frs/download.php/3085/pgbouncer-1.4.2.tgz
tar xzf pgbouncer-1.4.2.tgz 
cd pgbouncer-1.4.2
./configure --prefix=/usr/local
make
make install
mkdir -p /var/log/pgbouncer/
chown postgres /var/log/pgbouncer