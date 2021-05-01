from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash

from .forms import *
from .charts import *

seat = emptySeats(12, 4)
flight = initialSeats(seat)

#@app.route("/", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def user_options():
    
    form = UserOptionForm()
    if request.method == 'POST' and form.validate_on_submit():
        option = request.form['option']

        if option == "1":
            return redirect('/admin')
        else:
            return redirect("/reservations")
    
    return render_template("options.html", form=form, template="form-template")

@app.route("/admin", methods=['GET', 'POST'])
def admin():

    form = AdminLoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        #make sure the admin username and password are correct...
        username = request.form["username"]
        password = request.form["password"]


        for line in open("flask_wtforms_tutorial/passcodes.txt", "r").readlines():
            login = line.split(",")
            if username == login[0] and password == login[1].strip():
                err= None
                chart = print_flightChart(flight)
                return render_template("admin.html", form=form,template="form-template", err=err, chart = chart)
            else:
                err = "You've enterned the wrong information"
                chart = None
                return render_template("admin.html", form=form,template="form-template", err=err, chart = chart) 
                

    return render_template("admin.html", form=form, template="form-template")

@app.route("/reservations", methods=['GET', 'POST'])
def reservations():

    form = ReservationForm()

    return render_template("reservations.html", form=form, template="form-template")

