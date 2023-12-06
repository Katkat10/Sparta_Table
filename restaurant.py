import math
class Table:
    def __init__(self, diners):
        self.diners = diners
        self.bill = []


    def order(self, item, price, quantity = 1):
        fl_found = False
        for entry in self.bill:
            if entry["item"] == item and entry["price"] == price:
                entry["quantity"] += quantity
                fl_found = True
        if fl_found == False:
            order_dict = {"item": item, "price": price, "quantity": quantity}
            self.bill.append(order_dict)



    def remove(self, item, price, quantity):
        for entry in self.bill:
            if entry["item"] == item and entry["price"] == price:
                if entry["quantity"] >= quantity:
                    entry["quantity"] -= quantity
                    if entry["quantity"] == 0:
                        self.bill.remove(entry)
                    return True #totaly removed
                else:
                    return False
        return False

    def get_subtotal(self):
        subtotal = sum(entry["price"] * entry["quantity"] for entry in self.bill)
        return subtotal

    def get_total(self, service_charge=0.10):
        subtotal = self.get_subtotal()
        service_charge_amount = subtotal * service_charge
        total = subtotal + service_charge_amount
        return {
            "Sub Total": f"£{subtotal:.2f}",
            "Service Charge": f"£{service_charge_amount:.2f}",
            "Total": f"£{total:.2f}"
        }

    def split_bill(self):
        subtotal = self.get_subtotal()
        split_cost = math.ceil(subtotal / self.diners * 100) / 100
        return split_cost



