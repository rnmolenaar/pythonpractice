# A function that returns a generator that yields every month of the year
def year():
  months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
  ]

  for month in months: 
    yield month

# to toggle between two different possible answers. If it was white before, it's black next


def chess_match():
    turn = "white"
    while True:
        yield turn
        answer ="black" if answer == "white" else "white"

#
