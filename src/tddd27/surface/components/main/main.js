/* main component JS resource */
var main = {
    init: function() {

        $("form").submit(function (e) {
            e.preventDefault();

        });

        $("input[type=text]").placeholder();


    }
};
