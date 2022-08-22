from googleapi import google
euros = google.convert_currency(5.0, "USD", "EUR")
print("5.0 USD = {0} EUR".format(euros))