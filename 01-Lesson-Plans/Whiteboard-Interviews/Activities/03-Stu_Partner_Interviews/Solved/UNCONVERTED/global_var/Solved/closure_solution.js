'use strict';

for (var i = 0; i < 5; i += 1) {
  (function (j) {
    setTimeout(function () {
      console.log(j);
    }, j * 1000);
  })(i);
}
