from booking.booking import Booking

with Booking(teardown=False) as bot:
    bot.land_first_page()
    #bot.change_currency(currency='INR')
    bot.select_place_to_go('New York')
    bot.select_dates(check_in_date='2025-02-14', check_out_date='2025-02-24')
    bot.select_adults(count=4)
    bot.submit_search()
    input("Press Enter to close the browser...")
