# IoT Cihaz Emülatörü

Bu proje, IoT (Nesnelerin İnterneti) cihazlarını simüle eden bir Python uygulamasıdır. MQTT protokolü üzerinden sıcaklık ve nem verilerini yayınlayan sanal sensörler oluşturur.

## Özellikler

- WebSocket üzerinden MQTT iletişimi
- PostgreSQL veritabanı entegrasyonu
- Gerçek zamanlı sensör verisi simülasyonu
- Aktif/pasif sensör yönetimi

## Gereksinimler

- Python 3.x
- PostgreSQL
- paho-mqtt
- psycopg2

## Kurulum

1. Gerekli Python paketlerini yükleyin:
```bash
pip install paho-mqtt psycopg2-binary
```

2. PostgreSQL veritabanı bağlantı bilgilerini ayarlayın:
- Veritabanı: postgres
- Kullanıcı: postgres
- Şifre: postgres
- Sunucu: localhost

3. MQTT broker'ın çalıştığından emin olun:
- Sunucu: localhost
- WebSocket Port: 9001

## Kullanım

Uygulamayı başlatmak için:

```bash
python iot_device_emulator.py
```

Program, veritabanında aktif olarak işaretlenmiş sensörler için her 5 saniyede bir rastgele sıcaklık (20-30°C) ve nem (%40-60) verileri üretir ve bu verileri MQTT broker'a gönderir.

## Veri Formatı

Gönderilen veriler JSON formatındadır:
```json
{
    "sensor_id": "sensor_id",
    "temperature": 25.5,
    "humidity": 45.2
}
```
