import { createClient } from 'redis';
import { promisify } from 'util';
const client = createClient();

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

client.on('connect', async () => {
  console.log('Redis client connected to the server');
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
});
client.on('error', (err) => {
  console.error('Redis client error:', err);
});

async function setNewSchool(schoolName, value) {
  try {
    const reply = await setAsync(schoolName, value);
    console.log(reply);
  } catch (error) {
    console.log(error);
  }
}

async function displaySchoolValue(schoolName) {
  try {
    const reply = await getAsync(schoolName);
    console.log(reply);
  } catch (error) {
    console.logt(error);
  }
}
