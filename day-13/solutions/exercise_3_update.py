profile = {"username": "ada99", "followers": 100}

profile["verified"] = True
print(profile)

profile["followers"] = 150
print(profile)

del profile["username"]
print(profile)
