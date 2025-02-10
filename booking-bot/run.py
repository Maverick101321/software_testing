from booking.booking import Booking

with Booking(teardown=False) as bot:
    bot.land_first_page()
    input("Press Enter to close the browser...")
