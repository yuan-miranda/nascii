const { Client, Events, GatewayIntentBits } = require('discord.js');
require('dotenv').config();
const { token } = process.env;

const client = new Client({
	intents: [
		GatewayIntentBits.Guilds,
	],
});

client.on(Events.InteractionCreate, (interaction) => require('./events/interactionCreate.js')(interaction));
client.on(Events.MessageCreate, (message) => require('./events/messageCreate.js')(message));
client.once(Events.ClientReady, () => require('./events/ready.js')(client));

client.login(token);