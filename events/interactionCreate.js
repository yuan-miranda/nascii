const listCommand = require('../commands/list.js');
const pingCommand = require('../commands/ping.js');
const vToAsciiCommand = require('../commands/vtoascii.js');

module.exports = (interaction) => {
	if (!interaction.isCommand() && !interaction.isButton()) return;
	const { commandName } = interaction;

	if (interaction.user.bot) return;

	// const uid = interaction.user.id;
	// const channelId = interaction.channel.id;
	// const guildId = interaction.guild.id;

	if (commandName === 'list') listCommand.execute(interaction);
	else if (commandName === 'ping') pingCommand.execute(interaction);
	else if (commandName === 'vtoascii') vToAsciiCommand.execute(interaction);
	else interaction.reply(`Unknown command: **${commandName}**`);
};