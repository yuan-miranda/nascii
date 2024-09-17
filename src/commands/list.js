// src/commands/list.js
const { SlashCommandBuilder } = require("@discordjs/builders");
const fs = require("fs");

function listCommand(interaction) {
    // list all videos available in the media folder
    const videos = fs.readdirSync("./media");
    return interaction.reply(`Available videos: ${videos.join(", ")}`);
}


module.exports = {
    data: new SlashCommandBuilder()
        .setName("list")
        .setDescription("List all videos available"),
    async execute(interaction) {
        await listCommand(interaction);
    }
};
