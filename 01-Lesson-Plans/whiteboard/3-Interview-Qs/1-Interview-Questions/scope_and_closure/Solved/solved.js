'use strict';

function foo () {
  var updated = 0;
  var obj = {};

  var bar = function (arg) {
    var key = JSON.stringify(arg);

    if (!(obj[key])) {
      obj[key] = arg
      updated += 1;
    }

    console.log("You've updated the object " + updated + " times.");
    return obj[key];
  }

  return bar;
}
