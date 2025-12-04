import pandas as pd


def read_json():
    return pd.read_json("orders_simple.json")


def data_conversion(df):
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["total_amount"] = df["total_amount"].str.replace("$", "")
    df["total_amount"] = df["total_amount"].astype(float)
    return df


def removes_characters(df):
    df["items_html"] = df["items_html"].str.replace("<b>","")
    df["items_html"] = df["items_html"].str.replace("</b>"," ")
    df["items_html"] = df["items_html"].str.replace("<br>"," ")
    return df


def marks_empty_columns(df):
    df["coupon_used"] = df["coupon_used"].replace("","no coupon")
    return df


def creates_a_month_column(df):
    df["order_month"] = df["order_date"].dt.month
    return df


def column_based_on_the_average(df):
    average_total_amount = df["total_amount"].mean()
    df = df.assign(hith_value_order= lambda x : x.total_amount > average_total_amount)
    df = df.sort_values(by="total_amount" ,ascending=False)
    return df


def column_rating_calculation(df):
    rating_average = df.groupby("country")["rating"].transform("mean")
    df["average_by_country"] = rating_average
    return df


def filtering_the_rows(df):
    df = df.query('(total_amount > 1000) & (rating > 4.5)')
    return df


def value_check(x):
    if x > 7:
        return "delayed"
    else:
        return "on time"


def create_a_column(df):
    df["delivery_status"] = df["shipping_days"].apply(value_check)
    return df


def write_to_csv(df):
    df.to_csv("clean_orders_[ID_NUMBER].csv")







