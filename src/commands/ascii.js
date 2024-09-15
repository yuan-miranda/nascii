// src/commands/ascii.js
const { SlashCommandBuilder } = require("@discordjs/builders");

module.exports = {
    data: new SlashCommandBuilder()
        .setName("ascii")
        .setDescription("Render video selected to ascii (delay is 1 frames per second)")
        .addStringOption(option =>
            option.setName("video")
                .setDescription("The video to render to ascii")
                .setRequired(true)),
    async execute(interaction) {
        await interaction.reply("This command is not yet implemented");
    }
};