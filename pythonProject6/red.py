from dbco import mycursor
def record(facility_name,disease):
    # Query database to check if the provided credentials are valid
    query = "SELECT * FROM records WHERE facility_name= %s AND disease = %s"
    mycursor.execute(query, (facility_name, disease))
    records = mycursor.fetchone()
    return records