
import ssl
from django.core.mail.backends.smtp import EmailBackend as SMTPBackend

class EmailBackend(SMTPBackend):
    def _get_ssl_context(self):
        if self.ssl_context is None:
            self.ssl_context = ssl.create_default_context()
            self.ssl_context.check_hostname = False
            self.ssl_context.verify_mode = ssl.CERT_NONE
        return self.ssl_context
    
    def open(self):
        if self.connection:
            return False
            
        try:
            # Create unverified context
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            
            self.ssl_context = context 
            
            # Call super open which uses self.ssl_context
            return super().open()
        except Exception:
            if not self.fail_silently:
                raise
