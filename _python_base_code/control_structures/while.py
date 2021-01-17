# %%
# ? simple while loop
current_value = 1
while current_value <= 5:
    print(current_value)  # 1, 2, 3, 4, 5
    current_value += 1
# %%
# ? choose when quit
msg = ''
while msg != 'quit':
    msg = input("Your message")
    print(msg)
# %%
# ? use flag
active = True
while active:
    message = input("If something run, if quit then quit")

    if message == 'quit':
        active = False
    else:
        print(message)
# %%
# ? using break to exit loop
while True:
    city = input("something or quit")
    if city == 'quit':
        break
    else:
        print(city)
# %%
# ? using continue in loop
banned_users = ['eve', 'fred', 'gary', 'helen']
prompt = "\nAdd player to your team"
prompt += "\nEnter quit when you're done"

players = []
while True:
    player = input(prompt)
    if player == 'quit':
        break
    elif player in banned_users:
        print(f" {player} is banned!")
        continue
    else:
        players.append(player)
print("\nYour team: ")
for player in players:
    print(player)

# %% while loop skończona
i = 1
while i <= 5:
    print(i)  # 1,2,3,4,5
    i = i + 1
print("Finished")  # Finished
# %%
i = 0
while True:
    print(i)  # 0, 1, 2, 3, 4
    i = i + 1
    if i >= 5:
        print("Breaking")  # i = 5 so Breaking
        break
print("Finished")  # Finished
# %%
i = 1
while i <= 5:
    print(i)
    i += 1
    if i == 3:
        print("Skipping 3")
        continue
