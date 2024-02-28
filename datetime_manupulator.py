# from datetime import datetime, timedelta
# import math

# today = datetime.now().date()
# print(today)

# datetime_list = [
#     datetime(2022, 10, 12).date(),
#     datetime(2023, 8, 12).date(),
#     datetime(2023, 9, 12).date(),
#     datetime(2023, 10, 12).date(), #future
#     datetime(2023, 11, 18).date(), #future
# ]

# print(((max(datetime_list)+timedelta(days=14))-today).days/7)
# max_arrival = max(datetime_list)
# etd_date = max_arrival+timedelta(days=14) if max_arrival > today else today + timedelta(days=14)
# etd_date_days = (etd_date-today).days
# etd_date_weeks = (etd_date-today).days/7
# print("etd_date days", etd_date_days)
# print("etd_date weeks", etd_date_weeks)

# print(f"{math.floor(etd_date_weeks)}-{math.ceil(etd_date_weeks)} Weeks")

# print(min(datetime_list))
# print(max(datetime_list))


# dic = [{
#             "nw_date_init":  max_arrival+timedelta(days=14),
#             "nw_quantity_init": 5.0,
#             "sw_date_init": False,
#             "sw_quantity_init": 0.0,
#         }, {
#             "nw_date_init": max_arrival+timedelta(days=7),
#             "nw_quantity_init": 5.0,
#             "sw_date_init": False,
#             "sw_quantity_init": 0.0,
#         }, {
#             "nw_date_init": max_arrival,
#             "nw_quantity_init": 10.0,
#             "sw_date_init": False,
#             "sw_quantity_init": 0.0,
#         }]




from datetime import datetime, timedelta

def get_start_end_of_week():
    # Get the current date
    current_date = datetime.now().date()

    # Calculate the start of the week (Monday)
    start_of_week = current_date - timedelta(days=current_date.weekday())

    # Calculate the end of the week (Sunday)
    end_of_week = start_of_week + timedelta(days=6)

    # Combine with time information if needed
    start_datetime = datetime.combine(start_of_week, datetime.min.time())
    end_datetime = datetime.combine(end_of_week, datetime.max.time())

    return start_datetime, end_datetime

# Get the start and end datetime of the current week
start, end = get_start_end_of_week()

# Print the results
print(f"Start of the week: {start}")
print(f"End of the week: {end}")
