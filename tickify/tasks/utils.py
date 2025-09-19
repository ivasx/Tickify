menu = [{'title': 'Home', 'url': 'home'},
        {'title': 'Tasks', 'url': 'tasks_list'},
        {'title': 'Add Task', 'url': 'add_task'},
        {'title': 'Contact', 'url': 'contact'},
        {'title': 'Login', 'url': 'login'},
        {'title': 'Register', 'url': 'register'}
        ]


class DataMixin:
    title_page = None
    extra_context = {}

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page

        if 'menu' not in self.extra_context:
            self.extra_context['menu'] = menu


    def get_mixin_context(self, context, **kwargs):
        context['menu'] = menu
        context.update(kwargs)
        return context