# book_store/middleware.py
from django.http import JsonResponse
from django.conf import settings
from rest_framework import status
import time
import logging
from django.utils.deprecation import MiddlewareMixin

class ActiveUserCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/api/'):
            user = getattr(request, 'user', None)
            if user and user.is_authenticated and getattr(user, 'is_deleted', False):
                return JsonResponse({'error': 'Your account has been deactivated.'}, status=status.HTTP_403_FORBIDDEN)
        
        response = self.get_response(request)
        return response
    

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request._start_time = time.time()

    def process_response(self, request, response):
        if request.path.startswith('/api/'):
            duration = time.time() - getattr(request, '_start_time', time.time())
            
            log_data = {
                'method': request.method,
                'path': request.path,
                'status': response.status_code,
                'duration_ms': round(duration * 1000, 2),
                'user': getattr(request.user, 'username', 'anonymous'),
                'ip': self.get_client_ip(request),
            }
            
            if duration > 0.5:
                logger.warning(f"🐌 Slow Request: {log_data}")
            else:
                logger.info(f"✅ API Request: {log_data}")
                
        return response
    
    @staticmethod
    def get_client_ip(request):
        x_forwarded = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded:
            return x_forwarded.split(',')[0]
        return request.META.get('REMOTE_ADDR', 'unknown')