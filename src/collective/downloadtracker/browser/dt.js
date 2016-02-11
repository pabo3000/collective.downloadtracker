$(document).ready(function() {
  $('.documentByLine td a').click(function() {
    var td = $(this).parent();
    var tr = td.parent();
    var name = td.prev().prev().text();
    var date = td.prev().text();
    var url = window.location.href.replace(/view/, "delete");
    // alert('Handler for .click() called.');
    $.getJSON(
      url, {
        name: name,
        date: date
      },
      function(data) {
        // im Erfolgsfall Seite neuladen
        if (data === true) {
          tr.remove();
          //location.reload();
        }
      }
    );
    return false;
  });
});
