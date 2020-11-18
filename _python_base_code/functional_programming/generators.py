#Generatory - typy iterowane jak listy czy tuple, nie można ich indexować,
# ale można je iterować za pomocą pętli for. Tworzy sie je instrukcją yield
#generatory generują jedną pozycje na raz
# %%
def count_down():
    i = 5
    while i > 0:
        yield i
        i -= 1
print(list(count_down())) #[5, 4, 3, 2, 1]
# %%
