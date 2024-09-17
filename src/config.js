// src/config.js
const { IntentsBitField } = require("discord.js");
require("dotenv").config();

module.exports = {
    intents: [
        IntentsBitField.Flags.Guilds,
        IntentsBitField.Flags.GuildMessages,
        IntentsBitField.Flags.MessageContent,
        IntentsBitField.Flags.GuildMembers
    ],
    token: process.env.BOT_TOKEN,
    clientId: process.env.BOT_ID
};
