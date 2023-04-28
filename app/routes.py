from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import SignupForm, LoginForm, CreateDeckForm, CreateCardForm
from app.models import User, Card, Deck
# to log user in, function from login user. 
from flask_login import login_user, logout_user, current_user, login_required
 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        # Check to see if there is already a user with an email in the database.
        check_user = db.session.execute(db.select(User).filter((User.email == email))).scalars().all()
        if check_user:
            flash("A user with that email already exist", "warning")
            return redirect(url_for('signup'))
        new_user = User(email=email,  password=password)
        flash(f"Congrats, you signed up!", "success")
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        # user = db.session.execute(db.select(User).filter_by(email == email)).scalar_one()
        check_email = User.query.filter_by(email=email).first() 

        # If the user exists and has the correct password, log them in
        if check_email is not None and check_email.check_password(password):
            #Logs in user with that email and saves the id number.   
            login_user(check_email)
            flash(f'You have successfully logged in!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username and/or password. Please try again', 'danger')
            return redirect(url_for('login'))
            
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    # function from flask_login 
    logout_user()
    flash("You have logged out", "info")
    return redirect(url_for('index'))


#################################################################################################################################################################################################

@app.route('/decks')
@login_required
def decks():
    # decks will be a list of deck instances, 
    decks=Deck.query.all()
    # send back decks tot to the html
    return render_template('decks.html', decks=decks)


@app.route('/editdeckspage')
@login_required
def editdeckspage():
    # decks will be a list of deck instances, 
    decks=Deck.query.all()
    # send back decks tot to the html
    return render_template('editdeckspage.html', decks=decks)


@app.route('/createdeck', methods=['GET', 'POST'] )
#From flask_login, makes sure user is logged in before allowing them to access this route.
@login_required
def createdeck():
    form=CreateDeckForm()
    # from flask form, checks to see if if form has been validated and data entered is valid. 
    # if it has then it takes the data from the form, stores it in a variable and creates a new instance of Deck with that Data. 
    # When the new instance is created, it gets saved in the data base by db.session.commit in models file. 
    if form.validate_on_submit():
        deck_name = form.deck_name.data
        # Fom flask_login, current user is instance of User. 
        # Create an instance of Address with form data AND auth user ID. Get id form current user instance 
        new_deck = Deck(deck_name=deck_name, user_id=current_user.id)
        flash(f'Success, a new deck called "{deck_name}" has been created!', 'success')
        return redirect(url_for('decks'))
    return render_template('createdeck.html', form=form)

@app.route('/edit/<deck_id>', methods=['GET', 'POST'])
#From flask_login, makes sure user is logged in before allowing them to access this route.
@login_required
def edit_deck(deck_id):
    form = CreateDeckForm()
    # if id isn't found 404 error is displayed
    deck_to_edit = Deck.query.get_or_404(deck_id)
    # from flask form, checks to see if if form has been validated and data entered is valid. (post request)
    # if it has then it takes the data from the form, stores is at new value in variable and stores it in data base(edits current instance of Deck).  

    # User has to be the "user" of this deck to edit, need to use so user cant access through url."
    if deck_to_edit.user != current_user:
         flash("You do not have permission", "danger")
         return redirect(url_for('index'))

    if form.validate_on_submit():
        deck_to_edit.deck_name = form.deck_name.data
        #Commits to database
        db.session.commit()
        flash(f'Success,  {deck_to_edit.deck_name} has been edited!', 'success')
        return redirect(url_for('decks'))


    #fills out the form on the page so you already know whats there, repopulates, will update date already inside.  
    form.deck_name.data = deck_to_edit.deck_name
    return render_template('editdeckform.html', form=form, deck=deck_to_edit)

@app.route('/delete/<deck_id>')
#From flask_login, makes sure user is logged in before allowing them to access this route.
@login_required
def delete_deck(deck_id):
    deck_to_delete = Deck.query.get_or_404(deck_id)
    # User has to be the "user" of this deck to delete, need to use so user cant access through url."
    if deck_to_delete.user != current_user:
         flash("You do not have permission", "danger")
         return redirect(url_for('index'))
    # Deletes from database and updates, similar to db.sessions.add in models. 
    db.session.delete(deck_to_delete)
    db.session.commit()
    flash(f"{deck_to_delete.deck_name} has been deleted", "success")
    return redirect(url_for('decks'))

################################################################################################################################################################################################

@app.route('/flashcards')
@login_required
def flashcards():
    # decks will be a list of deck instances, 
    cards=Card.query.all()
    # send back decks tot to the html
    return render_template('flashcards.html', cards=cards)

@app.route('/createcard',  methods=['GET', 'POST'])
@login_required
def createcards():
    form=CreateCardForm()
    # from flask form, checks to see if if form has been validated and data entered is valid. 
    # if it has then it takes the data from the form, stores it in a variable and creates a new instance of Deck with that Data. 
    # When the new instance is created, it gets saved in the data base by db.session.commit in models file. 
    if form.validate_on_submit():
        question = form.question.data
        answer = form.answer.data
        # Fom flask_login, current user is instance of User. 
        # Create an instance of Card  with form data AND auth user ID.
        new_card = Card(question=question, answer=answer  deck_id=????)   ⬅️⬅️⬅️⬅️⬅️⬅️⬅️⬅️⬅️⬅️⬅️⬅️⬅️⬅️⬅️⬅️
        flash(f'Success, a new card "{question}" has been created!', 'success')
        return redirect(url_for('flashcards'))
    return render_template('createcard.html', form=form)



@app.route('/cards')
@login_required
def cards():
    return render_template('cards.html',)


