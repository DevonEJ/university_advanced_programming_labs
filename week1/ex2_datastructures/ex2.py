import itertools


sales_data = {
    "L3": {
        "figures" : [["April 18", "May 18", "June 18"],
           [390, 345, 379]],
        "location": "London"
    },
    "P2": {
        "figures": [["April 18", "May 18", "June 18"],
            [250, 270, 300]],
        "location": "Paris"
    },
    "N6": {
        "figures":
        [["April 18", "May 18", "June 18"],
            [460, 480, 450]],
        "location": "New York"
    },
    "B8": { "figures":
        [["April 18", "May 18", "June 18"],
          [470, 510, 360]],
          "location": "Beijing"
    }
}


print("Quarterly sales report")
print()

apr_figures = []
may_figures = []
jun_figures = []

all_figures = []

all_dates = []

total_space_padding =  16

for key, sub_dict in sales_data.items():
    # Collect figures and dates for second line of report
    apr_figures.append(sub_dict["figures"][1][0])
    may_figures.append(sub_dict["figures"][1][1])
    jun_figures.append(sub_dict["figures"][1][2])

    # Create first line of report
    total_figure_count = len(sub_dict["figures"][1])
    total_figure_sum = sum(sub_dict["figures"][1])
    location_name = sub_dict["location"]
    space_padding = " " * (total_space_padding - len(location_name) - len(key))
    print(location_name + space_padding, key + ":", "$" + str((total_figure_sum // total_figure_count)), "$" + str(total_figure_sum), sep="  ")

all_figures.append(apr_figures)
all_figures.append(may_figures)
all_figures.append(jun_figures)
all_dates = all_dates + sales_data["L3"]["figures"][0]

print()
# Shorten dates
for ind, date in enumerate(all_dates):
    short_date = date[:3] + date[-2:]

    # Second line of report
    date_figure_sum = sum(all_figures[ind])
    date_figure_count = len(all_figures[ind])

    space_padding = " " * (total_space_padding - len(short_date) + 1)

    print(short_date + space_padding, ":", " $" + str((date_figure_sum // date_figure_count)), " $" + str(date_figure_sum))

# Grand total line of report
combined_sales = itertools.chain.from_iterable(all_figures)

print()
print("Total:", "$" + str(sum(combined_sales)))

