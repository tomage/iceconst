

from django.forms import widgets
from django.template.defaultfilters import safe

class HTMLWidget(widgets.Widget):
    def __init__(self, html, attrs=None, *args, **kwargs):
        self.html = html
        self.attrs = attrs or {}
        super(HTMLWidget, self).__init__(*args, **kwargs)
    def render(self, name, value, attrs=None):
        return safe(self.html)

class TextActionsWidget(HTMLWidget):
    def __init__(self, attrs=None, *args, **kwargs):
        self.attrs = attrs or {}
        html = """
<div id="text_actions_widget">
    <ul>
        <li>
            <a id="js_generate_submodels" href="#">Generate submodels from original text</a>
        </li>
        <li>
            <a id="js_generate_translations" href="#">Generate google translations for this text (NOT IMPLEMENTED YET)</a>
        </li>
    </ul>
</div>
         """
        super(TextActionsWidget, self).__init__(html, *args, **kwargs)


