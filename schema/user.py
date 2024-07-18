from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    full_name = fields.String(validate=[validate.Length(min=2, max=100)])
    email = fields.String(required=True, validate=[validate.Length(max=100), validate.Email()])
    password = fields.String(load_only=True, required=True)
