from marshmallow import Schema, fields, post_load
from markupsafe import escape
from app.models.usuario import Usuario


class UsuarioMapping(Schema):
  id = fields.Integer()
  nombredeusuario = fields.String()
  password = fields.String()
  actividad = fields.Boolean()

  @post_load
  def make_usuario(self, data, **kwargs):
    for key in ['nombredeusuario', 'password'] :
      if key in data:
        data[key] = escape(data[key])
    return Usuario(**data)