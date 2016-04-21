$(function () {

    $("#txtInput").keydown(function (key) {
        if (key.keyCode == 13) {
            var val = $("#txtInput").val();
            if (val == "") {
              alert('공백 입력 나빠요');
            }
        }
    });

});
