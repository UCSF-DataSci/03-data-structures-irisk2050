#!/usr/bin/env python3
"""
Daily Quote Generator

This script selects a random quote for the day and prints it. Optional: The same quote should be generated for a given day.

Your task:
1. Complete the get_quote_of_the_day() function
2. Set up a cron job to run this script daily at 8:00 AM and append the output to a file

Hint: Look up `random.choice()` to select a random item from a list. You can use the `date` module to get the current date and set a seed for the random number generator.
"""

import random
from datetime import date

quotes = [
    # Create a list of quotes here
    "Life is like a box of chocolates. You never know what you're gonna get.",
    "If you focus on what you left behind, you will never be able to see what lies ahead.",
    "I never look back, darling! It distracts from the now.",
    "Just keep swimming.",
    "Adventure is out there.",
    "The greatest thing you will ever learn is just to love and be loved in return.",
    "May the Force be with you."
]

def get_quote_of_the_day(quotes):
    todays_quote = None

    # Your code here
    today_date = date.today()
    today_seed = today_date.toordinal()
    random.seed(today_seed)  # Seed the random generator
    todays_quote = random.choice(quotes)
    return todays_quote

if __name__ == "__main__":
    print(get_quote_of_the_day(quotes))

# Cron job (add this to your crontab):
# 0 8 * * * /usr/bin/python3 /path/to/quote_generator.py >> /path/to/daily_quote.txt