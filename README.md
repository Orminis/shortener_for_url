# shortener_for_url
 test project for url shortener

https://realpython.com/build-a-python-url-shortener-with-fastapi/#demo-your-python-url-shortener

used framework and libraries:
FastApi
Uvicorn
dotenv
sqlalchemy
validators


Define Environment Variables
You’re currently developing your Python URL shortener on your local computer. But once you want to make it available to your users, you may want to deploy it to the web.

It makes sense to use different settings for different environments. Your local development environment may use a differently named database than an online production environment.

To be flexible, you store this information in special variables that you can adjust for each environment. While you won’t take steps to host your app online in this tutorial, you’ll build your app in a way that enables you to deploy it to the cloud in the future.

It’s a good start to have env_name, base_url, and db_url in place with default values. But since the values for your current environment, the domain of your app, and the address of your database are dependent on the environment that you’re working in, you’ll load the values from external environment variables later.

