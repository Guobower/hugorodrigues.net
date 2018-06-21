"""Track website visitors"""

from odoo import http
from odoo.http import request


class VisitorTracker(http.Controller):

    @http.route(['/website/visitor/tracker'], type='http', auth='public')
    def tracker(self, **post):
        WebsiteVisitor = request.env['website.analytics.visitor'].sudo()
        WebsiteVisit = request.env['website.analytics.visit'].sudo()
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
            'ip': request.httprequest.remote_addr or '',
            'user_id': request.uid
            })

        # TODO prevent duplicated
        user_agent = request.httprequest.environ.get('HTTP_USER_AGENT', '')
        WebsiteVisit.create({'visitor_id': visitor.id,
                             'user_agent': user_agent,
                             'source': request.httprequest.referrer,
                             'path': request.httprequest.path})
        return request.make_response('', cookies=new_cookies)
