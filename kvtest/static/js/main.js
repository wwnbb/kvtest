$(function() {
    $('div.mytree div:has(div)').addClass('parent'); 
    $('div.active').children('div').toggle();
    $('div.active').parents('.parent').each(function() {
        $(this).children('div').toggle();
        $(this).addClass('expanded');
    });
}());
