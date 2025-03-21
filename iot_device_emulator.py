import paho.mqtt.client as mqtt
import json
import time
import random
import psycopg2

# PostgreSQL Bağlantı Bilgileri
DB_HOST = "localhost"  # Veritabanı sunucusu
DB_NAME = "postgres"  # Veritabanı adı
DB_USER = "postgres"  # PostgreSQL kullanıcı adı
DB_PASSWORD = "postgres"  # PostgreSQL şifresi

# MQTT Broker Bilgileri
BROKER_ADDRESS = "localhost"
PORT = 9001  # WebSocket portu
TOPIC = "sensor/data"

# WebSocket Bağlantısı için MQTT Client Tanımlama
client = mqtt.Client(transport="websockets")
client.connect(BROKER_ADDRESS, PORT, 60)


# PostgreSQL'den Aktif Sensörleri Getiren Fonksiyon
def get_active_sensors():
    try:
        connection = psycopg2.connect(
            host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD
        )
        cursor = connection.cursor()

        # Sadece isActive = True olan sensörleri al
        cursor.execute('SELECT "sensorId" FROM iot_devices WHERE "isActive" = TRUE;')
        sensors = [row[0] for row in cursor.fetchall()]

        cursor.close()
        connection.close()
        return sensors

    except Exception as e:
        print(f"❌ PostgreSQL bağlantı hatası: {e}")
        return []


# Veri Gönderme Fonksiyonu
def publish_sensor_data():
    active_sensors = get_active_sensors()

    if not active_sensors:
        print("⚠️ Aktif sensör bulunamadı.")
        return

    for sensor_id in active_sensors:
        temperature = round(random.uniform(20.0, 30.0), 2)
        humidity = round(random.uniform(40.0, 60.0), 2)
        payload = {
            "sensor_id": sensor_id,
            "temperature": temperature,
            "humidity": humidity,
        }
        json_payload = json.dumps(payload)
        client.publish(TOPIC, json_payload)
        print(f"📤 Veri gönderildi: {json_payload}")


# Sürekli veri gönderme
try:
    while True:
        publish_sensor_data()
        time.sleep(5)  # 5 saniyede bir veri gönder
except KeyboardInterrupt:
    print("Çıkış yapılıyor...")
    client.disconnect()
