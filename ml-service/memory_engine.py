memory_store = []

def remember(query, response):
    memory_store.append({"q": query, "a": response})

def retrieve_memory(query):
    for item in memory_store[::-1]:
        if query.lower() in item["q"].lower():
            return item["a"]
    return None