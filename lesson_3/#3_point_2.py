#point_2
def user_info(f_name, s_name, year, city, email, phone):
    print(f'Имя: {f_name}\nФамилия: {s_name}\nГод рождения: {year}\nГород: {city}\nEmail: {email}\nТелефон: {phone}')
    return True


f_name, s_name, year, city, email, phone = input().split()
user_info(f_name = f_name, s_name = s_name, year = year, city = city, email = email, phone = phone)