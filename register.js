const fs = require('fs');
const { REST, Routes } = require('discord.js');
require('dotenv').config();
const { token, clientId } = process.env;

const rest = new REST({ version: '10' }).setToken(token);

const commands = [];
for (const file of fs.readdirSync(`${__dirname}/commands`).filter(commandFile => commandFile.endsWith('.js'))) {
	const command = require(`${__dirname}/commands/${file}`);
	commands.push(command.data.toJSON());
}

(async () => {
	try {
		await rest.put(Routes.applicationCommands(clientId), { body: commands });
		console.log('Successfully registered application commands.');
	}
	catch (error) {
		console.error(error);
	}
})();