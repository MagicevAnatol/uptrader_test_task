from django import template
from ..models import MenuItem
from django.db.models import Prefetch

register = template.Library()


@register.inclusion_tag('menu/menu_template.html', takes_context=True)
def draw_menu(context, menu_name):
    try:
        menu_items = MenuItem.objects.prefetch_related(
            Prefetch('children', queryset=MenuItem.objects.all())
        ).filter(menu__name=menu_name)

        current_url = context['request'].path

        active_item = None
        for item in menu_items:
            if item.get_url() == current_url:
                active_item = item
                break

        def build_tree(items, parent=None):
            """Рекурсивное построение дерева меню"""
            tree = []
            for item in items:
                if item.parent == parent:
                    children = build_tree(items, parent=item)
                    tree.append({
                        'item': item,
                        'children': children,
                        'is_active': item == active_item or any(child['is_active'] for child in children)
                    })
            return tree

        menu_tree = build_tree(menu_items)
        return {'menu_tree': menu_tree}

    except MenuItem.DoesNotExist:
        return {'menu_tree': []}
