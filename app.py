from flask import Flask
from redis import Redis
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))
redisDb = Redis(host=redis_host, port=redis_port)

@app.route('/')
def welcomeToBishnudevs():
    redisDb.incr('visitorCount')
    visitCount = str(redisDb.get('visitorCount'), 'utf-8')
    return "Welcome to Bishnudevs.in! Visitor Count: " + visitCount

if __name__ == "__main__":
    app.run(debug=True)
