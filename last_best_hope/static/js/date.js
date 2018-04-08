require(["jquery"], function($) {
  "use strict";
  var fixDates = function() {
    for(var dt of $(".date")) {
      var $dt = $(dt);
      $dt.text(new Date($dt.text()));
    }
  };
  $(fixDates);
});
