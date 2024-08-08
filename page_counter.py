
import datetime as dt


def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("deadline", help="Day to be done",
                         type=lambda s: dt.datetime.strptime(s, '%Y-%m-%d'))
    parser.add_argument("total", help="Total pages",
                        type=int)
    parser.add_argument("current", help="Current page",
                        type=int)
    parser.add_argument("start", nargs='?',
                        default=dt.datetime.now()
                          .replace(hour=0, minute=0,
                                   second=0, microsecond=0),
                        type=lambda s: dt.datetime.strptime(s, '%Y-%m-%d'),
                        help="Date to start.  Default: today")
    args = parser.parse_args()
    return args


def abort(msg):
    print("error: " + msg)
    exit(1)


def main():
    args = parse_args()
    span = args.deadline - args.start
    if span.days < 0: abort("time span is negative!")
    print("days to go: %4i" % span.days)
    pages = args.total - args.current
    if pages < 0: abort("pages remaining is negative!")
    print("pages left: %4i" % pages)
    rate = pages / span.days
    print("pages/day:  %6.1f" % rate)
    print("")

    import random
    limit = min(5, span.days)
    for i in range(0, limit):
        td = dt.timedelta(days=i)
        day = args.start + td
        print(day.strftime(" %Y-%m-%d "), end='')
        page = args.current + rate * (i + 1)
        ipage = int(page) + (random.random() < page - int(page))
        print("%4i" % ipage)


if __name__ == "__main__":
    main()
