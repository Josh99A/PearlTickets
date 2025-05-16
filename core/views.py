from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from core.models import User


def index(request):
    """
    Render the index page.
    """
    return render(request, 'core/index.html')


def signup_view(request):
    """
    Handle user signup.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        is_passenger = request.POST.get('is_passenger', False)
        is_bus_admin = request.POST.get('is_bus_admin', False)

        # Create a new user
        user = User.objects.create_user(username=username, password=password, email=email, phone_number=phone_number,
                                        is_passenger=is_passenger, is_bus_admin=is_bus_admin)
        messages.success(request, 'Signup successful. You can now log in.')
        return redirect('login')  # Redirect to login page after signup

    return render(request, 'core/sign_up.html')

@login_required
def user_dashboard(request):
    """
    Render the user dashboard.
    """
    return render(request, 'core/user_dashboard.html')


def browse_routes(request):
    """
    Render the browse routers page.
    """
    return render(request, 'core/browse_page.html')



@login_required
def operator_dashboard(request):
    """
    Render the bus operator dashboard.
    """
    return render(request, 'core/operator_dashboard.html')



#A view to login a user 
def login_view(request):
    """
    Handle user login.
    """
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            if  request.user.is_staff:
                return redirect('operator-dashboard')
            else:
                return redirect('user-dashboard')  # Redirect to user   pdashboard after login
        else:
            messages.error(request, 'Invalid username or password.')
            print("Invalid username or password.")
    return render(request, 'core/login.html')



# A view to logout a user
@login_required
def logout_view(request):
    """
    Handle user logout.
    """
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('index')


# A view that allows bus operators to view their trips
# @login_required 
# def view_trips(request):
#     """
#     View trips for bus operators.
#     """
#     # Assuming you have a Trip model and a way to filter trips for the logged-in user
#     # trips = Trip.objects.filter(bus__company__user=request.user)
#     return render(request, 'core/view_trips.html', {'trips': trips})