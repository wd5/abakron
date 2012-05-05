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


A.controllers.CommentList = Spine.Controller.sub({

    el: $('section.comments'),

    events: {
        'click a.comment-reply': 'reply',
        'click a.comment-cancel': 'cancel',
        'keyup textarea': 'keyup',
        'submit form': 'submit'
    },

    reply: function(event) {
        event.preventDefault();
        var target = $(event.target);
        var container = target.parents('li');
        console.log(container);
        var form = $('#comment-form');

        this.el.find('a.comment-reply').show();
        form.appendTo(container);
        form.find('input[name="parent"]').val(container.data('id'));
        target.hide();
    },

    cancel: function(event) {
        event.preventDefault();
        $(event.target).parents('li').find('a.comment-reply').show();
        var form = $('#comment-form');
        form.appendTo(this.el);
        form.find('input[name="parent"]').removeAttr('value');
    },

    keyup: function(event) {
        // TODO: disable submit button if there is no comment text
    },

    /**
     * Submit form via AJAX
     */
    submit: function(event) {
        event.preventDefault();

        var form = $(event.target);
        $.post(form.attr('action'), {
            parent: form.find('input[name="parent"]').val(),
            content: form.find('textarea').val()
        }, function(response) {
            console.log(response);
        });
    },

    update: function() {
        $.getJSON(django_url_reverse('api.comments', ['blog', 1]), function(response) {
            console.log(response);
        });
    }

});
new A.controllers.CommentList();


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