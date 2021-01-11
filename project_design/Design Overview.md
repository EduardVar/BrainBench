# R1 - `/login`
## Template: `login.html`
* Have an `input#email` element
* Have an `input#password` element
* Have an `input#btn-submit` element
## Frontend.py
* `login_get()`
    * Returns the `login.html` template
* `login_post()`
    * Redirects the user to the home page with a 303 status code
    * Or redirects the user back to the `/login` page
## Backend.py
* `login_user(email, password)`
    *Uses `get_user(email)` to return a user object
* `check_password_hash(user.password, password)`
    * Uses user object's password and compares it to the password for that user the database
---
# R2 - `/register`
## Template: `register.html`
* Have an `input#email` element
* Have an `input#username` element
* Have an `input#password` element
* Have an `input#password2` element
## Frontend.py
* In `/register`, before filling out the form, runs `register_get()`
    * Return `render_template('register.html', message='')`
        * Displays the `register.html` template with no message (initially)
* In `/register`, after form, runs `register_post()`
    * Attempt to register the user using `backend.register_user(email, name, password, password2)`
    * If `backend.register_user` returns an error then return `render_template('register.html', message=error_message)`
      * `error_message` will be displayed when the template is re-rendered in the `{message}` field
    * Else, redirects to `/login` page
## Backend.py:
* `register_user(email, name, password, password2)`
    * Searches the database by `email` to see if this email is in use
    * Validates that password and `password2` match and both fulfill password requirements
    * Validate that the given email is valid
    * If any of these validations fail, return an appropriate error message else return `None`.
* `check_password_match(password, password2)`
    * Check that `password` and `password2` match exactly
    * Inform `redirect_user()` if passwords do not match
* `check_username_valid(username)`
    * Check that the name input is up to protocol set by the specification:
      * non-empty, alphanumeric-only, space allowed only if it not the first/last character, longer than 2 character and less than 20 characters
    * Inform `redirect_user()` if username is invalid
* `check_password_valid(password)` -> also used in R1
    * Check that the password input is up to the protocol set by the specification
      * Password has required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character
---
# R3 - /
## Template: index.html
  * Have a `button#logout` element
  * Have a `header#welcome` element
  * Have a `div#balance` element
  * Have a `table#tickets` element displaying all available tickets
  * Have a `button.buy_ticket` for each ticket in the table
    * When clicked the button should display the following
      * A `form#buy_ticket_form` element for purchasing new forms
      * A `input#buy_ticket_name`element
      * A `input#buy_ticket_quantity` element
      * A `button#submit_buy_ticket` element
        * The above information should be submitted to `/buy` as a `POST` request
  * Have a `button#submit_new_tickets` element
    * When clicked the button should display the following
      * A `form#submit_new_tickets` element
      * A `input#submit_name` element
      * A `input#submit_quantity` field
      * A `input#submit_price` field
      * A `input#submit_expiration_date` element
      * A `button#submit_new_ticket` element
        * The above info should be submitted to `/sell` as a `POST` request when the button is clicked
  * Have a `button#udpate_tickets` element
    * When clicked the button should display
      * A table displaying all the tickets that the user has uploaded
      * Each row should have a button then when clicked should display
        * A `form#update_ticket element`
        * A `input#update_name element`
        * A `input#update_quantity element`
        * A `input#update_price element`
        * A `input#update_expiration element`
        * A `button#submit_update element`
          * The above information should be sent to `/update` as a POST request when the button is clicked.
## Frontend.py:
  * If not logged in, redirects back to `/login` R1
  * Get all tickets via `backend.get_available_tickets()`
  * If logged in, return `render_template('index.html', user=user, tickets=tickets)`
    * Displays the `index.html` template with the user information
## Backend.py:
  * `get_available_tickets()`
    * Shows the forms of the available tickets
      * Information shown includes quantity of each ticket, owner's email
    * Call a method to check if the date for tickets has passed
      * If not, show price.
---
# R7 - `/logout`
## Template: `login.html`
## Frontend.py:
  * `logout()`
    * Removes `'logged_in'` from session
    * Redirects user to the `/login page`
---
# R8 - `/*`
## Template: `404.html`
  * Have a `h1#404-message`
  * Have a `h3#funny`
    * "Seat's taken"
    * "You just lost musical chairs"
    * "Sorry, we're full"
    * "You don't have a ticket for this seat"
    * "Hey, that's my seat!"
    * "No loitering, get outta here"
    * "Please remain seated during takeoff and landing"
    * "You can't sit with us."
## Frontend.py:
  * `page_not_found()`
    * Decorated with `@app.errorhandler(404)`
    * Serves the `404.html` page, with `404` status code