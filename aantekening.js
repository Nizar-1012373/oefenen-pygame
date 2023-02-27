// het gebruiken van built in functions and libraries

// math object
// afronden en inkorten

// rond een nummer af boven de volgende integer
Math.ceil()

// rond een nummer af naar beneden de volgende integer
Math.floor()

// rond een nummer naar de dichtbijzende integer
Math.round()

// voorbeeld
function round(num) {
  return Math.round(num * 100) / 100;
}

// Math.random
function rand(num) {
  return Math.floor(Math.random() * num) + 1;
}

//with keyword\
//voorbeeld
with (lastname) {
  window.alert("length of last name: " + length);
  capname = toUpperCase();
}

// Date object
// hiermee kan je werken met datums en tijden
// voorbeeelden
birthday = new Date();
birthday = new Date("June 20, 2003 08:00:00");
birthday = new Date(6, 20, 2003);
birthday = new Date(6, 20, 2003, 8, 0, 0);
// . setDate() sets the day of the month.
// . setMonth() sets the month. JavaScript numbers the months from 0 to 11,
// starting with January (0).
// . setFullYear() sets the year.
// . setTime() sets the time (and the date) by specifying the number of milliseconds since January 1, 1970.
// . setHours(), setMinutes(), and setSeconds() set the time.