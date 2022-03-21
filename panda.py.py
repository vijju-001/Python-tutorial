# import pandas as pd
#
# calories = {"day1": 420, "day2": 380, "day3": 390}
#
# myvar = pd.Series(calories)
#
# print(myvar)

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)