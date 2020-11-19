from google.cloud import datastore

CATEGORIA = 'cryptocurrency'

def save_cryptocurrency(code, name, status):
    client = datastore.Client()
    key = client.key(CATEGORIA, code)
    entity = datastore.Entity(key=key)
    entity.update({
        'code': code,
        'name': name,
        'status': status,
    })
    client.put(entity)
    result = client.get(key)
    print(result)

save_cryptocurrency("RING", "darwinia-network-native-token", True)
