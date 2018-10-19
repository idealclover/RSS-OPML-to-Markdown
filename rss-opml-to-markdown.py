# -*- coding: UTF-8 -*-
import listparser
import tabulate
import sys


def parse(file_name):
    result = listparser.parse(file_name)
    rst = {}
    for feed in result.feeds:
        for tag in feed['tags']:
            i = [feed['title'], feed['url']]
            rst.setdefault(tag, []).append(i)
    return rst


def print_to_std(feeds_list):
    for tag, feed_list in feeds_list.items():
        print("# " + tag + "\n")
        print(tabulate.tabulate(feed_list, headers=["title", "url"], tablefmt="pipe"))
        print("\n")


def print_to_file(feeds_list, filename):
    with open(filename, 'wt', encoding="utf-8") as f:
        for tag, feed_list in feeds_list.items():
            f.write("# " + tag + "\n")
            f.write(tabulate.tabulate(feed_list, headers=["title", "url"], tablefmt="pipe"))
            f.write("\n")


def main():
    if len(sys.argv) == 2:
        feeds_list = parse(sys.argv[1])
        print_to_std(feeds_list)
    elif len(sys.argv) == 3:
        feeds_list = parse(sys.argv[1])
        print_to_file(feeds_list, sys.argv[2])
    else:
        print("Error: argv number doesn't match")
        exit(-1)


if __name__ == "__main__":
    main()
