function getCaretPos(jQObject) {
    var obj = jQObject.get(0);

    obj.focus();

    if (document.selection) {
        var sel = document.selection.createRange();
        var clone = sel.duplicate();

        sel.collapse(true);
        clone.moveToElementText(obj);
        clone.setEndPoint('EndToEnd', sel);

        return clone.text.length;
    } else if (obj.selectionStart !== false) {
        return obj.selectionStart;
    } else {
        return 0;
    }
}


function getImageList(url) {
    $.getJSON(url, function (data) {
        var images = $('#imagepool_image_list').find('td.image'),
            link_prev = $('#imagepool_prev'),
            link_next = $('#imagepool_next');

        images.empty();

        for (var i = 0; i < data.images.length; i++) {

            $(images.get(i)).append('<a class="insert" href="' + data.images[i].src + '">' +
                '<img src="' + data.images[i].src + '"' +
                '</a><br>' +
                '<a class="delete" href="' + data.images[i].delete_src + '">Удалить</a>')

        }

        if (data.prev_url == '') {
            link_prev.addClass('disabled').attr('href', '#');
        } else {
            link_prev.removeClass('disabled').attr('href', data.prev_url)
        }

        if (data.next_url == '') {
            link_next.addClass('disabled').attr('href', '#');
        } else {
            link_next.removeClass('disabled').attr('href', data.next_url)
        }

    })
}


$(function () {
    var contentField = $('form textarea[name=content]');

    $('#imagepool_prev, #imagepool_next').click(function (evt) {
        evt.preventDefault();
        getImageList($(this).attr('href'));
    });

    $('#imagepool_output').on('load', function () {
        getImageList($('#imagepool_image_list').attr('data-href'))
    });

    $('#imagepool_image_list').on('click', 'td.image a.insert', function(evt){
        evt.preventDefault();

        var content = contentField.val(),
            position = getCaretPos(contentField);

        content = content.substring(0, position) + '[img]' + location.protocol + '//' + location.host +
                $(this).attr('href') + '[/img]' + content.substring(position);
        contentField.val(content);
    });
});