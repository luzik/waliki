from docutils import nodes
from docutils.parsers.rst import Directive, directives

try:
    import micawber
except ImportError:
    micawber = None  # NOQA


class Media(Directive):
    """ Restructured text extension for inserting any
        sort of media using micawber."""
    has_content = False
    required_arguments = 1
    optional_arguments = 999

    def run(self):
        if micawber is None:
            msg = "To use the media directive, install micawber first."
            return [nodes.raw('', '<div class="text-error">{0}</div>'.format(msg), format='html')]

        url = " ".join(self.arguments)
        providers = micawber.bootstrap_basic()
        data = providers.request(url)
        html = micawber.parse_text(url, providers)
        return [nodes.raw('', html, format='html')]


def register_directive():
    directives.register_directive('media', Media)
