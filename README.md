# flask-todo

This is my TODO app for PSET 0b of CS178.

## Aid used

I used the [bootstrap 5.3 documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/) extensively for styling. Note that some of the colors I used (e.g. #031633) were taken from bootstrap colors via inspect element, since for some reason `--bs-primary-bg-subtle` didn't work (following same example).

I used [HTMX's documentation](https://htmx.org/) to try to learn HTMX.

I had to remind myself how to update data using flask_sqlalchemy, which I found in their documentation [here](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/#query-the-data).

I used some of the work I've done for CS50 recently to speed up setting up the flask, a lot of `app.py` up until line 29 is copied directly from a (currently unreleased, else I would link it for credit) project I worked on over the winter break for cs50.

## Bugs fought

I wanted completed todos to be fuzzed out and have text content displayed with a strike-through. Styling the outer div (`.todo-item`) cascaded that `text-decoration` down to all lower elements, including the buttons. I was hopeful that there was a way to exlcude certain children elements, but after a quick Google and reading this Stack Overflow thread: [text-decoration bug](https://stackoverflow.com/questions/1261955/inherited-text-decoration-style), it became clear that isn't possible, and I had to tinker with both the HTML and CSS to get the effect I wanted.

I also wanted to be able to complete tasks via a built-in HTML `checkbox` `input` type, but combining this with HTMX was causing me issues. This is my first time using HTMX, so there may be a way around it, but I couldn't find it in the documentation or online, and I briefly tried using ChatGPT but I think HTMX is still too new/niche to provide any meaningful aid currently. I actually created a Stack Overflow account to see if I could get some help, and posted a [question here](https://stackoverflow.com/questions/77862122/htmx-interaction-with-checkboxes?noredirect=1#comment137270853_77862122), and I've just seen that someone replied with what seems like it could solve my problems! I had already shifted to just using a more conventional button, but I'll give their suggestion a try on a branch and see if it does solve the issue so that I can mark it as correct on the thread.