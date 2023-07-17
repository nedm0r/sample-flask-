# Start from a base MySQL image
FROM mysql:5.7

# Add a database
ENV MYSQL_DATABASE flask_db

# Add the content of the sql-scripts/ directory to your image
# All scripts in docker-entrypoint-initdb.d/ are automatically
# executed during container startup
COPY ./Script-SQL/ /docker-entrypoint-initdb.d/
