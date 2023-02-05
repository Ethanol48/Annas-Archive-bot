require('dotenv').config(`/Users/michaelbernardrouimi/code/Ethanol48/Annas-Archive-bot/`);

// if you want to use the Discord token:,
// process.env.DISCORD_TOKEN, it works for every variable in .env

const { Client, Collection, GatewayIntentBits } = require("discord.js")

const fs = require("fs");

const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.GuildMessageReactions,
    GatewayIntentBits.GuildInvites,
    GatewayIntentBits.GuildWebhooks,
    GatewayIntentBits.GuildIntegrations,
  ]
});

client.commands = new Collection();
client.commandArray = [];


const functionFolders = fs.readdirSync(`./src/functions`);
for (const folder of functionFolders) {

  const functionFiles = fs.readdirSync(`./src/functions/${folder}`).filter(file => file.endsWith('.js'));

  for (const file of functionFiles) 
    require(`./functions/${folder}/${file}`)(client);
}

client.handleEvents();
client.handleCommands();



client.login(process.env.DISCORD_TOKEN);
