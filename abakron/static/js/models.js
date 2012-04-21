'use strict';

var A = A || {};
A.models = {};

A.models.Chapter = Spine.Model.sub();
A.models.Chapter.configure('Chapter', 'title', 'slug', 'cover_url');
A.models.Chapter.extend(Spine.Model.Ajax);
A.models.Chapter.extend({
   url: django_url_reverse('api.comics.chapters')
});
A.models.Chapter.include({
    get_absolute_url: function() {
        return django_url_reverse('comics.chapters.read', [this.slug]);
    }
});

A.models.Comics = Spine.Model.sub();
A.models.Comics.configure('Comics', 'chapter', 'title', 'image_url', 'alt');
A.models.Comics.extend(Spine.Model.Ajax);
A.models.Comics.extend({
    url: django_url_reverse('api.comics'),
});
A.models.Comics.include({
    get_absolute_url: function() {
        return django_url_reverse('comics.read', [this.chapter().slug, this.position]);
    }
})
A.models.Comics.belongsTo('chapter', 'A.models.Chapter');
