'use strict';

var A = A || {};
A.controllers = {};

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
