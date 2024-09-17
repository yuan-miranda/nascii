// src/register.js
const fs = require("fs");
const { REST, Routes } = require("discord.js");
const { token, clientId } = require("./config");

const rest = new REST({ version: "10" }).setToken(token);

// load all commands
const commands = []
for (const file of fs.readdirSync(`${__dirname}/commands`).filter(file => file.endsWith(".js"))) {
    console.log(`Loading command ${file}`);
    const command = require(`${__dirname}/commands/${file}`);
    commands.push(command.data.toJSON());
}

(async () => {
    try {
        console.log("Started refreshing application (/) commands.");
        await rest.put(Routes.applicationCommands(clientId), { body: commands });
        console.log("Successfully reloaded application (/) commands.");
    } catch (error) {
        console.error(error);
    }
})();
