from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView, TemplateView
from django.utils.decorators import method_decorator
from django.contrib import messages

from services.models import Services
from .forms import ContactForm, LoginForm, UserRegisterForm
from .models import Contact



# Función que verifica si el usuario NO está autenticado
def not_logged_in(user):
    return not user.is_authenticated


class HomeView(ListView):
    template_name = "core/home.html"
    context_object_name = 'services'  # Nombre de la variable en el template
    queryset = Services.objects.filter(show_home=True)  # Filtro para mostrar solo los servicios relevantes

    # Si quieres ordenar o modificar el queryset, puedes sobrescribir el método get_queryset
    def get_queryset(self):
        return Services.objects.filter(show_home=True)

class AboutUsView(TemplateView):
    template_name = "core/about_us.html"

class LoginView(FormView):
    template_name = "core/login.html"
    form_class = LoginForm
    success_url = reverse_lazy('core:home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)  # Redirige a la `success_url`
        else:
            # Usuario no válido
            context = self.get_context_data(form=form, error=True, error_message='Usuario no válido')
            return self.render_to_response(context)

    def form_invalid(self, form):
        # Enviar el formulario con errores
        context = self.get_context_data(form=form, error=True)
        return self.render_to_response(context)

def logout_view(request):
    logout(request)
    return redirect(reverse('core:home'))

@method_decorator(user_passes_test(not_logged_in, login_url='/'), name='dispatch')
class RegisterView(FormView):
    template_name = "core/register.html"
    form_class = UserRegisterForm
    success_url = "/"  # Redirige a la página principal tras el registro exitoso

    def form_valid(self, form):
        username = form.cleaned_data['username']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        password2 = form.cleaned_data['password2']

        # Verificar si el nombre de usuario ya existe
        if User.objects.filter(username=username).exists():
            messages.error(self.request, 'El nombre de usuario ya está en uso. Por favor, elige otro.')
            return self.form_invalid(form)

        # Crear el usuario
        user = User.objects.create_user(username, email, password2)
        if user:
            user.first_name = first_name
            user.last_name = last_name
            user.save()

        # Mensaje de éxito
        messages.success(self.request, 'Usuario creado correctamente.')
        return super().form_valid(form)  # Redirige al success_url

    def form_invalid(self, form):
        # Mensaje de error
        messages.error(self.request, 'Problemas al crear el usuario, inténtelo de nuevo.')
        return self.render_to_response(self.get_context_data(form=form))
        
class ContactView(FormView):
    template_name = "core/contact.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        email = form.cleaned_data['email']
        comentario = form.cleaned_data['comentario']

        message_content = f'{nombre} con email {email} ha escrito lo siguiente: {comentario}'
        automatic_message = 'Tenemos su solicitud registrada, le responderemos lo antes posible, Muchas gracias.'
        messages.info(self.request, 'Correo enviado con satisfacción')

        Contact.objects.create(
            nombre=nombre,
            email=email,
            comentario=comentario
        )

        success = [(send_mail(
            "Formulario de contacto de mi Web",
            message_content,
            "carlos.ahoravasylocascas@gmail.com",
            ["carlos.beltra.lopez@gmail.com"],
            fail_silently=False,
        )), (
            send_mail(
            "Formulario de contacto de mi Web",
            automatic_message,
            "carlos.ahoravasylocascas@gmail.com",
            [email],
            fail_silently=False,
        ))]

        return super().form_valid(form)