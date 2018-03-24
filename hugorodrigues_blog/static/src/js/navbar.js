odoo.define('hugorodrigues_blog.navbar', function(require) {
    "use strict";

    $(window).scroll(function() {
        var st = $(this).scrollTop();
        var navbar = $('.navbar')
        if (st == 0) {
            navbar.addClass('pg-on-top');
        } else {
            navbar.removeClass('pg-on-top');
        }
    });
});
