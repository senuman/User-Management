class Vendor:
    def __init__(self, name, service, contact, rating=0):
        self.name = name
        self.service = service
        self.contact = contact
        self.rating = rating

    def get_info(self):
        return f"Vendor: {self.name}, Service: {self.service}, Contact: {self.contact}, Rating: {self.rating}"

    def update_rating(self, new_rating):
        self.rating = new_rating


class Institution:
    def __init__(self, name):
        self.name = name
        self.vendors = []

    def add_vendor(self, vendor):
        self.vendors.append(vendor)

    def remove_vendor(self, vendor_name):
        self.vendors = [v for v in self.vendors if v.name != vendor_name]

    def get_vendor(self, vendor_name):
        for vendor in self.vendors:
            if vendor.name == vendor_name:
                return vendor.get_info()
        return "Vendor not found"

    def list_vendors(self):
        return [v.get_info() for v in self.vendors]

    def update_vendor_rating(self, vendor_name, new_rating):
        for vendor in self.vendors:
            if vendor.name == vendor_name:
                vendor.update_rating(new_rating)
                return f"Updated {vendor.name}'s rating to {new_rating}"
        return "Vendor not found"

# Example code to create and manipulate objects will be commented out for review purposes:
# university1 = Institution("IUB")
# university1 = Vendor("Book Supplies Co.", "Textbooks", "546738")
# vendor2 = Vendor("Furniture Depot", "Furniture", "878674")

# university1.add_vendor(vendor1)
# university1.add_vendor(vendor2)
# print(school.list_vendors())

# university1.update_vendor_rating("Book Supplies Co.", 4)
# print(university.get_vendor("Book Supplies Co."))

# university1.remove_vendor("Furniture Depot")
# print(university1.list_vendors())
