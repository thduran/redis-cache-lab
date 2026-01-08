import time
import redis
from flask import Flask

app = Flask(__name__)

# connects to redis container
cache = redis.Redis(host='redis', port=6379)

# simulates a heavy query to the database
def get_data_from_slow_db():
    time.sleep(3) # pretends it lasted 3s
    return "Important data from DB"

@app.route('/')
def home():
    start_time = time.time()
    
    # 1. Attempts to get from cache
    data = cache.get('my_data')
    
    if data:
        # hit
        origin = "redis cache"
    else:
        # miss -> goes to library
        data = get_data_from_slow_db()
        # saves in cache for 10s, so the next can use
        cache.set('my_data', data, ex=10) 
        origin = "simulated slow database"
        
    end_time = time.time()
    duration = round(end_time - start_time, 4)
    
    return f"""
    <h1>Performance Test</h1>
    <p>Data origin: <strong>{origin}</strong></p>
    <p>Response time: <strong>{duration} seconds</strong></p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)