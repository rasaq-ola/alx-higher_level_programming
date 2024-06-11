# JavaScript Web JQuery

This project contains JavaScript scripts to manipulate DOM elements and fetch data using JQuery. Each task is a separate JavaScript file that performs specific actions on a provided HTML file.

## Tasks

### 0. No JQuery
Write a script that updates the text color of the `<header>` element to red (`#FF0000`) without using JQuery.

### 1. With JQuery
Write a script that updates the text color of the `<header>` element to red (`#FF0000`) using JQuery.

### 2. Click and turn red
Write a script that updates the text color of the `<header>` element to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`.

### 3. Add `.red` class
Write a script that adds the class `red` to the `<header>` element when the user clicks on the tag `DIV#red_header`.

### 4. Toggle classes
Write a script that toggles the class of the `<header>` element when the user clicks on the tag `DIV#toggle_header`. The `<header>` element must always have one class: `red` or `green`.

### 5. List of elements
Write a script that adds a `<li>` element to a list when the user clicks on the tag `DIV#add_item`.

### 6. Change the text
Write a script that updates the text of the `<header>` element to `New Header!!!` when the user clicks on `DIV#update_header`.

### 7. Star wars character
Write a script that fetches the character name from the URL `https://swapi-api.alx-tools.com/api/people/5/?format=json` and displays it in the HTML tag `DIV#character`.

### 8. Star Wars movies
Write a script that fetches and lists the title for all movies by using the URL `https://swapi-api.alx-tools.com/api/films/?format=json`. All movie titles must be listed in the HTML tag `UL#list_movies`.

### 9. Say Hello!
Write a script that fetches from `https://hellosalut.stefanbohacek.dev/?lang=fr` and displays the value of `hello` from that fetch in the HTML tag `DIV#hello`.

## Usage
To test each script, open the corresponding HTML file in your browser.

## Requirements
- Allowed editors: vi, vim, emacs
- Files will be interpreted on Chrome (version 57.0)
- All files should end with a new line
- Code should be semistandard compliant with the flag `--global $: semistandard *.js --global $`
- Use JQuery version 3.x
- Do not use `var`
- HTML should not reload for each action: DOM manipulation, update values, fetch data
