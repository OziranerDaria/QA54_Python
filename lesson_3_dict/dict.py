books = {
    'Lev Tolstoy' : 'Anna Karenina',
    'Anton Chekhov' : 'The Chetty Orchard'
}
books2 = {'Lev Tolstoy',
          'Anton Chekhov'
}
print(books2)

response = {  #ответ
    'statusCode' : '200',
    'user' :{
        'id' :1,
        'name' : 'Kristina'
            }
}
print(response['user']['name'])

data = [1,2,33]
print(isinstance(data, list))

value = 22.0
print(isinstance(value, float))

team_ages = {
    "Kristina": 39,
    "Alex": 40,
    "Tatiana": 54,
    "Andrey": 44,
    "Vladimir": 55
}
print(team_ages.keys())
print(team_ages.values())

team_names = "Kristina","Alex","Tatiana","Andrey","Vladimir"
team_num = [39,40,54,44,55]
team_ages = {name: age for name,age in zip(team_names,team_num)} #склеивает несколько значений
print(team_ages)