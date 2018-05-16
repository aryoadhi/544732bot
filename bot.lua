local discordia = require('discordia')
local client = discordia.Client()

client:on('ready', function()
	print('Logged in as '.. client.user.username)
end)

client:on('messageCreate', function(message)
	if message.content == '!ping' then
		message.channel:send('Pong!')
	end
end)

client:run('Bot NDQ2MTQ1Njg1MTkzMDk3MjI2.Dd1g5w.T7nvpqxsDql8D0is7TmNuNgdI5s')
