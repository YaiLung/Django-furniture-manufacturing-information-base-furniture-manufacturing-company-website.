$(window).load(function() {
  $("[data-toggle]").click(function() {
  var toggle_el = $(this).data("toggle");
  $(toggle_el).toggleClass("open-dukemapen-somenon");
  });
  $(".consum-dersidsnum").swipe({
  swipeStatus: function(event, phase, direction, distance, duration, fingers) {
  if (phase == "move" && direction == "right") {
  $(".kigasea-deisogan").addClass("open-dukemapen-somenon");
  return false;
  }
  if (phase == "move" && direction == "left") {
  $(".kigasea-deisogan").removeClass("open-dukemapen-somenon");
  return false;
  }
  }
  });
  });