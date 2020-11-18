# %%
from datetime import datetime as dt

today = dt.now()
date_string = today.strftime('%m--%d--%Y--%A--%B--%y--%H--%I--%p--%M--%S')
print(date_string) #11--11--2020--Wednesday--November--20--21--09--PM--03--20
# %%
from datetime import datetime as dt

new_years = dt(2019, 1, 1)
fall_equinox = dt(year=2019, month=9, day=22)
print(fall_equinox) #2019-09-22 00:00:00
# %%
from datetime import datetime as dt

new_years = dt.strptime('1/1/2019', '%m/%d/%Y')
print(new_years) #2019-01-01 00:00:00
my_string = new_years.strftime('%B %d, %Y')
print(my_string) #January 01, 2019
# %%
