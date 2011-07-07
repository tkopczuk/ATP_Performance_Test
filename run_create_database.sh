#!/bin/sh

echo "Run logged as postgres user! (su - postgres)"
psql -c "CREATE DATABASE ATP_Performance_Test"
psql -c "CREATE USER ATP_Performance_Test WITH PASSWORD 'ATP_Performance_Test'"
psql -c "GRANT ALL PRIVILEGES ON DATABASE ATP_Performance_Test TO ATP_Performance_Test"
