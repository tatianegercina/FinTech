'use strict';

for (var i = 0; i < 5; i += 1) {
  setTimeout(function () {
      console.log(i);
    }, i * 1000);
}
