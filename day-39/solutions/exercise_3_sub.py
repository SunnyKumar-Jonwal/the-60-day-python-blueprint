import re

messy = "This   has    way too   many spaces."

cleaned = re.sub(r" +", " ", messy)
print(cleaned)
