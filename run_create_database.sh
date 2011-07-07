#!/bin/sh

echo "Run logged as postgres user! (su - postgres)"
psql -c "CREATE DATABASE atp_performance_test"
psql -c "CREATE USER atp_performance_test WITH PASSWORD 'atp_performance_test'"
psql -c "GRANT ALL PRIVILEGES ON DATABASE atp_performance_test TO atp_performance_test"
