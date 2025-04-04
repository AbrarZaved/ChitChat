from django.contrib import admin

from chat_app.models import ChatRoom, Message

# Register your models here.
@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'content', 'timestamp')
    list_filter = ('room', 'timestamp')
    search_fields = ('user__username', 'content')
    date_hierarchy = 'timestamp'