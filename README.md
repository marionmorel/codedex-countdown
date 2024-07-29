# Countdown

## Codedex Project - Python

Let's use the <code>datetime</code> and <code>random</code> modules to make a birthday card to determine how far your birthday is from today! 🎂

For this exercise, we are creating *two* **.py** files in a separate code editor.

## bday_messages.py

Create a new file called bday_messages.py.

Import the <code>random</code> module.

Then, define a <code>bday_messages</code> list with the following items:

- 'Hope you have a very Happy Birthday! 🎈',
- 'It's your special day – get out there and celebrate! 🎉',
- 'You were born and the world got better – everybody wins! 🥳',
- 'Have lots of fun on your special day! 🎂',
- 'Another year of you going around the sun! 🌞'

Next, use the <code>random.choice()</code> method to get a single item from the list.

Save this item in a <code>random_message</code> variable.

Let's save **bday_messages.py** and move to the next part.

## main.py

Create a new file called **main.py**.

Import both the <code>datetime</code> module as well as <code>bday_messages</code> (the last file).

``` console
import datetime, bday_messages
```

Next, use the <code>datetime</code> module to create two <code>date</code> objects:

- <code>today</code>: Today's date, using the <code>datetime.date.today()</code> method.
- <code>next_birthday</code>: The date for your next birthday, using the <code>year</code>, <code>month</code>, and <code>day</code> arguments.

A really cool thing you can do with <code>date</code> objects is addition and subtraction!

``` console
time_difference = date1 - date2
```

Use date subtraction to calculate how many days away <code>today</code> is from <code>next_birthday</code>. Then, assign the result to a new variable called <code>days_away</code>.

Then, create a control flow statement:

- If <code>today</code> is equal to <code>next_birthday</code>, print the <code>random_message</code> variable (imported from <code>bday_messages</code>).
- Else, print <code>'My next birthday is {days_away} days away!'</code>.
The output should look something like this:

``` console
My next birthday is 42 days away!
```

Bonus: Instead of using a date in the future, what if we tried to see how many days it's been since a past event, like the release date of your favorite movie or game, or the date you were born? What about how many years or months it's been?