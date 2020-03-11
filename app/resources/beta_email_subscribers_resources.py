from flask_restful import Resource, request
from app import db
from app.models.BetaEmailSubscriber import BetaEmailSubscriber
from flask_restful.reqparse import RequestParser
import re

# from flask_restplus import inputs


# from flask_restplus import inputs

beta_subscriber_request_parser = RequestParser(bundle_errors=True)
beta_subscriber_request_parser.add_argument("first_name", type=str, required=True,
                                            help="First Name has to be a valid string")
beta_subscriber_request_parser.add_argument("last_name", type=str, required=True,
                                            help="Last Name has to be a valid string")
# Issue with Werkzeug: https://github.com/noirbizarre/flask-restplus/issues/777
# beta_subscriber_request_parser.add_argument("email", type=inputs.email(dns=True), required=True,
#                                             help="Email has to be a valid email address")
beta_subscriber_request_parser.add_argument("email", type=str, required=True,
                                            help="Email has to be a valid email address")


class BetaEmailSignUp(Resource):
    def post(self):
        args = beta_subscriber_request_parser.parse_args()

        # manually validate email until issue above is resolve
        email = args.get('email')
        # Taken from : https://stackoverflow.com/questions/201323/how-to-validate-an-email-address-using-a-regular-expression
        email_regex_pattern = "(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        if not re.match(email_regex_pattern, email):
            return {'email': "Not a valid email address"}

        beta_email_subscriber = BetaEmailSubscriber.from_json(args)
        try:
            db.session.add(beta_email_subscriber)
            db.session.commit()
            return {'new_user': args}
        except Exception as e:
            print(e)
            return {'error', e}
