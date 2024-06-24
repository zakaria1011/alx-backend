const redis = require('redis');

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err);
});

const hashKey = 'HolbertonSchools';

const schools = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

for (const [field, value] of Object.entries(schools)) {
  client.hset(hashKey, field, value, redis.print);
}

setTimeout(() => {
  client.hgetall(hashKey, (err, result) => {
    if (err) {
      console.log('Error retrieving data:', err);
    } else {
      console.log(result);
    }
    client.quit();
  });
}, 1000);
