<<<<<<< HEAD
import mysql.connector
from datetime import datetime

def log_to_mysql(emotion, confidence, img_path, timestamp):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='survi09mukh',
            database='mentis_mirror',
            auth_plugin='mysql_native_password'  # 👈 Ensure this is here
        )
        cursor = conn.cursor()
        query = "INSERT INTO emotion_logs (emotion, confidence, img_path, timestamp) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (emotion, confidence, img_path, timestamp))
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Logged to MySQL successfully!")
    except Exception as e:
        print(f"❌ Error logging to MySQL: {e}")

# Test entry
log_to_mysql("happy", 95.6, "images/sample.jpg", datetime.now())
=======
import mysql.connector
from datetime import datetime

def log_to_mysql(emotion, confidence, img_path, timestamp):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='survi09mukh',
            database='mentis_mirror',
            auth_plugin='mysql_native_password'  # 👈 Ensure this is here
        )
        cursor = conn.cursor()
        query = "INSERT INTO emotion_logs (emotion, confidence, img_path, timestamp) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (emotion, confidence, img_path, timestamp))
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Logged to MySQL successfully!")
    except Exception as e:
        print(f"❌ Error logging to MySQL: {e}")

# Test entry
log_to_mysql("happy", 95.6, "images/sample.jpg", datetime.now())
>>>>>>> 275544aa39468d141d7c260c5e3d57a7af11f987
