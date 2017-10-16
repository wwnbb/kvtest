$(function() {
    $('div.mytree div:has(div)').addClass('parent'); 

    $('div.active').children('div').toggle();

    if ($('div.active').hasClass('parent')) {
        $('div.active').addClass('expanded')
    }

    $('div.active').parents('.parent').each(function() {
        $(this).children('div').toggle();
        $(this).addClass('expanded');
    });

}());
