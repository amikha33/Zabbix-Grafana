# Configuring Doxkerized Zabbix

This guide provides step-by-step instructions for configuring AWS Security Groups to allow necessary traffic for Docker services running Zabbix, MariaDB, and Grafana.

![image](https://github.com/amikha33/Zabbix-Grafana/assets/46167070/415f6891-5ab0-40db-83a2-7fe99c695632)


## Prerequisites

- AWS Management Console access.
- Docker Compose setup for Zabbix, MariaDB, and Grafana.

## Step-by-Step Guide

### 1. Log in to the AWS Management Console

- Go to the [AWS Management Console](https://aws.amazon.com/console/).

### 2. Navigate to EC2 Dashboard

- In the console, go to the EC2 Dashboard by clicking on "EC2" under the "Compute" section.

### 3. Select Security Groups

- In the left-hand menu, under "Network & Security," click on "Security Groups."

### 4. Create or Modify a Security Group

- To create a new security group, click on "Create security group."
- To modify an existing security group, select the desired security group from the list.

### 5. Configure Inbound Rules

- Go to the "Inbound rules" tab.
- Click on "Edit inbound rules" (for existing security groups) or "Add rule" (for new security groups).
- Add rules for each port you want to open, specifying the protocol and port while setting the source to `0.0.0.0/0`.

### Example Rules Configuration

Configure the following rules for your Docker Compose setup:

#### MySQL (MariaDB) Server
- **Type**: MySQL/Aurora
- **Protocol**: TCP
- **Port Range**: 3306
- **Source**: 0.0.0.0/0

#### Zabbix Server
- **Type**: Custom TCP
- **Protocol**: TCP
- **Port Range**: 10051
- **Source**: 0.0.0.0/0

#### Zabbix Frontend (Web Interface)
- **Type**: HTTP
- **Protocol**: TCP
- **Port Range**: 80
- **Source**: 0.0.0.0/0

#### Grafana
- **Type**: Custom TCP
- **Protocol**: TCP
- **Port Range**: 3000
- **Source**: 0.0.0.0/0

#### Zabbix Agent
- **Type**: Custom TCP
- **Protocol**: TCP
- **Port Range**: 10050
- **Source**: 0.0.0.0/0

### 6. Apply Changes

- After adding the necessary rules, click on "Save rules."

## Security Considerations

- **Restrict IP Ranges**: Replace `0.0.0.0/0` with specific IP ranges to limit access to only trusted sources.
- **Use VPC**: Ensure your instances are in a Virtual Private Cloud (VPC) with proper subnet configurations for added security.
- **Monitor Traffic**: Utilize AWS CloudWatch and other monitoring tools to keep track of traffic and potential security issues.

By following these steps, you will configure your security groups to allow the necessary traffic for your Docker services running Zabbix, MariaDB, and Grafana with the minimum required source configuration then apply 

    docker compose up -d 
