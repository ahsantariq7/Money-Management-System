from django.urls import path
from .views import (
    UserProfileListView,
    UserProfileCreateView,
    UserProfileUpdateView,
    UserProfileDeleteView,
    AccountListView,
    AccountCreateView,
    AccountUpdateView,
    AccountDeleteView,
    CategoryListView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
    ExpensePurposeListView,
    ExpensePurposeCreateView,
    ExpensePurposeUpdateView,
    ExpensePurposeDeleteView,
    TransactionListView,
    TransactionCreateView,
    TransactionUpdateView,
    TransactionDeleteView,
    BudgetListView,
    BudgetCreateView,
    BudgetUpdateView,
    BudgetDeleteView,
    ReminderListView,
    ReminderCreateView,
    ReminderUpdateView,
    ReminderDeleteView,
    FinancialGoalListView,
    FinancialGoalCreateView,
    FinancialGoalUpdateView,
    FinancialGoalDeleteView,
    OtherAccountListView,
    OtherAccountCreateView,
    OtherAccountUpdateView,
    OtherAccountDeleteView,
    LoanListView,
    LoanCreateView,
    LoanUpdateView,
    LoanDeleteView,
    LoanGivenListView,
    LoanGivenCreateView,
    LoanGivenUpdateView,
    LoanGivenDeleteView,
    EnjoymentListView,
    EnjoymentCreateView,
    EnjoymentUpdateView,
    EnjoymentDeleteView,
    EmailPasswordListView,
    EmailPasswordCreateView,
    EmailPasswordUpdateView,
    EmailPasswordDeleteView,
    HomeView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    # URLs for UserProfile
    path("userprofiles/", UserProfileListView.as_view(), name="userprofile_list"),
    path(
        "userprofiles/create/",
        UserProfileCreateView.as_view(),
        name="userprofile_create",
    ),
    path(
        "userprofiles/<int:pk>/update/",
        UserProfileUpdateView.as_view(),
        name="userprofile_update",
    ),
    path(
        "userprofiles/<int:pk>/delete/",
        UserProfileDeleteView.as_view(),
        name="userprofile_delete",
    ),
    # URLs for Account
    path("accounts/", AccountListView.as_view(), name="account_list"),
    path("accounts/create/", AccountCreateView.as_view(), name="account_create"),
    path(
        "accounts/<int:pk>/update/", AccountUpdateView.as_view(), name="account_update"
    ),
    path(
        "accounts/<int:pk>/delete/", AccountDeleteView.as_view(), name="account_delete"
    ),
    # URLs for Category
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path("categories/create/", CategoryCreateView.as_view(), name="category_create"),
    path(
        "categories/<int:pk>/update/",
        CategoryUpdateView.as_view(),
        name="category_update",
    ),
    path(
        "categories/<int:pk>/delete/",
        CategoryDeleteView.as_view(),
        name="category_delete",
    ),
    # URLs for ExpensePurpose
    path(
        "expensepurposes/", ExpensePurposeListView.as_view(), name="expensepurpose_list"
    ),
    path(
        "expensepurposes/create/",
        ExpensePurposeCreateView.as_view(),
        name="expensepurpose_create",
    ),
    path(
        "expensepurposes/<int:pk>/update/",
        ExpensePurposeUpdateView.as_view(),
        name="expensepurpose_update",
    ),
    path(
        "expensepurposes/<int:pk>/delete/",
        ExpensePurposeDeleteView.as_view(),
        name="expensepurpose_delete",
    ),
    # URLs for Transaction
    path("transactions/", TransactionListView.as_view(), name="transaction_list"),
    path(
        "transactions/create/",
        TransactionCreateView.as_view(),
        name="transaction_create",
    ),
    path(
        "transactions/<int:pk>/update/",
        TransactionUpdateView.as_view(),
        name="transaction_update",
    ),
    path(
        "transactions/<int:pk>/delete/",
        TransactionDeleteView.as_view(),
        name="transaction_delete",
    ),
    # URLs for Budget
    path("budgets/", BudgetListView.as_view(), name="budget_list"),
    path("budgets/create/", BudgetCreateView.as_view(), name="budget_create"),
    path("budgets/<int:pk>/update/", BudgetUpdateView.as_view(), name="budget_update"),
    path("budgets/<int:pk>/delete/", BudgetDeleteView.as_view(), name="budget_delete"),
    # URLs for Reminder
    path("reminders/", ReminderListView.as_view(), name="reminder_list"),
    path("reminders/create/", ReminderCreateView.as_view(), name="reminder_create"),
    path(
        "reminders/<int:pk>/update/",
        ReminderUpdateView.as_view(),
        name="reminder_update",
    ),
    path(
        "reminders/<int:pk>/delete/",
        ReminderDeleteView.as_view(),
        name="reminder_delete",
    ),
    # URLs for FinancialGoal
    path("financialgoals/", FinancialGoalListView.as_view(), name="financialgoal_list"),
    path(
        "financialgoals/create/",
        FinancialGoalCreateView.as_view(),
        name="financialgoal_create",
    ),
    path(
        "financialgoals/<int:pk>/update/",
        FinancialGoalUpdateView.as_view(),
        name="financialgoal_update",
    ),
    path(
        "financialgoals/<int:pk>/delete/",
        FinancialGoalDeleteView.as_view(),
        name="financialgoal_delete",
    ),
    # URLs for OtherAccount
    path("otheraccounts/", OtherAccountListView.as_view(), name="otheraccount_list"),
    path(
        "otheraccounts/create/",
        OtherAccountCreateView.as_view(),
        name="otheraccount_create",
    ),
    path(
        "otheraccounts/<int:pk>/update/",
        OtherAccountUpdateView.as_view(),
        name="otheraccount_update",
    ),
    path(
        "otheraccounts/<int:pk>/delete/",
        OtherAccountDeleteView.as_view(),
        name="otheraccount_delete",
    ),
    # URLs for Loan
    path("loans/", LoanListView.as_view(), name="loan_list"),
    path("loans/create/", LoanCreateView.as_view(), name="loan_create"),
    path("loans/<int:pk>/update/", LoanUpdateView.as_view(), name="loan_update"),
    path("loans/<int:pk>/delete/", LoanDeleteView.as_view(), name="loan_delete"),
    # URLs for LoanGiven
    path("loangivens/", LoanGivenListView.as_view(), name="loangiven_list"),
    path("loangivens/create/", LoanGivenCreateView.as_view(), name="loangiven_create"),
    path(
        "loangivens/<int:pk>/update/",
        LoanGivenUpdateView.as_view(),
        name="loangiven_update",
    ),
    path(
        "loangivens/<int:pk>/delete/",
        LoanGivenDeleteView.as_view(),
        name="loangiven_delete",
    ),
    # URLs for Enjoyment
    path("enjoyments/", EnjoymentListView.as_view(), name="enjoyment_list"),
    path("enjoyments/create/", EnjoymentCreateView.as_view(), name="enjoyment_create"),
    path(
        "enjoyments/<int:pk>/update/",
        EnjoymentUpdateView.as_view(),
        name="enjoyment_update",
    ),
    path(
        "enjoyments/<int:pk>/delete/",
        EnjoymentDeleteView.as_view(),
        name="enjoyment_delete",
    ),
    # URLs for EmailPassword
    path("emailpasswords/", EmailPasswordListView.as_view(), name="emailpassword_list"),
    path(
        "emailpasswords/create/",
        EmailPasswordCreateView.as_view(),
        name="emailpassword_create",
    ),
    path(
        "emailpasswords/<int:pk>/update/",
        EmailPasswordUpdateView.as_view(),
        name="emailpassword_update",
    ),
    path(
        "emailpasswords/<int:pk>/delete/",
        EmailPasswordDeleteView.as_view(),
        name="emailpassword_delete",
    ),
]
