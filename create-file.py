#!/usr/bin/env python

import os
import datetime
import click

@click.command()
@click.option("--filename", help="Type your filename")

def file_date(filename):
    # Create the file in the current directory
    new_file = open(filename, "w")
    path = os.path.join(os.getcwd(), filename)
    timestamp =os.path.getmtime(path)
    date=datetime.datetime.fromtimestamp(timestamp)
    str_date=str(date)
    date_list=str_date.split(" ")
    return ("{}".format(date_list[0]))

if __name__ == "__main__":
    file_date()