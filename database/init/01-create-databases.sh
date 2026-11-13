#!/usr/bin/env bash

set -euo pipefail

psql \
    --set=ON_ERROR_STOP=1 \
    --set=auto_user="$AUTO_SERVICE_DB_USER" \
    --set=auto_password="$AUTO_SERVICE_DB_PASSWORD" \
    --set=repair_user="$REPAIR_SERVICE_DB_USER" \
    --set=repair_password="$REPAIR_SERVICE_DB_PASSWORD" \
    --username "$POSTGRES_USER" \
    --dbname "$POSTGRES_DB" <<'SQL'

-- Создание пользователя основного приложения
CREATE ROLE :"auto_user"
WITH LOGIN PASSWORD :'auto_password';

-- Создание базы данных основного приложения
CREATE DATABASE auto_service_db
OWNER :"auto_user";


-- Создание пользователя микросервиса
CREATE ROLE :"repair_user"
WITH LOGIN PASSWORD :'repair_password';

-- Создание базы данных микросервиса
CREATE DATABASE repair_service_db
OWNER :"repair_user";

SQL
