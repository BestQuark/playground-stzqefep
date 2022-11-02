import asyncio
from instagrapi import Client

cl = Client()
cl.login(YOUR_USERNAME, YOUR_PASSWORD)

user_id = cl.user_id_from_username("borisjohnsonuk")
user_info = cl.user_info(user_id).dict()
print(user_info['follower_count'])

followers = cl.user_followers(user_id, amount = 10)
print([f.dict()['username'] for f in followers.values()])

fs = cl.user_followers(user_id, amount = 10)
fl = set(
    [f.dict()['username'] for f in fs.values()])
async def track_followers():
    while True:
        global fs, fl
        new_fs = cl.user_followers(user_id, amount=10)
        new_fl = set(
            [f.dict()['username'] for f in new_fs.values()]
        )
        print("New follows: ", list(new_fl-fl))
        print("New unfollows: ", list(fl-new_fl))
        print("------------------------")
        fs, fl = new_fs, new_fl
        await asyncio.sleep(10)

task = asyncio.create_task(track_followers())