'use strict';

var A = A || {};
A.controllers = {};

A.controllers.AuthController = Spine.Controller.sub({
    el: $('*[data-auth="required"]'),

    events: {
        'click': 'click'
    },

    click: function(event) {
        var target = $(event.target);
        console.log(target);
    }

});

/**
 * Comics inner navigation
 */
A.controllers.ComicsNavigation = Spine.Controller.sub({
    el: $('ul.navigation-inner'),

    init: function() {
        A.models.Chapter.fetch();
        A.models.Comics.fetch();
    },

    events: {
        'change select[name="chapter"]': 'chapter',
        'change select[name="comics"]': 'comics'
    },

    chapter: function(event) {
        var target = $(event.target);
        var selects = this.el.find('select[name="chapter"]');
        var option = target.find('option:selected');
        var value = parseInt(option.data('id'));

        // Propagate selected value to the all chapter selectors
        selects.find('option').removeAttr('selected');
        selects.find('option[data-id="'+value+'"]').attr('selected', 'selected');

        // Redraw comics selectors
        var comics_selects = this.el.find('select[name="comics"]');
        comics_selects.empty();
        var comics = A.models.Comics.select(function(obj) { return obj.chapter_id == value; });
        for (var i= 0; i<comics.length; i++) {
            var entry = comics[i];
            comics_selects.append($('<option value="'+entry.get_absolute_url()+'" data-id="'+entry.position+'">'+entry.title+'</option>'));
        }

    },

    comics: function(event) {
        var target = $(event.target);
        window.location = target.val();
        // TODO: in fact, we can render selected comics without a redirect
    }

});
new A.controllers.ComicsNavigation();

/**
 * FAQ form submit
 */
A.controllers.FaqForm = Spine.Controller.sub({
    el: $('section.faq form'),

    events: {
        'keyup textarea': 'change',
        'submit': 'submit'
    },

    change: function(event) {
        var target = $(event.target);
        if (target.val().length == 0) {
            this.el.find('input[type="submit"]').attr('disabled', 'disabled');
        } else {
            this.el.find('input[type="submit"]').removeAttr('disabled');
        }
    },

    submit: function(event) {
        this.el.find('input[type="submit"]').attr('disabled', 'disabled');
    }

});

new A.controllers.FaqForm();