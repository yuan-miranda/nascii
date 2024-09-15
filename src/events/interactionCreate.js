// src/events/interactionCreate.js
const { exec } = require("child_process");
const fs = require("fs");

const UPDATE_INTERVAL_MS = 2;

async function asciiCommand(interaction) {
    const video = interaction.options.getString("video");

    const initialReply = await interaction.reply({
        content: `Rendering video "${video}" to ascii... This may take a while.`,
        fetchReply: true
    });

    exec("py ./src/main.py", async (error, stdout, stderr) => {
        if (error) {
            console.error(`Python error: ${error.message}`);
            return interaction.editReply(`Python error: ${error.message}`);
        }
        if (stderr) {
            console.error(`Python stderr: ${stderr}`);
            return interaction.editReply(`Python stderr: ${stderr}`);
        }
        console.log(`Python stdout: ${stdout}`);

        await interaction.editReply({
            content: `Finished rendering video "${video}" to ascii.\nLogs:\n\`\`\`${stdout}\`\`\``
        });

        const asciiReply = await interaction.followUp({
            content: "Starting to display the ascii video...",
            fetchReply: true
        })

        fs.readFile(`./output/${video}/${video}_resize_8colors_grayscale_ascii/${video}.txt`, "utf8", async (err, data) => {
            if (err) {
                console.error(`readFileSync error: ${err.message}`);
                return interaction.editReply(`readFileSync error: ${err.message}`);
            }
            const frames = data.split("END\r\n");
            for (let i = 0; i < frames.length; i++) {
                await new Promise(resolve => setTimeout(resolve, UPDATE_INTERVAL_MS));
                await asciiReply.edit(`\`Frame: ${i}\`\n\`\`\`${frames[i]}\`\`\``);
            }
        });
    });
}

module.exports = (interaction) => {
    if (!interaction.isCommand() && !interaction.isButton()) return;
    const { commandName, options } = interaction;

    if (interaction.user.bot) return;

    const uid = interaction.user.id;
    const channelId = interaction.channel.id;
    const guildId = interaction.guild.id;

    if (commandName === "ascii") {
        asciiCommand(interaction);
    }

    
}