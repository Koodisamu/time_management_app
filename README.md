## Time management app

# Project scope
- Allows consultants to log working hours​
- Tracks customer-specific consulting time​
- Provides weekly report on request​
- Uses cloud-based solution (Azure + PostgreSQL)

# System architecture
- Frontend: Postman​
- Backend: Python app that accesses PostgreSQL Database in Azure​
- Cloud Infrastructure: Backend hosted on two Azure Virtual Machines (one for logging hours and one for generating the report)

# Tech used
- Python
- Flask
- Postman
- Azure
- Azure Blob Storage
- Azure Virtual Machine
- PostgreSQL

# ERD

![image (4)](https://github.com/user-attachments/assets/e1fc5c6a-7d8f-4978-84b8-4b8b7197fae8)


# Future development ideas
- Developing front-end for logging hours​
- Automate report for example once per week​
- Visualize report better​
- Using same database as source for Power BI reports​
- Creating restrictions/attributes for different weekday logs​
- Error handling​
- Using the same app for tracking hour balance(liukuma)
