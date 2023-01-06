import re

#Check if the email is valid or not
def is_valid_email(email):
	regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

	if re.match(regec,email):
		return True
	else:
		return False

print(is_valid_email(sampleEmail@example.com))
