from django import forms
from .models import Customer

class DateInput(forms.DateInput):
  input_type = "date"

class CustomerForm(forms.ModelForm):
  first_name = forms.CharField(
    label="Nome",
    error_message={"max_length": "Nome não pode ter mais de 30 caracteres"}
  )
  last-Name = forms.CharField(
    label="Sobrenome",
    error_message={"max_length": "Nome não pode ter mais de 30 caracteres"}
  )
  email = forms.EmailField(label="E-mail")
  bisth_date = forms.DateField(label="Data de Nascimento", widget=DateInput())
  area_code = forms.RegexField(
    label="DDD",
    regex="^\+?1?[0-9]{2}$",
    error_message={"invalid": "Número de DDD inválido"}
  )
  phone_number = forms.RegexField(
    label="Telefone",
    regex="^\+?1?[0-9]{9,15}$",
    error_message={"invalid": "Número de telefone inválido"}
  )
  country = forms.CharField(label="País"),
  state = forms.CharField(label="Estado"),
  cep_code = RegexField(
    label="CEP",
    regex="^\+?1?[0-9]{8}$",
    error_message={"invalid": "Número de CEP inválido"}
  )
  city = forms.CharField(label="Cidade")
  address = models.CharField(label="Endereço")
  address_number = models.RegexField(
    label="Número",
    regex="^\+?1?[0-9]{9,15}$",
    error_message={"invalid": "Número inválido"}
  )

  class Meta:
    model = Customer
    fields = (
      "first_name",
      "last_name",
      "email",
      "birth_date",
      "area_code",
      "phone_number",
      "country",
      "state",
      "cep_code",
      "city",
      "address",
      "address_number",
    )
