// window.onload = function () {
//
//     console.log("JavaScript file loaded");
//
// }
$(document).ready(function() {
    console.log("JavaScript file loaded");
    $('.list-group-item').click(function() {
    var index = $(this).index();
    var text = $(this).text();
    alert('Index is: ' + index + ' and text is ' + text);
    });
});
