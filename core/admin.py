from django.contrib import admin

from core.models import Profile, Ticket, TicketGeoLocation


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "phone_number",
        "bio",
    )


class TicketAdmin(admin.ModelAdmin):
    list_display = (
        'logger',
        'category',
        'priority',
        'status',
        'subject',
        'description',
        'start_date',
        'end_date',
        'update_date',
        'date_created',
    )


class TicketGeoLocationAdmin(admin.ModelAdmin):
    list_display = (
        'ticket',
        'latitude',
        'longitude'
    )


admin.site.register(Profile, UserProfileAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(TicketGeoLocation, TicketGeoLocationAdmin)
