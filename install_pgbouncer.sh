#!/bin/sh

apt-get install libevent
cd /tmp
wget http://pgfoundry.org/frs/download.php/3085/pgbouncer-1.4.2.tgz
tar xzf pgbouncer-1.4.2.tgz 
cd pgbouncer-1.4.2
./configure --prefix=/usr/local
make
make install
cp etc/pgbouncer.ini /usr/local/etc/pgbouncer.ini
cp etc/userlist.txt /usr/local/etc/userlist.txt
pgbouncer /usr/local/etc/pgbouncer.ini -q