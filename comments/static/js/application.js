$.fn.initCommentPage = function() {
    var $this = this;

    $this.$form = $('#new-comment');

    $this.$form.on('submit', function(e) {
        event.preventDefault();

        $('form .help-error').each(function(){
            this.remove();
        })

        $.ajax({
            url: '/comments',
            data: $($this.$form).serialize(),
            type: "POST",
            dataType: 'json',
            success: function(data) {
                $this.$form.find('input[name="email"], textarea[name="body"]').each(function(){
                    $(this).val('');
                })

                var li = $("<li></li>").html("<div class='text-center'>" + data.body + "</div><div class='text-right'><b>email:</b> " + data.email + ", <b>created at:</b> " + data.created_at + "</div>");
                if($('#comments-list li').length > 0) {
                    $('#comments-list li:last-child').after(li);
                }else{
                    $('#comments-list').append(li);
                }

                $('html, body').animate({scrollTop: $this.$form.offset().top}, 'slow');
            },
            error: function(data) {
                $.each(data.responseJSON, function(key, value) {
                    $this.$form.find("#" + key).after("<div class='help-error'>" + value.join(' ') + "</div>");
                });
            }
        })
    });
}

$(document).ready(function(){
    $('#comments-page').initCommentPage();
})
