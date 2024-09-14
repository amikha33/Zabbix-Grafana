from pyzabbix import ZabbixAPI

# Zabbix API URL and credentials
zabbix_url = 'http://localhost:8080/api_jsonrpc.php'
zabbix_user = 'Admin'  # Replace with your Zabbix username
zabbix_password = 'zabbix'  # Replace with your Zabbix password

# Initialize ZabbixAPI object
zapi = ZabbixAPI(zabbix_url)

# Authenticate
try:
    zapi.login(zabbix_user, zabbix_password)
    print("Successfully logged in to Zabbix API")
except Exception as e:
    print(f"Error logging in: {e}")
    exit()

# Define parameters for the new host
new_host_params = {
    'host': 'NewHostName-RFC',  # The name of the new host
    'interfaces': [  # Network interfaces for the host
        {
            'type': 1,  # 1 for Zabbix agent
            'main': 1,  # Main interface (1 for main)
            'useip': 1,  # Use IP (1 if true)
            'ip': '192.168.1.100',  # IP address of the host
            'dns': '',  # DNS name (if applicable)
            'port': '10050'  # Port number (default for Zabbix agent is 10050)
        }
    ],
    'groups': [  # List of group IDs to which the host will belong
        {
            'groupid': '2'  # Replace with your group ID
        }
    ],
    'templates': [  # List of template IDs to link with the host
        {
            'templateid': '10001'  # Replace with your template ID
        }
    ],
}

# Create the host
try:
    result = zapi.host.create(new_host_params)
    print("Host Created:", result)
except Exception as e:
    print(f"An error occurred while creating the host: {e}")

