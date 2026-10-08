from data import resources
def list_resources():
    for resource in resources:
        print(resource)

def find_resource(resource_id) :
    for resource in resources :
        if resource["id"] == resource_id :
            return resource
    return None

def add_resource(resource_id, name, category, total):
    if find_resource(resource_id):
        return False
    resource = {
        "id": resource_id,
        "name": name,
        "category": category,
        "total": total,
        "available": total,
    }
    
    resources.append(resource)
    print("Resouce added successfully")
    return True
print(add_resource("R004", "Mouse", "Accessories", 10))
print(add_resource("R004", "Mouse", "Accessories", 10))
list_resources()