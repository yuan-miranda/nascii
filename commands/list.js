const fs = require('fs');
const { SlashCommandBuilder } = require('discord.js');

function listCommand(interaction) {
	const videos = fs.readdirSync('./media');
	return interaction.reply(`Available videos:\n- ${videos.join('\n- ')}`);
}

module.exports = {
	data: new SlashCommandBuilder()
		.setName('list')
		.setDescription('list all videos'),
	async execute(interaction) {
		await listCommand(interaction);
	},
};