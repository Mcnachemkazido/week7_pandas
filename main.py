import utils

if __name__ == "__main__":
    #1
    my_df = utils.read_json()
    #2
    my_df = utils.data_conversion(my_df)
    #3
    my_df = utils.removes_characters(my_df)
    #4
    my_df = utils.marks_empty_columns(my_df)
    #5
    my_df = utils.creates_a_month_column(my_df)
    #6
    my_df = utils.column_based_on_the_average(my_df)
    #7
    my_df = utils.column_rating_calculation(my_df)
    #8
    my_df = utils.filtering_the_rows(my_df)
    #9
    my_df = utils.create_a_column(my_df)
    #10
    utils.write_to_csv(my_df)
    print("Everything went successfully ,You have a file csv")