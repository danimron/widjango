import requests
from django.contrib.auth.models import User
from .models import UserProfile


class HimatifAuth:
    base_url = 'http://api.himatif.org'
    login_url = f'{base_url}/data/v1/user/login'
    profile_url = f'{base_url}/data/v1/anggota/search?type=npm&q='

    def get_user_profile(self, username):
        response = requests.get(self.profile_url + username)
        if response.status_code == 200:
            profile = response.json()['response'][0]
            return profile
        return None

    def api_login(self, username, password):
        params = {'username': username, 'password': password}
        response = requests.post(self.login_url, params)
        if response.status_code == 200:
            return response.json()
        return None

    def authenticate(self, request, username=None, password=None):
        user_data = self.api_login(username, password)
        if user_data:
            try:
                user = User.objects.get(username=username)
                api_profile = self.get_user_profile(username)
                UserProfile.objects.filter(user=user).update(
                    status=api_profile['status'],
                    foto=api_profile['url_foto']
                )
            except User.DoesNotExist:
                api_profile = self.get_user_profile(username)
                user = User(username=username, email=api_profile['email'])
                user.save()
                profile = UserProfile.objects.create(
                    user=user,
                    nama=api_profile['nama'],
                    npm=api_profile['npm'],
                    angkatan=api_profile['angkatan'],
                    status=api_profile['status'],
                    foto=api_profile['url_foto']
                )
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
