from django.contrib.sessions.models import Session

class OneSessionPerUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        #One-time configuration and initialization.

    def __call__(self, request):
        #Code to be executed for each request before
        # the view (and later middleware) are called.
        
        if request.user.is_authenticated:
            stored_session_key = request.user.logged_in_user.session_key

            if stored_session_key and stored_session_key != request.session.session_key:
                Session.objects.get(session_key = stored_session_key).delete()
                
            request.user.logged_in_user.session_key = request.session.session_key
            request.user.logged_in_user.save()

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the wiew is called.

        return response