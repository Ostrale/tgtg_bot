from tgtg import TgtgClient

from data import myaccess_token, myrefresh_token, myuser_id, mycookie
client = TgtgClient(access_token=myaccess_token, refresh_token=myrefresh_token, user_id=myuser_id, cookie=mycookie)

#908377

# You can then get some items, by default it will *only* get your favorites
items = client.get_items()
print(items)

# To get items (not only your favorites) you need to provide location informations
items = client.get_items(
    favorites_only=False,
    latitude=48.126,
    longitude=-1.723,
    radius=10,
)
print(items)