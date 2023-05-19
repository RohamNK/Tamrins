import instaloader
import getpass

f = open("followers.txt", "r")
old_followers = []
for line in f:
    old_followers.append(line[:-1])
f.close()

L = instaloader.Instaloader()
username = input ("Name karbari ra vared konid:  ")
password = getpass.getpass("Pasvord ra vared konid:  ")
L.login(username, password)
print("Vared Shdid!")

profile = instaloader.Profile.from_username(L.context, username)

new_followers = []
for follower in profile.get_followers():
    new_followers.append(follower.username)

f = open("followers.txt", "w")
for follower in new_followers:
    f.write(follower + "\n")
f.close()

for new_follower in new_followers:
    if new_follower not in old_followers:
        print(new_follower)
