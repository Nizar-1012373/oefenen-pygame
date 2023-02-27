//if statement
if (a == 1) {
  window.alert("Found a 1!");
  a = 0;
}

if (phone == "" || email == "") window.alert("Something’s Missing!");
//    || betekent or
// && betekent and
// ! betekent not
// != betekent not equal

//else statement
if (a == 1) {
  alert("Found a 1!");
  a = 0;
}
else {
  alert("Incorrect value: " + a);
}
// shorthand conditional expression
variable = (condition) ? (true action) : (false action);
// voorbeeld beneden
value = (a == 1) ? 1 : 0;
// is gelijk aan de statement beneden
if (a == 1)
  value = 1;
else
  value = 0;
// ? = true 
// : = false is ook wel de else statement
// voorbeeld:
document.write("Found " + counter + ((counter == 1) ? "word." : "words."));

// switch statements 
switch (button) {
  case "next":
    window.location = "next.html";
    break;
  case "previous":
    window.location = "prev.html";
    break;
  case "home":
    window.location = "home.html";
    break;
  case "back":
    window.location = "menu.html";
    break;
  default:
    window.alert("Wrong button.");
}

// for loops
// for loops stopt tot de condition gelijk staat aan de vastgestelde waarde
// var = 1; is een initial expression
// var < 10 is een condition
// var++ is een increment(verhoogde) expression 
//het verhoogd de originele nummer in de condition
// en herhaald zich steeds

for (var = 1; var < 10; var++) {
}

// voorbeeld
// als er maar 1 statement zit mag je deze haakjes "{}"
//weg laten maar beter om ze te houden
for (i = 0; i < 10; i++) {
  document.write("This is line " + i + "<br>");
}

// while loops
// while loops stopt tot dat de condition true is
// while loops doen niks als de initialeze false is
// deze while gebruikt een teller "[n]" om te herhalen
// door de "values" array.
// dit kan je ook gebruiken voor een for loop
while (total < 10) {
  n++;
  total += values[n];
}

// do...while loops
// zelfde als normale while loops met 1 verschil,
// dat ze de conditie testen aan het einde van de loop
// en niet aan het begin


do {
  n++;
  total += values[n];
}
while (total < 10);

//infinite loops
// deze blijven de hele tijd de excuteren tot dat
// de gebuiker het stopt of tot dat er een error komt.

// voorbeeld
// dit zal altijd blijven executeren omdat "i" hetzelfde blijft

while (i < 10) {
  n++;
  values[n] = 0;
}

// escaping from a loop
// gebruik maken van een break
// die skipt de rest van de loop en gaat verder met de eerste
// statement.
//voorbeeld
while (true) {
  n++;
  if (values[n] == 1) break;
}

//continuing a loop
// de continue statement skipt de rest van de loop maar,
// in tegenstelling tot de break gaat het verder met de volgende
// herhaling van de loop.
//voorbeeld
// deze for loop print de scores uit voor 20 studenten die zijn bewaard
// in de "score" array
for (i = 1; i < 21; i++) {
  if (score[i] == 0) continue;
  document.write("Student number ", i, " Score: ", score[i], "\n");
}

// for in loops
// worden gebruikt voor properties van een object
// voorbeeld
for (i in navigator) {
  document.write("property: " + i);
  document.write(" value: " + navigator[i] + "<br>");
}