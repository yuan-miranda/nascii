// src/commands/ascii.js
const { SlashCommandBuilder } = require("@discordjs/builders");
const { exec } = require("child_process");
const fs = require("fs");

const UPDATE_INTERVAL_MS = 2;

async function asciiCommand(interaction) {
    let video = interaction.options.getString("video");

    // check if video exists
    if (!fs.existsSync(`./media/${video}`)) return interaction.reply(`**${video}** does not exist.`);

    const initialReply = await interaction.reply({
        content: `Rendering video "${video}" to ascii... This may take a while.`,
        fetchReply: true
    });

    // execute python script
    exec(`py ./src/main.py ${video}`, async (error, stdout, stderr) => {
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

        // read ascii file and display it on discord frame by frame
        video = video.split(".")[0];
        fs.readFile(`./output/${video}/${video}_ascii.txt`, "utf8", async (err, data) => {
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

module.exports = {
    data: new SlashCommandBuilder()
        .setName("ascii")
        .setDescription("Render video selected to ascii (delay is 1 frames per second)")
        .addStringOption(option =>
            option.setName("video")
                .setDescription("The video to render to ascii")
                .setRequired(true)),
    async execute(interaction) {
        await asciiCommand(interaction);
    }
};
