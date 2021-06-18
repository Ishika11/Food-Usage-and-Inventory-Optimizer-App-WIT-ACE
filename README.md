# Food Usage and Inventory Optimzer App

## Short description

### What's the problem?
Food wastage is a major environmental problem facing the world today, and one of the major causes for the global food wastage is higher inventory due to poor forecasts. Many hotels end up over buying raw materials which remain unused till they go bad and are discarded. That ends up in lanfills and rots where it decomposes to produce harmful methane gas which causes green house effect. The energy that went into growing, transporting and harvesting the wasted food is also lost. 

### How can technology help?
With AI/ML, and sophisticated training models, it is not so hard to get near perfect predictions. Moreover, in today's time, it is also not hard to find resources for the training dataset. Technoloagy can go a long way in monitoring, maintaing and updating billing logs and using the data to forecast food consumption patterns.

### The idea
Using a set of open sourced tools, IBM Cloud and Watson Services, it was possible for us to create and Food Usage and Inventory Optimizer, that uses flask on the frontend and LSTM models to get restaurant data in the form of bills ( no extra effort from the users! ) and make predictions on the food consumption pattern for the next 7 days.

## Demo Video
[Vimeo Link](https://vimeo.com/564521168)

## Architecture

![Test Image 5](https://github.com/Ishika11/WitAce--Food-Optimization/blob/main/diag.PNG)

 ## Getting Started
 Select the directory where the files are saved, that is, within: eCommerceFlask directory
 ```
 $pushd D:\Food_Optimiser_FE\eCommerceFlask
 ```

Set up a virtual environment
```
python -m venv test-env
```

Activate the virtual environment
```
test-env\Scripts\activate.bat
```
Install dependencies
```
pip install -r requirements.txt
```

### Start this project ⚙️

```
python run.py
```

### Finally open loopback URL address  🤓

http://127.0.0.1:5000/

## Long description

Food wastage is not just a humanitarian concern with still millions of people going to bed hungry, but also an environmental issue. By wasting food, we waste the energy required for its growth, transport, packaging and harvesting. This discarded food ends up in landfills where it rots and produces methane, a greenhouse gas far more potent than carbon dioxide. 6-8% of all human greenhouse gas emission comes from food wastage. Food wastage, hence, has a direct and detrimental impact on climate.
A third of the world's food produce is wasted each year, in other words, 1.3 billion tonnes.. In India, 67 million tonnes of food is wasted yearly. Our infrastructure and technology do not focus on sustainability of the food in the supply chain. One of the major contributors is higher inventory due to poor forecasts. Over purchasing of raw materials like wheat, perishable vegetables and fruits by restaurants leads to appalling losses every year. This is exactly the challenge my teammates and I have tried to overcome by the Food Usage Optimiser App.
Keeping in mind that India is full of small-scale and large-scale restaurants and hotels, we have simplified the functioning of our app to increase the ease of use and quickness of procurement.
We created a simple billing system that allows the user to interact with the UI and select all the items per order per day. The log is collected over time, and gets fed into our prediction system that predicts the quantity of food that will be ordered over the week. With this knowledge, the user can optimize the inventory preventing food wastage.In simpler words, this information can be used by restaurant managers to make informed decisions about the quantity of raw materials they would need to order at the beginning of each week. 
Most of the hotels and restaurants will accept this solution with open hands, because this has two-way benefits of saving environments and production cost for the restaurant. 
The app is highly scalable, it is quick to produce the log, store it and produce results in real time, with minimal efforts from the user side.
Our frontend is a simple flask application, taking user inputs and using file I/O to store the data, the menu of the restaurant is stored in an SQL database. Once the user clicks the ‘Predict’ button, it runs an LSTM model in the background to predict food orders. The quantity of the food items represents time series with some seasonal behavior, sales being higher on the weekends as expected. Each food item is modeled as a separate time series, and the Deep Learning LSTM model predicts the desired order amount for the coming week for each item. The LSTM model takes in the past 30 days quantity values to predict the following 7-day order amount. The training set has 1200 unique dates starting from 2016 taken from a publicly available source on Kaggle. The database gets updated whenever a new order is placed.

## Project Roadmap

1. Generate Bill

2. Analyze food consumption patterns

3. Predict and Optimize inventory demand for future week

The application is in its final stage, it can be used in production as well, as long as we tweak the database to include the restaurant’s menu. The app will have to be used for a while, before it can make accurate predictions, the more data, the better!

There are a few new features that my team has in mind which can be inculcated into the app at later stages. For example, we can include a feature to monitor how much of the food ordered by the customers is going uneaten and predict the optimal food quantity that should be provided by the restaurant per plate to minimize losses.

Obviously, there are endless changes that we can make to the UI to make it more presentable and lucrative for users.

Our aim is to make available this technology to every major hotel to begin with. The top chains of restaurants will be more than willing to accept it because the costs they incur due to food wastage and unmanaged inventories are huge. Slowly, we plan to introduce even the smallest of the restaurants to this app when it gains momentum. Future steps would be to migrate this web app to a mobile app, as phones are available to almost all people.


## Built With

1. IBM Cloud
2. Watson Studio
3. Flask : Web framework
4. SQLAlchemy Repository

## Author

[Ishika Kumar](https://github.com/Ishika11)
[Juhi Mittal](https://github.com/juhi10071998)
[Tulika Jha](https://github.com/gally-threepwood)
[Neha Mittal](https://github.com/nehm212)
