const { SlashCommandBuilder } = require('discord.js')

module.exports = {
  data: new SlashCommandBuilder()
    .setName('beep')
    .setDescription(`I'll talk like a robot!`),

  async execute(interaction, client) {
    const message = await interaction.deferReply({
      fetchReply: true
  });

    const newMessage = `boop`
    
    await interaction.editReply({
      content: newMessage
    })
  }
}
