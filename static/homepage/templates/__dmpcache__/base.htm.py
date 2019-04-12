# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555073693.8705761
_enable_loop = True
_template_filename = '/home/eric/Documents/bchain/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n    <meta charset="UTF-8">\n    <head>\n\n        <title>Crop Chain</title>\n\n')
        __M_writer('        <script src="http://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\n      \t<link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/assets/css/main.css" />\n        <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/assets/css/font-awesome.min.css" />\n        <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/assets/css/noscript.css" />\n        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">\n        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">\n\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('/homepage/media/assets/js/breakpoints.min.js"></script>\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('/homepage/media/assets/js/browser.min.js"></script>\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('/homepage/media/assets/js/jquery.min.js"></script>\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('/homepage/media/assets/js/jquery.scrollex.min.js"></script>\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('/homepage/media/assets/js/jquery.scrolly.min.js"></script>\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('/homepage/media/assets/js/main.js"></script>\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('/homepage/media/assets/js/util.js"></script>\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\n        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\n        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>\n\n    </head>\n    <body>\n        <main>\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n        </main>\n\n        <footer id="footer">\n  \t\t\t\t\t\t<ul class="copyright">\n  \t\t\t\t\t\t\t<li>&copy; Untitled</li><li>Design: <a href="http://html5up.net">HTML5 UP</a></li>\n  \t\t\t\t\t\t</ul>\n              <div id="google_translate_element"></div>\n\n            <script type="text/javascript">\n                function googleTranslateElementInit() {\n                    new google.translate.TranslateElement({ pageLanguage: \'en\', layout: google.translate.TranslateElement.InlineLayout.SIMPLE }, \'google_translate_element\');\n                }\n            </script>\n            <script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>\n        </footer>\n\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n                Site content goes here in sub-templates.\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/eric/Documents/bchain/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"18": 0, "27": 2, "28": 10, "29": 11, "30": 11, "31": 12, "32": 12, "33": 13, "34": 13, "35": 18, "36": 19, "37": 19, "38": 20, "39": 20, "40": 21, "41": 21, "42": 22, "43": 22, "44": 23, "45": 23, "46": 24, "47": 24, "48": 25, "49": 25, "50": 26, "51": 26, "56": 35, "62": 33, "68": 33, "74": 68}}
__M_END_METADATA
"""
