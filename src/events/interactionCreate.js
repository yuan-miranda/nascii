// src/events/interactionCreate.js
const asciiCommand = require("../commands/ascii");
const listCommand = require("../commands/list");

module.exports = (interaction) => {
    if (!interaction.isCommand() && !interaction.isButton()) return;
    const { commandName, options } = interaction;

    if (interaction.user.bot) return;

    // const uid = interaction.user.id;
    // const channelId = interaction.channel.id;
    // const guildId = interaction.guild.id;

    if (commandName === "ascii") {
        asciiCommand.execute(interaction);
    }
    else if (commandName === "list") {
        listCommand.execute(interaction);
    }
    
}
