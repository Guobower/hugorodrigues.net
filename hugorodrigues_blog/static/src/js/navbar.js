odoo.define('hugorodrigues_blog.navbar', function(require) {
    "use strict";

    $(document).ready(function() {
        var navbar = $('.navbar');
        if ($('#wrapwrap').height() > $(window).height()) {
            $(window).scroll(function() {
                var st = $(this).scrollTop();
                if (st == 0) {
                    navbar.addClass('pg-on-top');
                } else {
                    navbar.removeClass('pg-on-top');
                }
            });
        } else {
            navbar.addClass('notransition');
            navbar.removeClass('pg-on-top');
            $('main').addClass('noscroll');
        }
    });
});
