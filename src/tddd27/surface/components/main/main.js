/* main component JS resource */
var main = {
    init: function() {

        $("form").submit(function (e) {
            e.preventDefault();
            $.post($(this).attr("action"), $(this).serialize());
            $("input[name=body]").val("").focus();
        });

        $("input[type=text]").placeholder();


        Push.bind("ChatMsgReceived", function (event) {
            var msgElement = $("#chatMsgTmpl").tmpl(event.data);
            $(".chat ul").append(msgElement)
            $(".chat .scroller").scrollTop($(".chat .scroller ul").outerHeight())

        })
    }
};
