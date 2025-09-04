from django.contrib import admin, messages

from tasks.models import Task, Category

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'category', 'user', 'updated_at', 'brief_info')
    list_display_links = ('title',)
    list_editable = ('completed', 'category')
    list_per_page = 5
    actions = ['set_completed', 'set_active']

    @admin.display(description='Кількість символів')
    def brief_info(self, task: Task):
        return f'{len(task.description)} символів'

    @admin.action(description='Позначити виконаним')
    def set_completed(self, request, queryset):
        queryset.update(completed=True)
        self.message_user(request, f'{queryset.count()} задачі позначено як виконані')

    @admin.action(description='Позначити невиконаним')
    def set_active(self, request, queryset):
        queryset.update(completed=False)
        self.message_user(request, f'{queryset.count()} задачі позначено як невиконані', messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user')
    list_display_links = ('id', 'name')