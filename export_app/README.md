# FastAPI Export App

Export structured data to multiple formats and systems with FastAPI.  
By Joanna Karytsioti & George Tsakalos (AUEB DMST – Spinelis SEIP)

[![PyPI version](https://badge.fury.io/py/fastapi-code-generator.svg)](https://pypi.python.org/pypi/fastapi-code-generator)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fastapi-code-generator)](https://pypi.python.org/pypi/fastapi-code-generator)
![license](https://img.shields.io/github/license/koxudaxi/fastapi-code-generator.svg)

---

## 📦 Features

This FastAPI application supports exporting data to:

### 📁 File Formats

- **JSON** → `?format=json`  
- **CSV** → `?format=csv`  
- **Excel** → `?format=excel`  
- **PDF** → `?format=pdf`  
- **Parquet** → `?format=parquet`  
- **Avro** → `?format=avro`  
- **Feather** → `?format=feather`  
- **ORC** → `?format=orc`  

### 🗄 Databases & Storage

- **MySQL** → `?format=mysql`  
- **SQLite** → `?format=sqlite`  
- **AWS S3** → `?format=s3`  

### 🔄 Streaming Systems

- **Kafka** → `?format=kafka`  
- **RabbitMQ** → `?format=rabbitmq`  
- **Apache Pulsar** → `?format=pulsar`  

---

## 🛠 Installation

Install the required dependencies:

```bash
pip install -r requirements_all_exports.txt
```

---

## ▶️ Usage

Start the development server:

```bash
uvicorn main:app --reload
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to access the Swagger UI and test the `/export` endpoint.

---

## 🔐 Environment Variables

Set the following environment variables depending on your export target:

### AWS S3

```env
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
AWS_S3_BUCKET=...
AWS_S3_OBJECT_KEY=...
```

### MySQL

```env
MYSQL_HOST=...
MYSQL_USER=...
MYSQL_PASSWORD=...
MYSQL_DATABASE=...
```

### Kafka

```env
KAFKA_BOOTSTRAP_SERVERS=localhost:9092
KAFKA_TOPIC=exported_data
```

### RabbitMQ

```env
RABBITMQ_HOST=localhost
RABBITMQ_QUEUE=export_queue
```

### Pulsar

```env
PULSAR_SERVICE_URL=pulsar://localhost:6650
PULSAR_TOPIC=exported_data
```

---

## 🧰 Tech Stack

- **FastAPI**, **Uvicorn**
- **Pandas**, **XlsxWriter**, **ReportLab**
- **PyArrow**, **FastAvro**
- **MySQL Connector**, **Boto3**, **Kafka-Python**
- **Pika**, **Pulsar-Client**

See [`requirements_all_exports.txt`](./requirements_all_exports.txt) for full details.

---

## 📄 License

MIT License – for educational and contribution purposes.
