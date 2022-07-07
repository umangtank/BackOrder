## Backorder-prediction ❗
-----
<p>
Backorder is an order which can’t be fulfilled at the given time due to lack of supply or the product is currently out of stock or not in inventory but can guarantee delivery of the goods or service requested by a certain date in the future because the production of goods or replenishment of inventory is underway. Unlike in the situation of Out-of-stock where the delivery date of the goods can’t be promised , in the Backorder scenario the customers are allowed to shop for the products and order. Simply put Backorder can be thought of as an order with a delayed delivery date.
</p>
<p>
Backorders are unavoidable, but by anticipating which things will be backordered, planning can be streamlined at several levels, preventing unexpected strain on production, logistics, and transportation. ERP systems generate a lot of data (mainly structured) and also contain a lot of historical data; if this data can be properly utilized, a predictive model to forecast backorders and plan accordingly can be constructed. Based on past data from inventories, supply chain, and sales, classify the products as going into backorder (Yes or No).
</p>

### Data Analysis
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In the Train dataset we are provided with 23 columns(Features) of data.

* Sku(Stock Keeping unit) : The product id — Unique for each row so can be ignored
* National_inv : The present inventory level of the product
* Lead_time : Transit time of the product
* In_transit_qty : The amount of product in transit
* Forecast_3_month , Forecast_6_month , Forecast_9_month : Forecast of the sales of the product for coming 3 , 6 and 9 months respectively
* Sales_1_month , sales_3_month ,sales_6_month , sales_9_month : Actual sales of the product in last 1 , 3 ,6 and 9 months respectively
* Min_bank : Minimum amount of stock recommended
* Potential_issue : Any problem identified in the product/part
* Pieces_past_due: Amount of parts of the product overdue if any
* Perf_6_month_avg , perf_12_month_avg : Product performance over past 6 and 12 months respectively
* Local_bo_qty : Amount of stock overdue
* Deck_risk , oe_constraint, ppap_risk, stop_auto_buy, rev_stop : Different Flags (Yes or No) set for the product
* Went_on_backorder : Target variable

Out of the 23 features given in the dataset 15 are numerical and 8(including the target variable) are categorical features.

### Approach
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The main goal is to predict the whether a product comes in backorder or not based on different factors available in the dataset.

* Data Exploration : Exploring dataset using pandas,numpy,matplotlib and seaborn.
* Data visualization : Ploted graphs to get insights about dependend and independed variables.
* Feature Engineering : Removed missing values and created new features as per insights.
* Model Selection I : Tested all base models to check the base accuracy. Also ploted and calculate Performance Metrics to check whether a model is a good fit or not.
* Model Selection II : Performed Hyperparameter tuning using RandomsearchCV.
* Pickle File : Selected model as per best accuracy and created pickle file using pickle library.
* Webpage & deployment : Created a webform that takes all the necessary inputs from user and shows output. After that I have deployed project on AWS .

### Technologies Used
-------------------------------------------------------------------------------------------------------------------------------------------------------------

 * VS-Code Is Used For IDE.
 * For Visualization Of The Plots Matplotlib , Seaborn Are Used.
 * Heroku is Used For Model Deployment.
 * mongoDB Database Is Used To As Data Base.
 * Front End Deployment Is Done Using HTML , CSS.
 * Flask is for creating the application server and pages.
 * Git Hub Is Used As A Version Control System.
 * josn is for data validation processes.
 * os is used for creating and deleting folders.
 * csv is used for creating .csv format file.
 * numpy is for arrays computations and mathematical operations
 * pandas is for Manipulation and wrangling structured data
 * scikit-learn is used for machine learning tool kit
 * pickle is used for saving model
 * XgBoost is used for XgBoostClassifier Implementation.
 * Nearmiss Imbalance is used for handling Imbalance Data.

 ### User InterFace 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* Home Page 

<p align="center">
  <img src="Model_image\index.png" width='600px'>
</p>

* Predict Page
<p align="center">
  <img src="Model_image\predict.png" width='600px' border = "1px">
</p>


 ### Run Locally
 ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* Clone the project
```bash
  git clone https://github.com/umangtank/BackOrder
```

* Go to the project directory
```bash
  cd BackOrder
 ```

* Install dependencies
```bash
pip install -r requirements.txt
 ```

* Run the app.py
```bash
  python app.py
 ```

### Usage
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**In Development If You Want to contribute? Great!**

To fix a bug or enhance an existing module, follow these steps:

* Fork the repo

* Create a new branch
```bash
    git checkout -b new-feature
 ```

* Make the appropriate changes in the file

* Commit your changes
```bash
    git commit -m "New feature added"
 ```
* Push to the branch
```bash
    git push origin new-feature
 ```

* Create a pull request

### Help Me Improve
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Hello Reader if you find any bug please consider raising issue I will address them asap.

 * [github](https://github.com/umangtank)
  * [umangtank.me](https://umangtank.me)
   * [Linkedin](https://www.linkedin.com/in/umangtank/)
