# myapp/tests/test_views.py
import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client

@pytest.fixture
def client():
   return Client()

def test_index_view(client):
   url = reverse('index')
   response = client.get(url)  # Replace with your actual URL path
   assert response.status_code == 200
   assert 'myapp/index.html' in [t.name for t in response.templates]
   
def test_index_view(client):
    response = client.get(reverse('index'))
    assert response.status_code == 200
    assert b'Welcome to the Homepage' in response.content


def test_signup_view(client, django_user_model):
    # Create a user to simulate authentication
    user = django_user_model.objects.create_user(
        username='testuser',
        password='testpassword'
    )

    
        # Simulate a logged-in user
    client.force_login(user)


    # Make a request to the 'hello' view
    url = reverse('hello')
    response = client.get(url)


    # Assert the response status code is 200
    assert response.status_code == 200


    # Assert that the correct template is used
    assert 'myapp/hello.html' in [t.name for t in response.templates]


    # Assert that the 'username' variable is passed to the template
    assert 'user' in response.context
    assert response.context['user'].username == user.username
   
# def test_signup_view(client, django_user_model):
#     # Create a user to simulate authentication
#     user = django_user_model.objects.create_user(
#         username='testuser',
#         password='testpassword'
#     )

#     # Log in the user using a new client instance
#     client = Client()
#     client.login(username='testuser', password='testpassword')

#     # Test access to the signup page while authenticated
#     response = client.get(reverse('signup'))
#     assert response.status_code == 302  # 302 indicates a redirect for authenticated users


# def test_login_view(client, django_user_model):
#     # Create a user for testing
#     user = django_user_model.objects.create_user(
#         username='testuser',
#         password='testpassword'
#     )

#     # Test access to the login page while not authenticated
#     response = client.get(reverse('login'))
#     assert response.status_code == 200
#     assert b'Log In' in response.content

#     # Test login functionality
#     response = client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
#     assert response.status_code == 302  # 302 indicates a redirect after successful login
#     assert client.get(reverse('hello')).status_code == 200  # Check that we are redirected to 'hello'

# def test_logout_view(client):
#     response = client.get(reverse('logout'))
#     assert response.status_code == 302  # 302 indicates a redirect
#     assert response.url == reverse('login')  # Check that we are redirected to 'login'
   
