import math

from SQL_Connection import Connect_to_SQL_Server
from matplotlib import pyplot as plt
from collections import Counter, OrderedDict

cursor = Connect_to_SQL_Server()


def Month_with_the_most_reservation():
    dates = {}
    for row in cursor.execute("exec Month_with_the_most_reservation"):
        if row[0] not in dates:
            dates[row[0]] = 1
        else:
            count = dates[row[0]] + 1
            dates.update({row[0]: count})

    months = dates.keys()
    count = dates.values()
    plt.bar(months, count)
    plt.ylim(0, max(count) + 1)
    plt.yticks(range(0, max(count) + 1))
    plt.xlabel("MONTH")
    plt.ylabel("Amount")
    plt.title("Month with the most reservation")
    plt.show()


if __name__ == '__main__':
    Month_with_the_most_reservation()
