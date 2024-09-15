// src/events/messageCreate.js
module.exports = (message) => {
    if (message.author.bot) return;
    if (message.content === '!ping') message.reply('Pong!');
};