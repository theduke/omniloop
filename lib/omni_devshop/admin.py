from django.contrib import admin

from .models import Website, WebsiteEnvironment

class WebsiteEnvInline(admin.StackedInline):
    model = WebsiteEnvironment


class WebsiteAdmin(admin.ModelAdmin):
    inlines = [WebsiteEnvInline]
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Website, WebsiteAdmin)


#class WebsiteEnvAdmin(admin.ModelAdmin):
    #pass
#admin.site.register(WebsiteEnvironment, WebsiteEnvAdmin)
