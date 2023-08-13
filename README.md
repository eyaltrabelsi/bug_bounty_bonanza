# Bug Bounty Bonanza

`bug_bounty_bonanza` is a tool (or platform) designed for [purpose or brief description of your project]. This README provides instructions on how to install, run, and trigger events for the tool.
- [Installation](#installation)
- [Running the Server](#running-the-server)
- [Triggering Events](#triggering-events)


---

## Running the Server
To run `bug_bounty_bonanza`, clone with the following command:

```bash
git clone https://github.com/eyaltrabelsi/bug_bounty_bonanza.git
```

To serve your application, Run the server using the command (or something fancier):
   ```bash
   export FLASK_APP=app.py && flask run & ngrok http 5000
```

## Triggering Events
The most naive and less fun way is to run locally, for that, simply navigate to: ```http://localhost:5000```.
If you want to trigger using something cool like webhooks from GitHub, there are a couple of ways to set like deploying it to a server. but we will use [Ngrok and integrate it to github webhook](https://ngrok.com/docs/integrations/github/webhooks/).
