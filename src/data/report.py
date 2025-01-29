from flask import Flask, request, jsonify
import psycopg2
from config import config
from datetime import datetime
import io
import os
import uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, ContainerClient, BlobBlock, BlobClient, StandardBlobTier
from connection_info import connection_string, report_file_path

app = Flask(__name__)

# Generate consultant report from database
def get_weekly_hours_by_consultant():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = """
    SELECT 
    c.consultantname AS consultant_name,
    DATE_TRUNC('week', tm.startTime) AS week_start,
    ROUND(SUM(
        EXTRACT(EPOCH FROM (tm.endTime - tm.startTime)) / 3600 - 
        CASE WHEN tm.lunchbreak = True THEN 30 / 60 ELSE 0 END
    ), 2) AS total_weekly_hours
    FROM 
    f_time_management tm
    JOIN 
    d_consultants c ON tm.consultant_id = c.id
    GROUP BY 
    c.consultantname, DATE_TRUNC('week', tm.startTime)
    ORDER BY 
    c.consultantname, week_start;
        """
        cursor.execute(SQL)
        weekly_report_consultant = cursor.fetchall()
        print("Weekly Breakdown per consultant:")
        for row in weekly_report_consultant:
            week = row[1].strftime('%Y-W%V')
            consultant_name = row[0]
            total_hours = row[2]
            #print(f"Week: {week}, Consultant name: {consultant_name}, Total hours: {total_hours}")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()
    return weekly_report_consultant


# Generate customer report from database
def get_weekly_hours_by_customer():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = """
    SELECT 
    cu.customername AS customer_name,
    DATE_TRUNC('week', tm.startTime) AS week_start,
    ROUND(SUM(
        EXTRACT(EPOCH FROM (tm.endTime - tm.startTime)) / 3600 - 
        CASE WHEN tm.lunchbreak = True THEN 30 / 60 ELSE 0 END
    ), 2) AS total_weekly_hours
    FROM 
    f_time_management tm
    JOIN 
    d_customers cu ON tm.consultant_id = cu.id
    GROUP BY 
    cu.customername, DATE_TRUNC('week', tm.startTime)
    ORDER BY 
    cu.customername, week_start;
        """
        cursor.execute(SQL)
        weekly_report_customer = cursor.fetchall()
        print("Weekly Breakdown per customer:")
        for row in weekly_report_customer:
            week = row[1].strftime('%Y-W%V')
            customer_name = row[0]
            total_hours = row[2]
            #print(f"Week: {week}, Customer name: {customer_name}, Total hours: {total_hours}")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()
            return weekly_report_customer

# Write reports to one txt file
def write_report_to_file(report1,report2,filename):
    with open(filename, "w") as file:
        file.write("Weekly breakdown per consultant:\n")
        for row in report1:
            week = row[1].strftime('%Y-W%V')
            consultant_name = row[0]
            total_hours = row[2]
            file.write(f"Week: {week}, Consultant name: {consultant_name}, Total hours: {total_hours}\n")
        file.write("\n")  # Add spacing between results

        # Write results of the second query
        file.write("Weekly breakdown per customer:\n")
        for row2 in report2:
            week2 = row2[1].strftime('%Y-W%V')
            customer_name = row2[0]
            total_hours2 = row2[2]
            file.write(f"Week: {week2}, Customer name: {customer_name}, Total hours: {total_hours2}\n")


# Upload report to Azure Blob Storage
def upload_to_azure(file_path = str):
    container_name = "timereports"
    blob_name = os.path.basename(file_path)  # Name of the blob in the container

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    container_client = blob_service_client.get_container_client(container_name)
    if not container_client.exists():
        container_client.create_container()

    with open(file_path, "rb") as data:
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        blob_client.upload_blob(data, overwrite=True)


# Create a API command to generate a report
@app.route('/report', methods=['GET'])
def report_endpoint():
    """API endpoint that generates and uploads a report."""
    try:
        write_report_to_file(get_weekly_hours_by_consultant(),get_weekly_hours_by_customer(),report_file_path) # Write report to file
        blob_url = upload_to_azure(report_file_path)  # Upload report
        
        return jsonify({"message": "Report generated and uploaded", "url": blob_url})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()