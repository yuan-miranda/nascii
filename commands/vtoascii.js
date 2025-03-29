const fs = require('fs');
const { spawn } = require('child_process');
const os = require('os');
const { SlashCommandBuilder } = require('discord.js');

const UPDATE_INTERVAL_MS = 200;

async function vToAsciiCommand(interaction) {
	const video = interaction.options.getString('video');
	if (!fs.existsSync(`./media/${video}`)) return interaction.reply(`**${video}** does not exist`);

	const python = os.platform() === 'win32' ? 'python' : 'python3';

	await interaction.reply(`Converting **${video}** to ASCII... This may take a while.`);
	const vToAsciiProcess = spawn(python, ['./vtoascii.py', video]);

	vToAsciiProcess.stdout.on('data', async (data) => {
		console.log(data.toString());
		await interaction.editReply(`\`\`\`${data.toString()}\`\`\``);
	});

	vToAsciiProcess.stderr.on('data', async (data) => {
		console.error(data.toString());
		await interaction.editReply(`\`\`\`${data.toString()}\`\`\``);
	});

	vToAsciiProcess.on('close', async () => {
		const reply = await interaction.editReply({
			content: 'Rendering video as ASCII...',
			fetchReply: true,
		});

		const fileName = video.split('.').slice(0, -1).join('.');
		fs.readFile(`./output/${fileName}/${fileName}.txt`, 'utf8', async (err, data) => {
			if (err) return interaction.editReply(`Error reading file: ${err}`);
			const frames = data.split('END\r\n');
			for (let i = 0; i < frames.length; i++) {
				await new Promise(resolve => setTimeout(resolve, UPDATE_INTERVAL_MS));
				await reply.edit(`\`Frame: ${i}\`\n\`\`\`${frames[i]}\`\`\``);
			}
		});
	});
}

module.exports = {
	data: new SlashCommandBuilder()
		.setName('vtoascii')
		.setDescription('Render a video as ASCII')
		.addStringOption(option =>
			option.setName('video')
				.setDescription('The video to render as ASCII')
				.setRequired(true)),
	async execute(interaction) {
		await vToAsciiCommand(interaction);
	},
};