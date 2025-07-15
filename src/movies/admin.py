from django.contrib import admin

# Register your models here.

from .models import Movie

class MovieAdmin(admin.ModelAdmin):

    list_display = ['__str__', 'calculate_ratings_count']
    readonly_fields = ['calculate_ratings_count','calculate_ratings_avg','rating_avg_display']


admin.site.register(Movie, MovieAdmin)
