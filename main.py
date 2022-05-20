from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateTimeField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    # cafe = StringField('Cafe name', validators=[DataRequired()])
    # submit = SubmitField('Submit')
    cafe = StringField(label='Cafe Name', validators=[DataRequired('Field cannot be blank')])
    location = StringField(label='Location', validators=[DataRequired('Field cannot be blank'), URL('web address required')])
    open = StringField(label='Opening Time (e.g. 10AM)', validators=[DataRequired('Field cannot be blank')])
    close = StringField(label='Closing Time (e.g. 10PM)', validators=[DataRequired('Field cannot be blank')])
    coffee_rating = SelectField(label='Coffee Rating', choices=['✘', '☕', '☕☕', '☕☕☕', '☕☕☕☕'])
    wifi_rating = SelectField(label='Wifi Rating', choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪'])
    power_rating = SelectField(label='Power Rating', choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌'])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    # print true if form meets validation criteria
    if form.validate_on_submit():
        print("True")
        with open('cafe-data.csv', encoding='utf8', mode='a') as csv_file:
            # csv_file.write([form.cafe.data, form.location.data, form.open.data, form.close.data, form.coffee_rating.data, form.wifi_rating.data, form.power_rating.data])
            csv_file.write(f"{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open.data},"
                           f"{form.close.data},"
                           f"{form.coffee_rating.data},"
                           f"{form.wifi_rating.data},"
                           f"{form.power_rating.data}"
                           )
            csv_file.write("\n")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        number_of_rows = len(list_of_rows)
        print(number_of_rows)
    return render_template('cafes.html', cafes=list_of_rows, num_rows=number_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
