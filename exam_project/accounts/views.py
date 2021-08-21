from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, UpdateView

from accounts.forms import ProfileForm
from accounts.models import Profile


class UserDetailView(DetailView):
    model = get_user_model()
    template_name = 'profile.html'
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        page_owner = self.get_object()
        if self.request.user != page_owner:
            context['adverts'] = page_owner.advert.filter(is_moderated=True)
            return context
        context['adverts'] = page_owner.advert.all()
        return context


class PhoneNumberUpdateView(PermissionRequiredMixin, UpdateView):
    model = Profile
    template_name = 'registration/update_profile.html'
    form_class = ProfileForm
    context_object_name = 'profile'
    permission_required = 'account.change_profile'

    def has_permission(self):
        return self.get_object().user == self.request.user

    def get_success_url(self):
        return reverse('accounts:profile', kwargs={'pk': self.kwargs.get('pk')})

# Create your views here.