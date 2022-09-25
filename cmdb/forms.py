from django import forms

class RoomAddForm(forms.Form):
    room_name = forms.CharField(max_length=255)
