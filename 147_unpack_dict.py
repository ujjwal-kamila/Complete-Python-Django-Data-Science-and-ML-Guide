# 147. Practice - Unpacking a Dictionary into Keyword Arguments

def setup_db_connection(hostname, port, username, password):
    print(f"Connecting to {hostname}:{port} as {username} with password {password}")

data = {
    'hostname': 'localhost',
    'username': 'admin',
    'password': 'admin@123',
    'port': 8101,
}
# if same name as dict then =>unpack using ** 
setup_db_connection(**data)
