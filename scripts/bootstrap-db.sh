# Postgres username.
DB_USER="sandbox"
# Postgres password.
DB_PASS="sandbox"
# Database name.
DB_NAME="sandbox"
# Delete database if it exists.
sudo -u postgres psql -c "DROP DATABASE IF EXISTS $DB_NAME;"
# Delete user if it exists.
sudo -u postgres psql -c "DROP ROLE IF EXISTS $DB_USER;"
# Create user.
sudo -u postgres psql -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASS';"
# Make user a superuser.
sudo -u postgres psql -c "ALTER USER $DB_USER WITH SUPERUSER;"
# Make database.
sudo -u postgres psql -c "CREATE DATABASE $DB_NAME OWNER $DB_USER;"
# Grant privilages on database.
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME to $DB_USER;"

# Edit line 90. Change (local all all peer) to (local all all trust).
# sudo vi /etc/postgresql/9.3/main/pg_hba.conf
