// src/main.js
const { Client } = require('discord.js');
const { token, intents } = require('./config');

const client = new Client({ intents });

client.on('ready', () => require('./events/ready')(client));
client.on('messageCreate', (message) => require('./events/messageCreate')(message));
client.on('interactionCreate', async (interaction) => require('./events/interactionCreate')(interaction));

client.login(token);