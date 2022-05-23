First, run the command 'ngrok http 7777'
Next run microservice.py
-your port should match the specified port you are wanting to expose to be public facing
Next, copt the forwarding port webaddress ending in '.ngrok.io' and replace the response_API variable in testapi.py

You should now be able to access your port from the web.
