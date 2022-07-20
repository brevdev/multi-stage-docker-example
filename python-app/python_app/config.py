import os

MYSQL_ENDPOINT = os.environ.get("MYSQL_ENDPOINT")
REDIS_ENDPOINT = os.environ.get("REDIS_ENDPOINT")
ENV = os.environ.get("ENV")

print(f"ENV: {ENV}")
print(f"MYSQL_ENDPOINT: {MYSQL_ENDPOINT}")
print(f"REDIS_ENDPOINT: {REDIS_ENDPOINT}")
