
[//]: # ( challenge tech stack: streamlit )

[//]: # ( challenge instructions )

We saw in the previous challenge how to plug a website to our **Prediction API** in order to allow regular users to make predictions.

Now let's create our own website ! 🔥

We are going to use **Streamlit** which will allow us to create a website very easily and without any web development skills.

## First, let's create another website project

We will create a new project directory for the code of our website.

Again, this directory will be located inside of our *projects directory*: `~/code/<user.github_nickname>`.

Create a new project directory named `taxifare-website`.

```bash
cd ~/code/<user.github_nickname>
mkdir taxifare-website
cd taxifare-website
```

Initialise a new git repository:

```bash
git init
```

Create a corresponding repository on our **GitHub** account:

``` bash
gh repo create taxifare-website --private --source=. --remote=origin
```

Go to the GitHub repo in order to make sure that everything is ok:

``` bash
gh browse
```

The repository is empty, which is normal since we have not pushed any code yet...

We are now all set!

## Create a streamlit website

First, we need an `app.py` file inside of our project. The file will contain the code for our page.

``` bash
touch app.py
```

Then, let's copy the `Makefile` that is provided inside of the project... It will allow us to run useful commands for:
- `install_requirements` : dependencies
- `streamlit` : run the **Streamlit** web server in order to see what our website looks like


``` bash
cp ~/code/<user.github_nickname>/{{local_path_to('07-ML-Ops/05-User-interface/02-Taxifare-website')}}/Makefile ~/code/<user.github_nickname>/taxifare-website/
```

You project should look like this:

``` bash
.
├── Makefile
└── app.py
```

Not too overwhelming, right ? 😉

Well... This is half the work.

Lets add some content to our website in `app.py`:

``` python
import streamlit as st

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
```

Let's run the **Streamlit** web server and see what our website looks like:

``` bash
make streamlit
```

We have a website of our own running on our machine 🎉

## Now we want to plug our API to the website

... So that users can actually make some predictions!

👉 Let's follow the instructions inside the web page and replace the content with some `requests` package magic and a call to our API!

👉 Again, alternatively, you may use this Le Wagon **Prediction API URL** if you you do not have one in production: https://taxifare.lewagon.ai/

Let's inspect `app.py` and check what is being done inside...

Replace the URL to the prediction API with your own and update the code accordingly.

Now let's get crazy with the page content 🎉

Maybe add some map 🗺

Once we are satisfied, let's push the code to production! 🔥


## Deploy

Let's setup the project for **Streamlit Cloud**.

❓ **What do we need to deploy our website to Streamlit Cloud ?**

We need to push our repository is up to date in GitHub

<details>
  <summary markdown='span'><strong> 💡 Hint </strong></summary>

``` bash
cd ~/code/<user.github_nickname>/taxifare-website && git add .
git commit -m 'My first website'
git push origin master
```

</details>

We also need to add a configuration file to our project:
- `requirements.txt` for our app dependencies

Let's make sure we only include packages we actually need 😉

<details>
  <summary markdown='span'><strong> 💡 Hint </strong></summary>

  ⚠️ Don't include any of the [modules from base Python](https://docs.python.org/3/py-modindex.html) or Streamlit Cloud will throw an error when deploying !

``` text
streamlit
requests
```

</details>

The project should now look like this:

``` bash
.
├── Makefile
├── app.py
└── requirements.txt
```

Create an app for our website on **Streamlit Cloud**...

Go to [Streamlit Cloud](https://share.streamlit.io/) and create an account.
You can use any authentication method you want but using your GitHub account is the most efficient one as you will need access to your repository anyway 😉

Once signed in, you can create a new app following the steps shown during the lecture (feel free to take a look at the slides again).

❓ **How to update your app ?**

Your GitHub repository is the source for the app : each time you push an update to your repo you will see it in the app in almost real time. Try it out!

🧠 If you make any changes in your `requirements.txt`, Streamlit automatically detects it and install the new packages !

😮 You can setup your own subdomain name in the settings of your app! Check the [documentation](https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app#your-app-url).

That's it, your website is online ! 🚀

Feel free to explore all the possibilities given by Streamlit and enhance your app !
➡️ Take a look at the [documentation](https://docs.streamlit.io/)
