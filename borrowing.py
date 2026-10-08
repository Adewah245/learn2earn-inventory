from data import borrow_records
from fellow import find_fellow
from resource import find_resource

def borrow_resource(fellow_id, resource_id, quantity):
    fellow = find_fellow(fellow_id)
    if fellow is None:
        return False
    resource = find_resource(resource_id)
    if resource is None:
        return False
    if not isinstance(quantity, int) or quantity <= 0 :
        return False
    if quantity > resource["available"]:
        return False
    resource["available"] -= quantity
    borrow_records.append({
        "fellow_id": fellow_id,
    })