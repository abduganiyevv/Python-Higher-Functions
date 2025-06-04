from randomusers import randomusers_data

def get_email_list(users: list[dict]) -> list[str]:
    emails=[]
    for user in users :
        emails.append(user['email'])
    return emails

def get_name_list(users: list[dict]) -> list[str]:
    names = []
    for user in users:
        names.append(user['name'])
    return names

def get_country_list(users: list[dict]) -> list[str]:
    countries = []
    for user in users:
        countries.append(user['country'])
    return countries

def get_phone_list(users: list[dict]) -> list[str]:
    phones = []
    for user in users:
        phones.append(user['phone'])
    return phones

def get_city_list(users: list[dict]) -> list[str]:
    cities = []
    for user in users:
        cities.append(user['city'])
    return cities

def get_oldest_list(users: list[dict]) -> list[str]:
    for user in users:
        max_age = max(user["age"] )
        for user in users:
         if user["age"] == max_age:
            return user

def get_youngest_list(users: list[dict]) -> dict:
    for user in users:
        min_age = min(user["age"] )
        for user in users:
            if user["age"] == min_age:
                return user


def main() -> None:
    results = randomusers_data["results"]
    email_list = get_email_list(results)
    print(email_list)

    results = randomusers_data["results"]
    name_list = get_name_list(results)
    print(name_list)

    results = randomusers_data["results"]
    country_list = get_country_list(results)
    print(country_list)

    results = randomusers_data["results"]
    phone_list = get_phone_list(results)
    print(phone_list)

    results = randomusers_data["results"]
    city_list = get_city_list(results)
    print(city_list)
    
    results = randomusers_data["results"]
    oldest = get_oldest_list(results)
    print(oldest)

    results = randomusers_data["results"]
    youngest = get_youngest_list(results)
    print(youngest)

if __name__ == "__main__":
    main()
