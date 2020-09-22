[![License: MIT](https://img.shields.io/badge/License-MIT-teal.svg)](https://opensource.org/licenses/MIT)

# Cosibot Portugal

<img align="right" width="200" height="201" alt="Helen-wp" src="https://cosibot.org/wp-content/uploads/2020/04/Helen-wp-3.png"></img>
[Cosibot](https://cosibot.org/) – Covid Stay Informed Bot is a non-profit initiative developed by [ROBO.AI](https://robo-ai.com/) to provide citizens around the world with credible and up-to-date information on Coronavirus, using different sources and making it available in a single application.

This is the Portuguese version, available in Portuguese.

## Add Cosibot to your website
You can add the Cosibot Corona Virus Chatbot as a popup to your website. It is straightforward and it can be done in just three simple steps:
1. [Ask for an API key](https://cosibot.org/contact)
2. Ask your web developer to add the code snippet to your website - you can choose to add the International version or one of the Country bots available.
```javascript
<script src="https://cdn.cosibot.org/widget/cosibot.js"></script>
<script>
var config = {
   bot: 'covid-int-en',
   key: '<Your API key>',
   language: 'en'
}
Cosibot.init(config);
</script>
```
3. Ta-da, The Cosibot is there. Tell the world about it!

## This is an open source project - Contribute!
### Train the bot
If you want to train the bot to test it locally, you can do it by running the following command (inside the bot folder): 
```bash
rasa train
```

### Interact with the bot
To interact with the bot locally you can run:
```bash
rasa run actions
```
```bash
rasa shell
```

## Get in contact
For any queries you might have, you can contact us [here](https://cosibot.org/contact).
You can also find us on [Facebook](https://www.facebook.com/cosibot), [Twitter](https://twitter.com/cosibot) and [Linkedin](https://www.linkedin.com/company/cosibot/).