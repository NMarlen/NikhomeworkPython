from address import Address
from mailing import Mailing


from_addr = Address("101000", "Москва", "Тверская", "12", "45")
to_addr = Address("190000", "Санкт-Петербург", "Невский проспект", "55", "10")

mail = Mailing(to_addr, from_addr, 350, "TR123456789RU")

print(
    f"Отправление {mail.track} "
    f"из {mail.from_address.index}, {mail.from_address.city}, "
    f"{mail.from_address.street}, {mail.from_address.house} - "
    f"{mail.from_address.apartment} "
    f"в {mail.to_address.index}, {mail.to_address.city}, "
    f"{mail.to_address.street}, {mail.to_address.house} - "
    f"{mail.to_address.apartment}. "
    f"Стоимость {mail.cost} рублей."
)
