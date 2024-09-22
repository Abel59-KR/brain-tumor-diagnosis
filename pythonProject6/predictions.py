from dbco import mycursor
def predictions(classname, confidence_score):
    # Query database
    query = 'INSERT INTO pred (classname, confidence_score) VALUES (%s, %s)'
    mycursor.execute(query, (classname, confidence_score))
    predictions = mycursor.fetchall()
    return predictions