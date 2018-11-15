from django import forms
from .models import Image,Profile,Comment

import json,re

class Ajax(forms.Form):
	args = []
	user = []

	def __init__(self, *args, **kwargs):

		self.args = args
		if len(args) > 1:
			self.user = args[1]
			if self.user.id == None:
				self.user = "NL"

	def error(self, message):
		return json.dumps({ "Status": "Error", "Message": message }, ensure_ascii=False)

	def success(self, message):
		return json.dumps({ "Status": "Success", "Message": message }, ensure_ascii=False)

	def items(self, json):
		return json

	def output(self):
		return self.validate()

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'photo_date','likes','comment','image_name']

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class NewCommentForm(forms.ModelForm):
    class Meta :
        model = Comment
        exclude = ['username','comment_photo']

class AjaxFollow(Ajax):
    def validate(self):
        try:
            self.follower = self.args[0]["user"]
        except Exception as e:
            return self.error("Malformed request, did not process.")
        
        if self.user == "NL":
            return self.error("Unauthorised request.")

        if self.user.username == self.follower:
            return self.erroe("Can't follow yourself")

        if not Follwers.objects.filter(user=self.follower,follower=self.user.username).exists():
            f = Follwers(user=self.follower, follower=self.user.username).save()
            following = True
        else:
            Followers.objects.filter(user=self.follower, follower=self.user.username).delete()
            follwing = False
        out = {"Following": following}
        return self.items(json.dumps(out))
        
