
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
    parser.add_argument("start", nargs='?', default=dt.datetime.now(),
                        type=lambda s: dt.datetime.strptime(s, '%Y-%m-%d'),
                        help="Date to start.  Default: today")
    args = parser.parse_args()


    return args

def validate(args):
    pass

def main():
    args = parse_args()
    print(str(args))
    span = args.deadline - args.start
    print("days to go: %3i" % span.days)
    pages = args.total - args.current
    print("pages left: %3i" % pages)
    rate = pages / span.days
    print("pages/day:  %5.1f" % rate)

    import random
    limit = 5
    for i in range(0, limit):
        td = dt.timedelta(days=i)
        day = args.start + td
        print(day.strftime("%Y-%m-%d "), end='')
        page = args.current + rate * i
        print("page:  %4.1f" % page)
        ipage = int(page) + (random.random() < page - int(page))
        print("ipage: %4.1f" % ipage)

if __name__ == "__main__":
    main()
