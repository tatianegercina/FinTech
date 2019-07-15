'use strict';

function User (firstName, lastName, email) {
  this.firsTName = firstName;
  this.lastName = lastName;
  this.email = email;
}

User.prototype.fullName = function () {
  return this.firstname + " " + this.lastname;
}
