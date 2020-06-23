#!/usr/bin/python3

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset_unix.pkl", "rb"))

##number of data point in email + fin list
print("The number of data point = {}".format(len(enron_data)))

##number of features for each point
num_feat = 0
for keys in enron_data.keys():
    num_feat = len(enron_data[keys])

print("The number of features for each point = {}".format(num_feat))
##number of POI == 1
count = 0
for keys in enron_data.keys():
    if enron_data[keys]["poi"] == 1:
        count += 1

print("The number of POI = {}".format(count))

##total value of stock for James Prentice
print("total value of the stock belonging to James Prentice = {}".format(enron_data['PRENTICE JAMES']['total_stock_value']))

##number of email messages we have from Wesley Colwell to persons of interest
print("total number of emails from Wesley Colwell to persons of interest = {}".format(enron_data['COLWELL WESLEY']['from_this_person_to_poi']))


##code base for searching enron data dictionary
print(enron_data)
names = list(enron_data.keys())
for i in names:
     if 'skilling'.upper() in i:
         print(i)
         print(i,':', enron_data[i], '\n')

##find POI with no salary record and POI with no email address
no_salary = 0
no_email = 0
for keys in enron_data.keys():
    if enron_data[keys]['salary'] == "NaN":
        no_salary += 1
    elif '.com' in enron_data[keys]['email_address']:
        no_email += 1
print(len(enron_data) - no_salary)
print(no_email)

##POI with no Total Payments
num_no_total_pay = 0
for keys in enron_data.keys():
    if enron_data[keys]['total_payments'] == "NaN":
        num_no_total_pay += 1
print(num_no_total_pay)

##number of POI == 1 and total payment = NaN
count_POI_total_pay_NAN = 0
for keys in enron_data.keys():
    if enron_data[keys]["poi"] == 1 and enron_data[keys]["total_payments"] == "NaN":
        count_POI_total_pay_NAN += 1
print(count_POI_total_pay_NAN)

high_b1 = 0
high_s1 = 0
high_b2 = 0
high_s2 = 0
high_b3 = 0
high_s3 = 0
high_b4 = 0
high_s4 = 0
high_b5 = 0
high_s5 = 0
keyy1 = ''
keyy2 = ''
keyy3 = ''
keyy4 = ''
keyy5 = ''
for keys in enron_data.keys():
    if enron_data[keys]['salary'] == 'NaN' or enron_data[keys]['bonus'] == 'NaN':
        continue
    elif int(enron_data[keys]['salary']) >= high_s1 and int(enron_data[keys]['bonus']) >= high_b1:
        high_s5 = high_s4
        high_s4 = high_s3
        high_s3 = high_s2
        high_s2 = high_s1
        high_s1 = int(enron_data[keys]['salary'])
        high_b5 = high_b4
        high_b4 = high_b3
        high_b3 = high_b2
        high_b2 = high_b1
        high_b1 = int(enron_data[keys]['bonus'])
        keyy5 = keyy4
        keyy4 = keyy3
        keyy3 = keyy2
        keyy2 = keyy1
        keyy1 = keys
print(keyy1,".....", keyy2,"....",keyy3,"...", keyy4, "...", keyy5)