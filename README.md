## Setting up Twitter Developer Account and Generate API Keys
### Creating a new account / signing into an existing account
- I've already an existing X account
### Sign up for a Twitter Developer Account
- Navigate to the Twitter Developer Platform
- Sign up for a Developer account and create a project
- I've a default project and now let's generate the keys inside the app.
### Generating API keys
- Click on Projects & Apps under Dashboard and now tap on Apps and then navigate to keys and tokens
- Generate the following keys & tokens:
   - API Key and Secret
   - Bearer Token
   - Access Token and Secret

![image](https://github.com/user-attachments/assets/8527b283-6417-4f64-951d-0ac455868262)
### Configuring OAuth
- Click on settings, tap on set up button for user authentication

![image](https://github.com/user-attachments/assets/3de4fa26-1fa1-40a7-a6d6-eab9608cdfa1)

- Setting up of callback url

![image](https://github.com/user-attachments/assets/a06e0f86-26d3-4609-90d6-d5178624c97f)

## Interacting with Twitter API
### Posting a new Tweet
- Let's post a tweet using  POST statuses/update endpoint of the Twitter API 
- We can use Python to say a message "Hello from Twitter API"

![image](https://github.com/user-attachments/assets/299198f9-0286-428a-bc8e-71545050fe1a)

- We can see the tweet posted on the timeline

![image](https://github.com/user-attachments/assets/0bed61c1-3a36-4ea7-9365-6350f37b5a8f)

- Let's post one more tweet regarding a movie release date

![image](https://github.com/user-attachments/assets/3b3aae8e-bb03-4d6c-8b7e-f3d680ff3a85)
 
![image](https://github.com/user-attachments/assets/5c9592d5-41ee-426a-8214-7e77a2d114a0)

### Deleting a tweet
- Now using python code, deleting a tweet can be possible by passing the tweet ID

![image](https://github.com/user-attachments/assets/086867bc-1da8-4d0a-87e9-44b814a1ce3f)

- Tweet got deleted!

![image](https://github.com/user-attachments/assets/1e6a204e-e05b-426c-9ec4-8c174d0488c0)
