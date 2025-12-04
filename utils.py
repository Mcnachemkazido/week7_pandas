from sys import prefix

import pandas as pd

df = pd.read_json("orders_simple.json")


#1
df["order_date"] = pd.to_datetime(df["order_date"])
df["total_amount"] = df["total_amount"].str.replace("$", "")
df["total_amount"] = df["total_amount"].astype(float)



#2
df["items_html"] = df["items_html"].str.replace("<b>","")
df["items_html"] = df["items_html"].str.replace("</b>"," ")
df["items_html"] = df["items_html"].str.replace("<br>"," ")


#3
df["coupon_used"] = df["coupon_used"].replace("","no coupon")

#4
df["order_month"] = df["order_date"].dt.month

#5
average_total_amount = df["total_amount"].mean()
df = df.assign(hith_value_order= lambda x : x.total_amount > average_total_amount)
df = df.sort_values(by="total_amount" ,ascending=False)

#6
rating_average = df.groupby("country")["rating"].transform("mean")
df["average_by_country"] = rating_average

#7
df = df.query('(total_amount > 1000) & (rating > 4.5)')

#8

def value_check(x):
    if x > 7:
        return "delayed"
    else:
        return "on time"

df["delivery_status"] = df["shipping_days"].apply(value_check)


#9
df.to_csv("clean_orders_[ID_NUMBER].csv")







