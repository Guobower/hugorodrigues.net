"""Track website visitors"""

from odoo import http
from odoo.http import request


class VisitorTracker(http.Controller):

    @http.route(['/website/visitor/tracker'], type='http', auth='public')
    def tracker(self, **post):
        source_ip = http.request.httprequest.environ.get('REMOTE_ADDR', '')
        user_agent = http.request.httprequest.environ.get('HTTP_USER_AGENT',
                                                          '')
        WebsiteVisitor = request.env['website.analytics.visitor'].sudo()
        visitor = request.session.get('tracker_visitor_id', False)
        new_cookies = {}
        if not visitor:
            # Find a existing visitor via cookies
            visitor = request.httprequest.cookies.get('tracker_visitor_id',
                                                      False)
            if visitor:
                visitor = int(visitor)
            else:
                # Create a new visitor
                visitor = WebsiteVisitor.create({})
                new_cookies['tracker_visitor_id'] = str(visitor.id)
            request.session['tracker_visitor_id'] = visitor.id
        if isinstance(visitor, int):
            visitor = WebsiteVisitor.browse(visitor)
        visitor.write({
            'ip': source_ip,
            'user_id': request.uid
            })

        # TODO Map country in controller
        # TODO Map browser
        return request.make_response('', cookies=new_cookies)
