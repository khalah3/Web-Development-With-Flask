from flask import Flask
import random


app=Flask(__name__)

#This defines a decotrator that adds h1 heading and an image around any function (such as guess_number() below
def site_decorator(function):
    def wrapper():
        return '<h1>' + function()+ '</h1>'  \
               '<img src="https://media2.giphy.com/media/uLgd9dOYWpnu5WkShY/giphy.webp?cid=790b76114ns34q1irh6g9gtkgl0df20c0rpmfvp8vkknfg3j&ep=v1_gifs_trending&rid=giphy.webp&ct=g" width=500>'
    return wrapper

@app.route('/') #This will create a server on your local machine with the home address denoted by '/'
@site_decorator  #This will apply the decorator defined above by site_decorator(function)
def guess_number():
    return 'Guess a number between 0 and 9\n'


@app.route('/<int:user_input>')
def take_a_guess(user_input):
    random_number = random.randint(1, 10)
    if random_number > user_input:
        #give a style and color
       return f'<h1 style="color:red">{user_input} is too low. The correct number is {random_number}</h1>' \
       #add an image
       "<img src='https://media.giphy.com/media/M9yC8b0x7Y7oA/giphy.gif' width='400' height='400'>"
    elif random_number < user_input:
        # give a style and color
        return f'<h1 style="color:red">{user_input} is too high. The correct number is {random_number}</h1>' \
            # add an image
        '<img src="https://media.giphy.com/media/LcoK2zRKbQlUc/giphy.gif">'
    else:
        return f'<h1 style="color:green">{user_input} is the correct number</h1>' \
        "<img src='https://media.giphy.com/media/ekNBF5OU8whqp8YqFD/giphy.gif' width='300' height='300'>"


if __name__=='__main__':
    app.run(debug=True)



