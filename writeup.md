# CS178 PSET0b Writeup
## Andrew Holmes


### Question 1: Svelte tutorial

**Work through this [Svelte.js tutorial](https://svelte.dev/tutorial/basics). long enough (at least through Sections 1 and 2) to compose 3-5 candidate “concepts” (as described in the first pre-class reading) by thinking of the Svelte framework design as a UI for specifying what you want the computer to do (as approximately described by the second pre-class reading). In your write-up, list these candidate concepts; give each abstract concept a name, provide one or more examples of its concrete syntax, and describe its purpose.**

1. A 'login' concept is often important, to separate parts of systems that should only permit authenticated users' access. Here's a really basic login idea, just having a button that logs you in by giving you a unique username (basically a gensym username) and shows the current list of logged in users.

```html
<script>
	let count = 0;
	let logged_in_users = [];

	function login(user) {
		logged_in_users = [...logged_in_users, user];
		count += 1;
	}
</script>

<button on:click={() => login("user" + count)}>
	Clicked
</button>

<p>Logged in: {logged_in_users}</p>

```


### Question 2: Flask todo app

**Do the same (in your write-up, compose a corresponding list of candidate concepts) for any Flask Todo app tutorials, e.g., https://www.python-engineer.com/posts/flask-todo-app/. (Look for the one you like best!) Specify in your submission which one (or combination of tutorials) you found most helpful. In your write-up, provide a public link to Github or Github-equivalent with your code, and let us know if you got a to-do app up and working locally. Bonus points if you comment your code to indicate where your candidate concepts are instantiated!)**

I implemented a todo app using Flask and HTMX, you can view my [repository here](https://github.com/ACHolmes/flask-todo). I didn't use the tutorial, as per the next question, I have some experience in Flask and wanted to do this by myself as a way of learning HTMX, which I've never used. I have a working TODO app, with the capability to add, delete or mark todos as complete. Credits for resources I used beneath the concepts.

1. The **add** concept is probably the most obvious concept here, with the ability to add to a list a fundamental component of a todo list. I have it visually signalled by a bootstrap form element (with classic white background text boxes with placeholders for input, and a green 'submit' style button to add).
2. In turn, the **delete** concept gives the possibility to permanently delete a todo item, again visually signalled with the classic 'big red button' signifying dangerous or destructive actions.
3. The **complete** concept allows for the completion or 'ticking off' of todos, as you would do with a physical todo list. It differs from the deletion concept since many (myself included) find it satisfying and motivating to be able to see not just tasks that we need to do, but also those which we have already completed (or perhaps are in progress, which I don't have here).

#### Credits

I used the [bootstrap 5.3 documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/) extensively for styling. Note that some of the colors I used (e.g. #031633) were taken from bootstrap colors via inspect element, since for some reason `--bs-primary-bg-subtle` didn't work (following same example).

I used [HTMX's documentation](https://htmx.org/) to try to learn HTMX.

I had to remind myself how to update data using flask_sqlalchemy, which I found in their documentation [here](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/#query-the-data).

I used some of the work I've done for CS50 recently to speed up setting up the flask, a lot of `app.py` up until line 29 is copied directly from a (currently unreleased, else I would link it for credit) project I worked on over the winter break for cs50.


### Question 3: Bugs, prior experience

**In your write-up, for each of the two frameworks, tell us about a code or mental bug that you debugged, and how you did it (or couldn’t and what you tried). Did anyone within or beyond the class help you, and if so, how? (We're a learning community! Debugging is part of the process, and it's good to help each other. Give credit generously.)**

**Tell us what prior experiences (if any) you have with that framework.**

#### Bugs/challenges

* Flask todo app

  * I wanted completed todos to be fuzzed out and have text content displayed with a strike-through. Styling the outer div (`.todo-item`) cascaded that `text-decoration` down to all lower elements, including the buttons. I was hopeful that there was a way to exlcude certain children elements, but after a quick Google and reading this Stack Overflow thread: [text-decoration bug](https://stackoverflow.com/questions/1261955/inherited-text-decoration-style), it became clear that isn't possible, and I had to tinker with both the HTML and CSS to get the effect I wanted.

  * I also wanted to be able to complete tasks via a built-in HTML `checkbox` `input` type, but combining this with HTMX was causing me issues. This is my first time using HTMX, so there may be a way around it, but I couldn't find it in the documentation or online, and I briefly tried using ChatGPT but I think HTMX is still too new/niche to provide any meaningful aid currently. I actually created a Stack Overflow account to see if I could get some help, and posted a [question here](https://stackoverflow.com/questions/77862122/htmx-interaction-with-checkboxes?noredirect=1#comment137270853_77862122), and I've just seen that someone replied with what seems like it could solve my problems! I had already shifted to just using a more conventional button, but I'll give their suggestion a try on a branch and see if it does solve the issue so that I can mark it as correct on the thread.

#### Prior experience

I have essentially no prior experience at all with Svelte, I've looked at one page of svelte code in the [classes.wtf repository](https://github.com/ekzhang/classes.wtf) because I was curious how they handled such fast course search, but I've looked at it for no more than 10 minutes before.

Flask is a very different story - I first used Flask as a CS50 student in Fall 2020, and I have TF'd the course every Fall semester since, so I have quite a lot of experience with the basics of using Flask. In addition, last summer I worked for CS50 as a software engineer, where I helped build [cs50.ai](https://cs50.ai/) (GitHub login required to properly use), which used Flask. Finally, I again worked for CS50 for the January term for two weeks before this spring semester started, working on a new project as a full-stack web engineer, again using Flask for the backend. I was more focused on the frontend (pure JS, we are always constrained to use Flask + JS so that future maintainers of all of CS50's tools only need to learn one set of tools), but did work on the backend/with flask for a few days, especially at the beginning, before shifting focus to the frontend and writing primarily JavaScript.


### Question 4: Comparisons & Judgements


* **In your write-up, tell us what's most usable about each and least usable about each for you, given your prior programming experiences.**
* **Tell us two similarities and two differences between the two framework**
* **Tell us which framework you would prefer using in the future, given a choice, and why.**

#### Answers

* Svelte
  * Svelte's reacitivity capabilities seem, from a first play, super nice. I don't particularly like the `$:` syntax, but I guess it is short and doesn't clash hugely elsewhere, but I love how it functions and it seems to provide significant power to the developer to quickly create and easily manage shared state that might be displayed in multiple places/modalities.
  * On the other hand, I generally find JavaScript a nuisance. I have never used a NoSQL database, so I always find it hugely frustrating to incur the cost of the server serializing and object to JSON, and then the frontend deserializing it to be able to modify HTML/display content. It's lack of safety around `NaN`, `null` and `undefined` are a constant thorn, and I think the console error messages are generally very low quality and find debugging a huge chore in the language.
* Flask
  * The main appeal of Flask is the generally widely accepted usability of Python itself, which lots of software engineers are familiar with and allows for generally quick prototyping. I am also extremely biased as I've used it a lot, so I find it intuitive!
  * I think some of the flask add-ons are not as great as other frameworks. In particular, `flask_sqlalchemy` is somewhat confusing and not the best documented in my opinion.
  * I would also say that using Python is also one of its main disadvantages - having a full JS stack (e.g. MERN) has the appeal of uniformity in language, even if React code (especially with JSX, styled-components) looks nothing like Express code, it is still fundamentally the same language so for small teams, those may be eaiser to handle/train/learn.
  * Flask also generally relies on `render_template` for displaying pages, and this then almost necessitates a basic familiarity with `Jinja`, thus Flask actually introduces two languages into your stack, which may feel like one or two more languages than desired.

**Two similarities**:

1. Both have some sort of component capability, with Svelte's closer to what I know from React components (e.g. `import Nested from './Nested.svelte'` from the tutorial), while Flask provides macros (`{ % macro %}` etc) in Jinja along with a templating system (`{% extends %}`, `{% block ... %}` etc) to reduce copy-paste code and having to update code duplicates in multiple locations.
2. Both can directly modify the DOM, Flask via `render_template` and Flask via HTML/CSS/JS.
3. Both seem to be relatively beginner-friendly, as compared to frameworks such as Angular or using some of the trickier backend tools like Rocket (Rust).

**Two differences**:

1. Svelte seems to place great emphasis on reactivity and making handling DOM updates as easy as possible. Flask out of the box does almost nothing to help with reactivity beyond regular HTML/JS capabilities.
2. Svelte seems to provide out of the box modifications to HTML that Flask doesn't, for example, `<button on:click={incrementCount}>` looks similar to jinja, except `on:click` seems to be a Svelte-specific handler which I guess is pre-compiled to a regular HTML `onclick` attribute, and I'm not even sure why `incrementCount` needs to be in `{}`, perhaps to enforce scoping or perhaps this is just Svelte's syntax.
3. Svelte requires compilation to raw JS before it can be deployed/ran, which is just an extra step over `flask run`.

#### Rather use

I have a good amount of experience with Flask, so in terms of getting going, Flask would certainly make my life easier. However, Svelte does seem to handle state super elegantly with its store system and overall looks very appealing, I would quite like to try it out. I would like to try to do at least one project with Svelte, but there's always the room to use both since Flask is primarily (in my eyes) a backend framework while Svelte is a frontend framework (or perhaps library? Not sure the correct terminology).