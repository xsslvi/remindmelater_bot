# Runs container with volume for API token storing
docker run -v /home/botfather/store:/store/ -v /home/botfather/logs:/logs/ -d slawiko/remindmelater_bot:nightly-build