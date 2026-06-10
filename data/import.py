import subprocess

# Configure your connection details
sqlite_file = "db.sqlite"
mysql_user = "root"
mysql_password = "Yoursolution29650!"
mysql_host = "localhost"
mysql_database = "kanboard"

# Execute the transfer via shell command
subprocess.run([
    "sqlite3mysql",
    "-f", sqlite_file,
    "-d", mysql_database,
    "-u", mysql_user,
    f"--mysql-password={mysql_password}",
    "-h", mysql_host
])