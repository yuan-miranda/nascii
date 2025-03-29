const { SlashCommandBuilder } = require('discord.js');

function pingCommand(interaction) {
	return interaction.reply('Pong!');
}

module.exports = {
	data: new SlashCommandBuilder()
		.setName('ping')
		.setDescription('Replies with Pong!'),
	async execute(interaction) {
		await pingCommand(interaction);
	},
};