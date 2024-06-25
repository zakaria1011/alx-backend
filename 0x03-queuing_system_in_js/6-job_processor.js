const kue = require('kue');

const queue = kue.createQueue();

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});

queue.on('job complete', (id) => {
  console.log(`Job completed with id ${id}`);
});

queue.on('job failed', (id, errorMessage) => {
  console.log(`Job failed with id ${id} and error: ${errorMessage}`);
});

queue.on('error', (err) => {
  console.error('There was an error with the Kue queue:', err);
});
