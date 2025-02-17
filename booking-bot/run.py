from booking.booking import Booking
from booking.booking_filtration import BookingFiltration

with Booking(teardown=False) as bot:
    bot.land_first_page()
    #bot.change_currency(currency='INR')
    bot.select_place_to_go('Paris')
    bot.select_dates(check_in_date='2025-02-24', check_out_date='2025-02-28')
    bot.select_adults(count=4)
    bot.submit_search()

    filtration = BookingFiltration(bot.driver)
    filtration.apply_star_rating(3, 4)
    #bot.apply_filtrations()
    input("Press Enter to close the browser...")
