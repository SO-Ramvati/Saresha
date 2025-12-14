from academic import academic_response
from personal import personal_response

def get_response(user_input, mode):
    if mode == "academic":
        return academic_response(user_input)
    else:
        return personal_response(user_input)
