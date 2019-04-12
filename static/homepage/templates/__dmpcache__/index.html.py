# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555073693.8630033
_enable_loop = True
_template_filename = '/home/eric/Documents/bchain/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def __M_anon_3():
            return render___M_anon_3(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], '__M_anon_3'):
            context['self'].__M_anon_3(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render___M_anon_3(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def __M_anon_3():
            return render___M_anon_3(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="content">\n        <a href="/producer/">Producer</a>\n        <a href="/manufacturer/">Manufacturer</a>\n        <a href="/distributor/">Distributor</a>\n        <a href="/retailer/">Retailer</a>\n        <a href="/shipper/">Shipper</a>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<!DOCTYPE HTML>\n<!--\n\tSpectral by HTML5 UP\n\thtml5up.net | @ajlkn\n\tFree for personal and commercial use under the CCA 3.0 license (html5up.net/license)\n-->\n<html>\n\t<body class="landing is-preload">\n\t\t<!-- Page Wrapper -->\n\t\t\t<div id="page-wrapper">\n\n\t\t\t\t<!-- Banner -->\n\t\t\t\t\t<section id="banner">\n\t\t\t\t\t\t<div class="inner">\n\t\t\t\t\t\t\t<h2 class="header">Crop Chain</h2>\n\t\t\t\t\t\t\t<!-- <p>Trackable, Organic meat and grains.<br />\n\t\t\t\t\t\t\tGuaranteed.</p> -->\n\t\t\t\t\t\t\t<ul class="actions special">\n\t\t\t\t\t\t\t\t<li><a href="/login" class="button medium primary">Login</a></li>\n\t\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t<a href="#one" class="more scrolly">Learn More</a>\n\t\t\t\t\t</section>\n\n\t\t\t\t<!-- One -->\n\t\t\t\t\t<section id="one" class="wrapper style1 special">\n\t\t\t\t\t\t<div class="inner">\n\t\t\t\t\t\t\t<header class="major">\n\t\t\t\t\t\t\t\t<h4>An unalterable solution to track your livestock and grains</h4>\n\t\t\t\t\t\t\t</header>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</section>\n\n\t\t\t\t<!-- Two -->\n\t\t\t\t\t<section id="two" class="wrapper alt style2">\n\t\t\t\t\t\t<section class="spotlight">\n\t\t\t\t\t\t\t<div class="image"><img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/images/grain.jpg" alt="" /></div><div class="content">\n\t\t\t\t\t\t\t\t<h2>Low Cost & Efficient</h2>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</section>\n\t\t\t\t\t\t<section class="spotlight">\n\t\t\t\t\t\t\t<div class="image"><img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/images/chickens.jpg" alt="" /></div><div class="content">\n\t\t\t\t\t\t\t\t<h2>Provides Validation</h2>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</section>\n\t\t\t\t\t\t<section class="spotlight">\n\t\t\t\t\t\t\t<div class="image"><img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/images/farmer.jpg" alt="" /></div><div class="content">\n\t\t\t\t\t\t\t\t<h2>Verify Certifications and Other Qualifications</h2>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</section>\n\t\t\t\t\t</section>\n\n\t\t\t\t<!-- Three -->\n\t\t\t\t\t<section id="one" class="wrapper style1 special">\n\t\t\t\t\t\t<div class="inner">\n\t\t\t\t\t\t\t<!-- <header class="major">\n\t\t\t\t\t\t\t\t<h2>Accumsan mus tortor nunc aliquet</h2>\n\t\t\t\t\t\t\t\t<p>Aliquam ut ex ut augue consectetur interdum. Donec amet imperdiet eleifend<br />\n\t\t\t\t\t\t\t\tfringilla tincidunt. Nullam dui leo Aenean mi ligula, rhoncus ullamcorper.</p>\n\t\t\t\t\t\t\t</header>\n\t\t\t\t\t\t\t<ul class="features">\n\t\t\t\t\t\t\t\t<li class="icon fa-paper-plane-o">\n\t\t\t\t\t\t\t\t\t<h3>Arcu accumsan</h3>\n\t\t\t\t\t\t\t\t\t<p>Augue consectetur sed interdum imperdiet et ipsum. Mauris lorem tincidunt nullam amet leo Aenean ligula consequat consequat.</p>\n\t\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t<li class="icon fa-laptop">\n\t\t\t\t\t\t\t\t\t<h3>Ac Augue Eget</h3>\n\t\t\t\t\t\t\t\t\t<p>Augue consectetur sed interdum imperdiet et ipsum. Mauris lorem tincidunt nullam amet leo Aenean ligula consequat consequat.</p>\n\t\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t<li class="icon fa-code">\n\t\t\t\t\t\t\t\t\t<h3>Mus Scelerisque</h3>\n\t\t\t\t\t\t\t\t\t<p>Augue consectetur sed interdum imperdiet et ipsum. Mauris lorem tincidunt nullam amet leo Aenean ligula consequat consequat.</p>\n\t\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t<li class="icon fa-headphones">\n\t\t\t\t\t\t\t\t\t<h3>Mauris Imperdiet</h3>\n\t\t\t\t\t\t\t\t\t<p>Augue consectetur sed interdum imperdiet et ipsum. Mauris lorem tincidunt nullam amet leo Aenean ligula consequat consequat.</p>\n\t\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t<li class="icon fa-heart-o">\n\t\t\t\t\t\t\t\t\t<h3>Aenean Primis</h3>\n\t\t\t\t\t\t\t\t\t<p>Augue consectetur sed interdum imperdiet et ipsum. Mauris lorem tincidunt nullam amet leo Aenean ligula consequat consequat.</p>\n\t\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t<li class="icon fa-flag-o">\n\t\t\t\t\t\t\t\t\t<h3>Tortor Ut</h3>\n\t\t\t\t\t\t\t\t\t<p>Augue consectetur sed interdum imperdiet et ipsum. Mauris lorem tincidunt nullam amet leo Aenean ligula consequat consequat.</p>\n\t\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t</ul>-->\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</section>\n\n\t\t\t\t<!-- CTA -->\n\n\t\t\t</div>\n\n\t\t<!-- Scripts -->\n\t\t\t<script src="assets/js/jquery.min.js"></script>\n\t\t\t<script src="assets/js/jquery.scrollex.min.js"></script>\n\t\t\t<script src="assets/js/jquery.scrolly.min.js"></script>\n\t\t\t<script src="assets/js/browser.min.js"></script>\n\t\t\t<script src="assets/js/breakpoints.min.js"></script>\n\t\t\t<script src="assets/js/util.js"></script>\n\t\t\t<script src="assets/js/main.js"></script>\n\n\t</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/eric/Documents/bchain/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "45": 11, "50": 119, "56": 3, "62": 3, "68": 13, "76": 13, "77": 51, "78": 51, "79": 56, "80": 56, "81": 61, "82": 61, "88": 82}}
__M_END_METADATA
"""
