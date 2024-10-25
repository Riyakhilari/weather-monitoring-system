import psycopg2

def connect_db():
    return psycopg2.connect(
        dbname="weather_db", user="postgres", password="your_password", host="localhost", port="5432"
    )

def insert_summary(city, avg_temp, max_temp, min_temp, dominant_weather):
    conn = connect_db()
    cursor = conn.cursor()
    query = """
    INSERT INTO weather_summary (city, avg_temp, max_temp, min_temp, dominant_weather)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (city, avg_temp, max_temp, min_temp, dominant_weather))
    conn.commit()
    cursor.close()
    conn.close()
