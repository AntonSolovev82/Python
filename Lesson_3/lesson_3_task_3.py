from address import Address
from mailing import Mailing

to_address = Address("196066", "Санкт-Петербург", "Гастелло", "9", "47")
from_address = Address("680001", "Хабаровск", "Гамарника", "52", "13")

mailing = Mailing(to_address, from_address, 2150, "10855213582")

print(mailing)
