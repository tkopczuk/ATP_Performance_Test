#!/bin/sh

dotcloud run atpp.db -- psql -c \"CREATE DATABASE ATP_Performance_Test\"
dotcloud run atpp.db -- psql -c \"CREATE USER ATP_Performance_Test WITH PASSWORD 'ATP_Performance_Test'\"
dotcloud run atpp.db -- psql -c \"GRANT ALL PRIVILEGES ON DATABASE ATP_Performance_Test TO ATP_Performance_Test\"
