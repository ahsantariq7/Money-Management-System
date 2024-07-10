from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import (
    UserProfile,
    Account,
    Category,
    ExpensePurpose,
    Transaction,
    Budget,
    Reminder,
    FinancialGoal,
    OtherAccount,
    Loan,
    LoanGiven,
    Enjoyment,
    EmailPassword,
)


# Base view class for dynamically creating views for each model
class BaseListView(ListView):
    template_name_suffix = "_list"
    context_object_name_suffix = "s"


class BaseCreateView(CreateView):
    template_name_suffix = "_form"
    success_url_suffix = "_list"

    def get_success_url(self):
        return reverse_lazy(self.success_url_suffix)


class BaseUpdateView(UpdateView):
    template_name_suffix = "_form"
    success_url_suffix = "_list"

    def get_success_url(self):
        return reverse_lazy(self.success_url_suffix)


class BaseDeleteView(DeleteView):
    template_name_suffix = "_confirm_delete"
    success_url_suffix = "_list"

    def get_success_url(self):
        return reverse_lazy(self.success_url_suffix)


# Dynamically create views for each model
for model in [
    UserProfile,
    Account,
    Category,
    ExpensePurpose,
    Transaction,
    Budget,
    Reminder,
    FinancialGoal,
    OtherAccount,
    Loan,
    LoanGiven,
    Enjoyment,
    EmailPassword,
]:
    # Create ListView
    list_view_name = model.__name__ + "ListView"
    list_view = type(list_view_name, (BaseListView,), {"model": model})
    globals()[list_view_name] = list_view

    # Create CreateView
    create_view_name = model.__name__ + "CreateView"
    create_view = type(
        create_view_name,
        (BaseCreateView,),
        {
            "model": model,
            "fields": "__all__",
            "success_url_suffix": model.__name__.lower() + "_list",
        },
    )
    globals()[create_view_name] = create_view

    # Create UpdateView
    update_view_name = model.__name__ + "UpdateView"
    update_view = type(
        update_view_name,
        (BaseUpdateView,),
        {
            "model": model,
            "fields": "__all__",
            "success_url_suffix": model.__name__.lower() + "_list",
        },
    )
    globals()[update_view_name] = update_view

    # Create DeleteView
    delete_view_name = model.__name__ + "DeleteView"
    delete_view = type(
        delete_view_name,
        (BaseDeleteView,),
        {"model": model, "success_url_suffix": model.__name__.lower() + "_list"},
    )
    globals()[delete_view_name] = delete_view


class AccountListView(TemplateView):
    template_name = "templates/handle/accounts/account_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["accounts"] = Account.objects.all()
        return context


class UserProfileListView(TemplateView):
    template_name = "templates/handle/userprofile_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["userprofiles"] = UserProfile.objects.all()
        return context


class HomeView(TemplateView):
    template_name = "templates/handle/home.html"
