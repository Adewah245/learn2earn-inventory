from data import fellows
def list_fellows():
    for fellow_id, name in fellows.items():
        print(fellow_id, name)

def find_fellow(fellow_id) :
    return fellows.get(fellow_id)
