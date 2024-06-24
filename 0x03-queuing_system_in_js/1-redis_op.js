import { createClient, print } from 'redis';

const client = createClient();
client.on('connect', () => {
  console.log('Redis client connected to the server');
  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
});
client.on('error', (err) => {
  console.error('Redis client error:', err);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.log(err);
    } else {
      console.log(reply);
    }
  });
}
