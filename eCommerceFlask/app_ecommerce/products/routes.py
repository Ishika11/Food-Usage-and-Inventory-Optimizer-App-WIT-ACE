from flask import (render_template, url_for, flash,
                   redirect, Blueprint)
from flask_login import login_required
from app_ecommerce.categories.utils import get_categories_allowed
#from app_ecommerce.products.utils import save_picture
from app_ecommerce.products.forms import ProductsForm
from app_ecommerce.models import Product, Category
from app_ecommerce import db,quote
import json


import pandas as pd
import matplotlib.pyplot as plt
from keras.models import Sequential, load_model
from keras.layers.core import Dense
from keras.layers.recurrent import LSTM
from keras import optimizers
from keras.callbacks import EarlyStopping
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, r2_score
from math import sqrt
import datetime as dt
import time
import seaborn as sns
plt.style.use('ggplot')
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from numpy import array
import numpy as np

products = Blueprint('products',__name__)

@products.route('/products/new',methods=['GET','POST'])
@login_required
def new_product():
    form = ProductsForm()
    form.category.choices = get_categories_allowed()
    if form.validate_on_submit():
        #print(form.image1.data)
        #print(form.image2.data)
        #print(form.image3.data)
        img1 = None
        img2 = None
        img3 = None
        
        cate = Category.query.get(form.category.data)
        product = Product(name=form.Item.data,
                          #description=form.description.data,
                          #weight=form.weight.data,
                          price=form.Price.data,
                          cate=cate,
                          )
        db.session.add(product)
        db.session.commit()
        flash(f'Your product has been created','success')
        return redirect(url_for('main.home'))

    return render_template('create_product.html', title='New Product', form=form, legend='New Product')

@products.route('/product/<int:product_id>')
def view_product(product_id):
    product = Product.query.get(product_id)
    return render_template('product.html', title='Product',quote=quote,product=product)


@products.route("/product/100", methods=["POST"])
def create_CSV():
    import csv;
    from flask import request
    product_quantity = request.form['quantity']
    product_name = request.form['product_name']
    fieldnames = ['Order Date', 'Item Name','Quantity', 'Price']
    product_price = request.form['product_price']
    import datetime
    ct = str(datetime.datetime.today()).split()[0]
    with open('D:/file_1.txt','a',newline="") as inFile:
            # DictWriter will help you write the file easily by treating the
            # csv as a python's class and will allow you to work with
            # dictionaries instead of having to add the csv manually.
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)
            writer.writerow({'Order Date':ct, 'Item Name':product_name,'Quantity':product_quantity, 'Price':product_price})
    return "Thanks!"


@products.route('/predic/')
def pred():
    def split_sequence(sequence, n_steps, n_out):
        X,y = list(), list()
        for i in range(len(sequence)):
            #find end of this pattern
            end_ix = i+n_steps
            out_end = end_ix + n_out
            # check if we are beyond the sequence
            if out_end > len(sequence)-1:
                break
            seq_x, seq_y = sequence[i:end_ix], sequence[end_ix:out_end]
            # gather input and output parts of the pattern
            X.append(seq_x)
            y.append(seq_y)
        return array(X),array(y)

    #getting the txt file as data and converting to dataframe
    #df=pd.read_csv("restaurant-1-orders.csv")
    with open("D:/file_1.txt", encoding="utf-8") as file:
        mylist = [l.rstrip("\n") for l in file]
    df = pd.DataFrame([sub.split(",") for sub in mylist])
    df = df.rename(columns = { 0 : 'date', 1 : 'Item_name' , 2 : 'Quantity' , 3 : 'Product Price'})
    df.head()
    df = df.astype({'Quantity': 'float'})\

    #weekddf['date'].values[0]
    import datetime

    #2021-06-17 19:06:37.295423,Paneer_Lababdar,3,200
    data = df[['date','Item_name','Quantity','Product Price']]
    data_1 = data.groupby(['date','Item_name']).agg({'Quantity' : 'sum', 'Product Price' : 'first'})
    data_1 = data_1.reset_index()
    top_20_list = ['Mint_Sauce',
    'Onion_Chutney',
    'Meat_Samosa',
    'Onion_Bhajee',
    'Chapati',
    'Chicken_Tikka_Masala',
    'Pilau_Rice',
    'Plain_Rice',
    'Bombay_Aloo',
    'Garlic_Naan',
    'Keema_Naan',
    'Plain_Naan',
    'Plain_Papadum',
    'Butter_Chicken',
    'Korma',
    'Mushroom_Rice',
    'Peshwari_Naan',
    'Saag_Aloo',
    'Mango_Chutney',
    'Korma_Chicken']

    data_filtered = data_1[data_1.Item_name.isin(top_20_list)]

    output = []
    for i in top_20_list:
        dict = {}
        df = data_filtered[data_filtered['Item_name'] == i]
        df = df.sort_values(by = 'date')
        raw_seq = df['Quantity'].tolist()
        # choose a number of time steps
        n_steps = 30
        n_out = 7
        # split into samples
        X, y = split_sequence(raw_seq, n_steps, n_out) 
        #[samples, timesteps, features]
        n_features = 1
        X = X.reshape((X.shape[0], X.shape[1], n_features))
        y = y.reshape((y.shape[0], n_out, n_features))
        x_train = X[0:len(X)-1]
        y_train = y[0:len(X)-1]
        x_test = X[-1]
        x_test = x_test.reshape(1,x_test.shape[0],x_test.shape[1])
        y_test = y[-1]
        # define model
        model = Sequential()
        model.add(LSTM(15, activation='relu', input_shape=(n_steps, n_features), return_sequences= False))
        model.add(Dropout(0.4))
        model.add(Dense(7))
        model.compile(optimizer='adam', loss='mae')
        # fit model
        model.fit(x_train, y_train, epochs=20, verbose=0)
        predicted_inventory = model.predict(x_test)
        predicted_inventory = np.round(predicted_inventory)
        dict[i] = predicted_inventory
        output.append(dict)
    with open('D:/out.txt','w') as op:
        for item in output:
            data = str(item)+"\n"
            op.write(data)
    return 'Prediction Ready!'
