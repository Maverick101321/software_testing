from booking.booking import Booking
from booking.booking_filtration import BookingFiltration
import time

with Booking(teardown=False) as bot:
    bot.land_first_page()
    #bot.change_currency(currency='INR')
    bot.select_place_to_go('Paris')
    bot.select_dates(check_in_date='2025-02-24', check_out_date='2025-02-28')
    bot.select_adults(count=4)
    bot.submit_search()

    time.sleep(5)

    filtration = BookingFiltration(bot.driver)
    #Applying star rating
    filtration.apply_star_rating(3)
    #Applying popular filters
    filtration.apply_meals_filter("mealplan=9")
    #Sorting results
    filtration.sort_by_price_lowest_best_review()

    bot.refresh()
    bot.report_results()

    #Adding this line so that the browser doesn't close immediately
    input("Press Enter to close the browser...")
