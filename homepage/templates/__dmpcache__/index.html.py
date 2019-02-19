# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1550591820.4590359
_enable_loop = True
_template_filename = '/Users/nicoletucker/Dev/bchain/homepage/templates/index.html'
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
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def __M_anon_3():
            return render___M_anon_3(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
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
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n<!DOCTYPE HTML>\n<!--\n\tSpectral by HTML5 UP\n\thtml5up.net | @ajlkn\n\tFree for personal and commercial use under the CCA 3.0 license (html5up.net/license)\n-->\n<html>\n\t<body class="landing is-preload">\n\t\t<!-- Page Wrapper -->\n\t\t\t<div id="page-wrapper">\n\n\t\t\t\t<!-- Banner -->\n\t\t\t\t\t<section id="banner">\n\t\t\t\t\t\t<div class="inner">\n\t\t\t\t\t\t\t<h2>Beef Blockchain</h2>\n\t\t\t\t\t\t\t<p>Organice meat<br />\n\t\t\t\t\t\t\tand produce<br />\n\t\t\t\t\t\t\tgaurenteed</p>\n\t\t\t\t\t\t\t<ul class="actions special">\n\t\t\t\t\t\t\t\t<li><a href="#" class="button primary">Login</a></li>\n\t\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t<a href="#one" class="more scrolly">Learn More</a>\n\t\t\t\t\t</section>\n\n\t\t\t\t<!-- One -->\n\t\t\t\t\t<section id="one" class="wrapper style1 special">\n\t\t\t\t\t\t<div class="inner">\n\t\t\t\t\t\t\t<header class="major">\n\t\t\t\t\t\t\t\t<h2>Arcu aliquet vel lobortis ata nisl<br />\n\t\t\t\t\t\t\t\teget augue amet aliquet nisl cep donec</h2>\n\t\t\t\t\t\t\t\t<p>Aliquam ut ex ut augue consectetur interdum. Donec amet imperdiet eleifend<br />\n\t\t\t\t\t\t\t\tfringilla tincidunt. Nullam dui leo Aenean mi ligula, rhoncus ullamcorper.</p>\n\t\t\t\t\t\t\t</header>\n\t\t\t\t\t\t\t<ul class="icons major">\n\t\t\t\t\t\t\t\t<li><span class="icon fa-diamond major style1"><span class="label">Lorem</span></span></li>\n\t\t\t\t\t\t\t\t<li><span class="icon fa-heart-o major style2"><span class="label">Ipsum</span></span></li>\n\t\t\t\t\t\t\t\t<li><span class="icon fa-code major style3"><span class="label">Dolor</span></span></li>\n\t\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</section>\n\n\t\t\t\t<!-- Two -->\n\t\t\t\t\t<section id="two" class="wrapper alt style2">\n\t\t\t\t\t\t<section class="spotlight">\n\t\t\t\t\t\t\t<div class="image"><img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/images/grain.jpg" alt="" /></div><div class="content">\n\t\t\t\t\t\t\t\t<h2>Magna primis lobortis<br />\n\t\t\t\t\t\t\t\tsed ullamcorper</h2>\n\t\t\t\t\t\t\t\t<p>Aliquam ut ex ut augue consectetur interdum. Donec hendrerit imperdiet. Mauris eleifend fringilla nullam aenean mi ligula.</p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</section>\n\t\t\t\t\t\t<section class="spotlight">\n\t\t\t\t\t\t\t<div class="image"><img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/images/chickens.jpg" alt="" /></div><div class="content">\n\t\t\t\t\t\t\t\t<h2>Tortor dolore feugiat<br />\n\t\t\t\t\t\t\t\telementum magna</h2>\n\t\t\t\t\t\t\t\t<p>Aliquam ut ex ut augue consectetur interdum. Donec hendrerit imperdiet. Mauris eleifend fringilla nullam aenean mi ligula.</p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</section>\n\t\t\t\t\t\t<section class="spotlight">\n\t\t\t\t\t\t\t<div class="image"><img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/images/farmer.jpg" alt="" /></div><div class="content">\n\t\t\t\t\t\t\t\t<h2>Augue eleifend aliquet<br />\n\t\t\t\t\t\t\t\tsed condimentum</h2>\n\t\t\t\t\t\t\t\t<p>Aliquam ut ex ut augue consectetur interdum. Donec hendrerit imperdiet. Mauris eleifend fringilla nullam aenean mi ligula.</p>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</section>\n\t\t\t\t\t</section>\n\n\t\t\t\t<!-- Three -->\n\t\t\t\t\t<section id="three" class="wrapper style3 special">\n\t\t\t\t\t\t<div class="inner">\n\t\t\t\t\t\t\t<header class="major">\n\t\t\t\t\t\t\t\t<h2>Accumsan mus tortor nunc aliquet</h2>\n\t\t\t\t\t\t\t\t<p>Aliquam ut ex ut augue consectetur interdum. Donec amet imperdiet eleifend<br />\n\t\t\t\t\t\t\t\tfringilla tincidunt. Nullam dui leo Aenean mi ligula, rhoncus ullamcorper.</p>\n\t\t\t\t\t\t\t</header>\n\t\t\t\t\t\t\t<ul class="features">\n\t\t\t\t\t\t\t\t<li class="icon fa-paper-plane-o">\n\t\t\t\t\t\t\t\t\t<h3>Arcu accumsan</h3>\n\t\t\t\t\t\t\t\t\t<p>Augue consectetur sed interdum imperdiet et ipsum. Mauris lorem tincidunt nullam amet leo Aenean ligula consequat consequat.</p>\n\t\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t<li class="icon fa-laptop">\n\t\t\t\t\t\t\t\t\t<h3>Ac Augue Eget</h3>\n\t\t\t\t\t\t\t\t\t<p>Augue consectetur sed interdum imperdiet et ipsum. Mauris lorem tincidunt nullam amet leo Aenean ligula consequat consequat.</p>\n\t\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t<li class="icon fa-code">\n\t\t\t\t\t\t\t\t\t<h3>Mus Scelerisque</h3>\n\t\t\t\t\t\t\t\t\t<p>Augue consectetur sed interdum imperdiet et ipsum. Mauris lorem tincidunt nullam amet leo Aenean ligula consequat consequat.</p>\n\t\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t<li class="icon fa-headphones">\n\t\t\t\t\t\t\t\t\t<h3>Mauris Imperdiet</h3>\n\t\t\t\t\t\t\t\t\t<p>Augue consectetur sed interdum imperdiet et ipsum. Mauris lorem tincidunt nullam amet leo Aenean ligula consequat consequat.</p>\n\t\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t<li class="icon fa-heart-o">\n\t\t\t\t\t\t\t\t\t<h3>Aenean Primis</h3>\n\t\t\t\t\t\t\t\t\t<p>Augue consectetur sed interdum imperdiet et ipsum. Mauris lorem tincidunt nullam amet leo Aenean ligula consequat consequat.</p>\n\t\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t<li class="icon fa-flag-o">\n\t\t\t\t\t\t\t\t\t<h3>Tortor Ut</h3>\n\t\t\t\t\t\t\t\t\t<p>Augue consectetur sed interdum imperdiet et ipsum. Mauris lorem tincidunt nullam amet leo Aenean ligula consequat consequat.</p>\n\t\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</section>\n\n\t\t\t\t<!-- CTA -->\n\t\t\t\t\t<section id="cta" class="wrapper style4">\n\t\t\t\t\t\t<div class="inner">\n\t\t\t\t\t\t\t<header>\n\t\t\t\t\t\t\t\t<h2>Arcue ut vel commodo</h2>\n\t\t\t\t\t\t\t\t<p>Aliquam ut ex ut augue consectetur interdum endrerit imperdiet amet eleifend fringilla.</p>\n\t\t\t\t\t\t\t</header>\n\t\t\t\t\t\t\t<ul class="actions stacked">\n\t\t\t\t\t\t\t\t<li><a href="#" class="button fit primary">Get Started</a></li>\n\t\t\t\t\t\t\t\t<li><a href="#" class="button fit">Learn More</a></li>\n\t\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</section>\n\n\t\t\t\t<!-- Footer -->\n\t\t\t\t\t<footer id="footer">\n\t\t\t\t\t\t<ul class="icons">\n\t\t\t\t\t\t\t<li><a href="#" class="icon fa-twitter"><span class="label">Twitter</span></a></li>\n\t\t\t\t\t\t\t<li><a href="#" class="icon fa-facebook"><span class="label">Facebook</span></a></li>\n\t\t\t\t\t\t\t<li><a href="#" class="icon fa-instagram"><span class="label">Instagram</span></a></li>\n\t\t\t\t\t\t\t<li><a href="#" class="icon fa-dribbble"><span class="label">Dribbble</span></a></li>\n\t\t\t\t\t\t\t<li><a href="#" class="icon fa-envelope-o"><span class="label">Email</span></a></li>\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t<ul class="copyright">\n\t\t\t\t\t\t\t<li>&copy; Untitled</li><li>Design: <a href="http://html5up.net">HTML5 UP</a></li>\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t</footer>\n\n\t\t\t</div>\n\n\t\t<!-- Scripts -->\n\t\t\t<script src="assets/js/jquery.min.js"></script>\n\t\t\t<script src="assets/js/jquery.scrollex.min.js"></script>\n\t\t\t<script src="assets/js/jquery.scrolly.min.js"></script>\n\t\t\t<script src="assets/js/browser.min.js"></script>\n\t\t\t<script src="assets/js/breakpoints.min.js"></script>\n\t\t\t<script src="assets/js/util.js"></script>\n\t\t\t<script src="assets/js/main.js"></script>\n\n\t</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/nicoletucker/Dev/bchain/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "45": 11, "50": 160, "56": 3, "62": 3, "68": 13, "76": 13, "77": 60, "78": 60, "79": 67, "80": 67, "81": 74, "82": 74, "88": 82}}
__M_END_METADATA
"""
